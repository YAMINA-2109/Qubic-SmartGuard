"""
Qubic Network Integration Module
Provides real-time connection to Qubic blockchain for contract validation
"""

import asyncio
import logging
import os
import time
from typing import Any, Dict

import aiohttp
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


class QubicNetworkClient:
    """Client for interacting with Qubic blockchain network"""

    def __init__(self):
        self.rpc_url = os.getenv("QUBIC_RPC_URL", "https://rpc.qubic.org")
        self.network_id = os.getenv("QUBIC_NETWORK_ID", "mainnet")
        self.testnet_url = os.getenv("QUBIC_TESTNET_RPC_URL",
                                     "https://testnet-rpc.qubic.org")
        self.enable_real_network = (
            os.getenv("ENABLE_REAL_NETWORK", "false").lower() == "true"
        )
        self.session = None

    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()

    async def test_connection(self) -> Dict[str, Any]:
        """Test connection to Qubic network"""
        if not self.enable_real_network:
            return {
                "status": "disabled",
                "message": "Real network integration disabled in config",
                "mock": True
            }

        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(
                    total=10)) as session:
                # Test basic connectivity
                async with session.get(f"{self.rpc_url}/health") as response:
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "status": "connected",
                            "network": self.network_id,
                            "rpc_url": self.rpc_url,
                            "block_height": data.get("latest_block", 0),
                            "timestamp": time.time()
                        }
                    else:
                        return {
                            "status": "error",
                            "message": f"HTTP {response.status}",
                            "network": self.network_id
                        }

        except asyncio.TimeoutError:
            return {
                "status": "timeout",
                "message": "Connection timeout to Qubic network",
                "network": self.network_id
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "network": self.network_id
            }

    async def get_network_stats(self) -> Dict[str, Any]:
        """Get current network statistics"""
        if not self.enable_real_network:
            # Return mock data for demo purposes
            return {
                "network_id": "mainnet-mock",
                "block_height": 12345678,
                "total_smart_contracts": 1547,
                "active_validators": 676,
                "network_hashrate": "2.5 PH/s",
                "avg_block_time": "7.2s",
                "total_qubic_supply": "1000000000000",
                "mock": True,
                "timestamp": time.time()
            }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.rpc_url}/stats") as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        raise Exception(
                            f"Failed to get stats: {response.status}")

        except Exception as e:
            logger.error(f"Failed to get network stats: {str(e)}")
            # Return fallback mock data
            return {
                "error": str(e),
                "network_id": self.network_id,
                "mock": True,
                "timestamp": time.time()
            }

    async def validate_contract_on_network(self,
                                           contract_code: str) -> Dict[str, Any]:
        """Validate smart contract against network requirements"""
        if not self.enable_real_network:
            # Mock validation for demo
            return {
                "validation": "mock",
                "compatible": True,
                "qubic_version": "2.0",
                "gas_estimate": 150000,
                "deployment_cost": "100 QUBIC",
                "warnings": [
                    "This is a mock validation",
                    "Enable ENABLE_REAL_NETWORK for real validation"
                ],
                "mock": True
            }

        try:
            validation_payload = {
                "contract_code": contract_code,
                "validate_only": True,
                "network": self.network_id
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.rpc_url}/validate-contract",
                    json=validation_payload
                ) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        error_data = await response.text()
                        return {
                            "validation": "failed",
                            "error": f"HTTP {response.status}: {error_data}",
                            "compatible": False
                        }

        except Exception as e:
            return {
                "validation": "error",
                "error": str(e),
                "compatible": False,
                "message": "Failed to connect to Qubic network for validation"
            }

    async def get_contract_deployment_requirements(self) -> Dict[str, Any]:
        """Get current requirements for smart contract deployment"""
        if not self.enable_real_network:
            return {
                "min_qubic_balance": "1000 QUBIC",
                "gas_limit": 500000,
                "max_contract_size": "64KB",
                "supported_features": [
                    "PUBLIC_PROCEDURE",
                    "PUBLIC_FUNCTION",
                    "State management",
                    "Inter-contract calls"
                ],
                "network_version": "2.0.0",
                "mock": True
            }

        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.rpc_url}/deployment-requirements"
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        raise Exception(f"HTTP {response.status}")

        except Exception as e:
            logger.error(f"Failed to get deployment requirements: {str(e)}")
            # Return sensible defaults
            return {
                "error": str(e),
                "min_qubic_balance": "Unknown",
                "gas_limit": 500000,
                "max_contract_size": "64KB",
                "fallback": True
            }


class QubicSmartContractValidator:
    """Validator for Qubic smart contracts using network integration"""

    def __init__(self):
        self.client = QubicNetworkClient()

    async def comprehensive_validation(self,
                                       contract_code: str) -> Dict[str, Any]:
        """Perform comprehensive validation including network checks"""

        results = {
            "timestamp": time.time(),
            "contract_size": len(contract_code),
            "validation_steps": {}
        }

        # Step 1: Test network connection
        connection_test = await self.client.test_connection()
        results["validation_steps"]["network_connection"] = connection_test

        # Step 2: Get network requirements
        requirements = await self.client.get_contract_deployment_requirements()
        results["validation_steps"]["deployment_requirements"] = requirements

        # Step 3: Validate contract on network
        network_validation = await self.client.validate_contract_on_network(
            contract_code)
        results["validation_steps"]["network_validation"] = network_validation

        # Step 4: Get network stats for context
        network_stats = await self.client.get_network_stats()
        results["validation_steps"]["network_stats"] = network_stats

        # Summary
        results["summary"] = {
            "network_accessible": connection_test.get("status") == "connected",
            "contract_compatible": network_validation.get("compatible", False),
            "ready_for_deployment": (
                connection_test.get("status") == "connected" and
                network_validation.get("compatible", False)
            ),
            "estimated_cost": network_validation.get("deployment_cost", "Unknown"),
            "gas_estimate": network_validation.get("gas_estimate", 0)
        }

        return results


# Convenience functions for easy integration
async def test_qubic_network_connection():
    """Quick test of Qubic network connectivity"""
    async with QubicNetworkClient() as client:
        return await client.test_connection()


async def validate_contract_with_network(contract_code: str):
    """Validate a contract with full network integration"""
    validator = QubicSmartContractValidator()
    return await validator.comprehensive_validation(contract_code)


def get_qubic_network_status():
    """Get current Qubic network status (sync wrapper)"""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return loop.run_until_complete(test_qubic_network_connection())

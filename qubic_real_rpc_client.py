"""
Real Qubic Network Data Fetcher - UPDATED with Official RPC Endpoints
Uses actual Qubic RPC API: https://rpc.qubic.org
"""

import os
import time
from datetime import datetime
from typing import Dict, List, Optional

import requests


class RealQubicDataFetcher:
    """
    Fetches REAL data from Qubic blockchain using official RPC endpoints.
    Documentation: https://qubic.github.io/integration/Partners/swagger/qubic-rpc-doc.html
    """

    def __init__(self):
        # Load from environment variables
        self.rpc_endpoint = os.getenv(
            "QUBIC_RPC_ENDPOINT", "https://rpc.qubic.org")
        self.api_key = os.getenv("QUBIC_API_KEY", "")

        # Check if real endpoints are configured
        self.is_real_mode = bool(self.rpc_endpoint)

        # Cache for performance
        self._cache = {}
        self._cache_timeout = 30  # seconds

    def _get_cached(self, key: str):
        """Get cached data if still valid"""
        if key in self._cache:
            data, timestamp = self._cache[key]
            if time.time() - timestamp < self._cache_timeout:
                return data
        return None

    def _set_cache(self, key: str, data):
        """Cache data with timestamp"""
        self._cache[key] = (data, time.time())

    def _make_request(self, url: str, params: dict = None, method: str = "GET", json_data: dict = None) -> Optional[dict]:
        """Make HTTP request to Qubic RPC API"""
        try:
            headers = {"accept": "application/json"}
            if json_data:
                headers["Content-Type"] = "application/json"
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            if method == "GET":
                response = requests.get(
                    url, params=params, headers=headers, timeout=10)
            else:
                response = requests.post(
                    url, json=json_data, headers=headers, timeout=10)

            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ API Error: {e}")
            return None

    def get_network_status(self) -> Dict:
        """
        Get REAL network status from Qubic blockchain
        Uses: GET https://rpc.qubic.org/v1/status
        """
        cached = self._get_cached("network_status")
        if cached:
            return cached

        if not self.is_real_mode:
            return {
                "status": "demo_mode",
                "error": "No RPC endpoint configured"
            }

        # Use official Qubic RPC /v1/status endpoint
        try:
            status_url = f"{self.rpc_endpoint.rstrip('/')}/v1/status"
            data = self._make_request(status_url)

            if data:
                last_tick = data.get("lastProcessedTick", {})
                result = {
                    "status": "real_data",
                    "current_tick": last_tick.get("tickNumber", 0),
                    "epoch": last_tick.get("epoch", 0),
                    "initial_tick": data.get("initialTick", 0),
                    "number_of_entities": data.get("numberOfEntities", 0),
                    "number_of_transactions": data.get("numberOfTransactions", 0),
                    "timestamp": datetime.now().isoformat()
                }
                self._set_cache("network_status", result)
                return result
        except Exception as e:
            print(f"Error fetching network status: {e}")

        return {"status": "error", "error": "Failed to fetch network data"}

    def get_tick_info(self) -> Dict:
        """
        Get current tick information
        Uses: GET https://rpc.qubic.org/v1/tick-info
        """
        cached = self._get_cached("tick_info")
        if cached:
            return cached

        if not self.is_real_mode:
            return {"status": "demo_mode"}

        try:
            url = f"{self.rpc_endpoint.rstrip('/')}/v1/tick-info"
            data = self._make_request(url)

            if data and "tickInfo" in data:
                tick_info = data["tickInfo"]
                result = {
                    "status": "real_data",
                    "tick": tick_info.get("tick", 0),
                    "duration": tick_info.get("duration", 0),
                    "epoch": tick_info.get("epoch", 0),
                    "timestamp": datetime.now().isoformat()
                }
                self._set_cache("tick_info", result)
                return result
        except Exception as e:
            print(f"Error fetching tick info: {e}")

        return {"status": "error"}

    def get_transactions_by_tick(self, tick: int) -> Dict:
        """
        Get all transactions for a specific tick
        Uses: GET https://rpc.qubic.org/v2/ticks/{tick}/transactions
        """
        if not self.is_real_mode:
            return {"status": "demo_mode", "transactions": []}

        try:
            url = f"{self.rpc_endpoint.rstrip('/')}/v2/ticks/{tick}/transactions"
            data = self._make_request(url)

            if data:
                transactions = data.get("transactions", [])
                return {
                    "status": "real_data",
                    "tick": tick,
                    "transaction_count": len(transactions),
                    "transactions": transactions,
                    "timestamp": datetime.now().isoformat()
                }
        except Exception as e:
            print(f"Error fetching transactions: {e}")

        return {"status": "error", "transactions": []}

    def get_account_balance(self, public_id: str) -> Dict:
        """
        Get real account balance
        Uses: GET https://rpc.qubic.org/v1/balances/{publicId}
        """
        if not self.is_real_mode or not public_id:
            return {"status": "demo_mode", "balance": 0}

        cached = self._get_cached(f"balance_{public_id}")
        if cached:
            return cached

        try:
            url = f"{self.rpc_endpoint.rstrip('/')}/v1/balances/{public_id}"
            data = self._make_request(url)

            if data and "balance" in data:
                balance_data = data["balance"]
                result = {
                    "status": "real_data",
                    "public_id": public_id,
                    "balance": balance_data.get("balance", 0),
                    "valid_for_tick": balance_data.get("validForTick", 0),
                    "latest_incoming_transfer_tick": balance_data.get("latestIncomingTransferTick", 0),
                    "latest_outgoing_transfer_tick": balance_data.get("latestOutgoingTransferTick", 0),
                    "timestamp": datetime.now().isoformat()
                }
                self._set_cache(f"balance_{public_id}", result)
                return result
        except Exception as e:
            print(f"Error fetching balance: {e}")

        return {"status": "error", "balance": 0}

    def query_smart_contract(self, contract_index: int, input_type: int, request_data: str) -> Dict:
        """
        Query a smart contract (read-only)
        Uses: POST https://rpc.qubic.org/v1/querySmartContract
        """
        if not self.is_real_mode:
            return {"status": "demo_mode"}

        try:
            url = f"{self.rpc_endpoint.rstrip('/')}/v1/querySmartContract"
            payload = {
                "contractIndex": contract_index,
                "inputType": input_type,
                "inputSize": len(request_data) if request_data else 0,
                "requestData": request_data
            }

            data = self._make_request(url, method="POST", json_data=payload)

            if data:
                return {
                    "status": "real_data",
                    "response_data": data.get("responseData", ""),
                    "timestamp": datetime.now().isoformat()
                }
        except Exception as e:
            print(f"Error querying smart contract: {e}")

        return {"status": "error"}

    def get_real_statistics(self) -> Dict:
        """
        Aggregate real network statistics from multiple endpoints
        """
        if not self.is_real_mode:
            return {
                "status": "demo_mode",
                "message": "Configure QUBIC_RPC_ENDPOINT in .env for real data"
            }

        # Get network status
        network = self.get_network_status()
        tick_info = self.get_tick_info()

        return {
            "status": "real_data",
            "network": network,
            "tick_info": tick_info,
            "endpoint": self.rpc_endpoint,
            "timestamp": datetime.now().isoformat()
        }

    def get_recent_activities(self, limit: int = 10) -> List[Dict]:
        """
        Get REAL recent blockchain activities from latest tick
        """
        if not self.is_real_mode:
            return [{
                "type": "info",
                "message": "⚠️ Demo Mode - Configure QUBIC_RPC_ENDPOINT for real data",
                "timestamp": datetime.now().isoformat(),
                "is_demo": True
            }]

        # Get current tick and fetch recent transactions
        tick_info = self.get_tick_info()
        if tick_info.get("status") == "real_data":
            current_tick = tick_info.get("tick", 0)
            if current_tick > 0:
                # Get transactions from recent ticks
                activities = []
                for offset in range(min(5, limit)):
                    tick_data = self.get_transactions_by_tick(
                        current_tick - offset)
                    if tick_data.get("status") == "real_data":
                        tx_count = tick_data.get("transaction_count", 0)
                        if tx_count > 0:
                            activities.append({
                                "type": "transaction",
                                "message": f"✅ {tx_count} transactions in tick {current_tick - offset}",
                                "timestamp": datetime.now().isoformat(),
                                "tick": current_tick - offset,
                                "is_real": True
                            })

                if activities:
                    return activities

        return [{
            "type": "info",
            "message": "📡 Connected to Qubic network - Monitoring for activity",
            "timestamp": datetime.now().isoformat(),
            "is_real": True
        }]

    def is_configured(self) -> bool:
        """Check if real data sources are configured"""
        return self.is_real_mode

    def get_configuration_status(self) -> Dict:
        """Get detailed configuration status"""
        return {
            "rpc_endpoint": f"✅ {self.rpc_endpoint}" if self.rpc_endpoint else "❌ Not set",
            "api_key": "✅ Set" if self.api_key else "ℹ️  Optional",
            "mode": "🟢 Real Data Mode" if self.is_real_mode else "🔴 Demo Mode",
            "cache_enabled": True,
            "cache_timeout": f"{self._cache_timeout}s",
            "official_rpc": "https://rpc.qubic.org"
        }


# Singleton instance
_fetcher_instance = None


def get_real_data_fetcher() -> RealQubicDataFetcher:
    """Get or create singleton fetcher instance"""
    global _fetcher_instance
    if _fetcher_instance is None:
        _fetcher_instance = RealQubicDataFetcher()
    return _fetcher_instance

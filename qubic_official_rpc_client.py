"""
Official Qubic RPC Client - Using Live Tree API
Documentation: https://qubic.github.io/integration/Partners/swagger/qubic-rpc-doc.html
Base URL: https://rpc.qubic.org
"""

import os
import time
from datetime import datetime
from typing import Dict, List, Optional

import requests


class QubicRPCClient:
    """
    Official Qubic RPC Client using Live Tree API endpoints.

    Available Endpoints (GET):
    - /v1/status - Network status
    - /v1/tick-info - Current tick information
    - /v1/balances/{identity} - Get account balance
    - /v1/assets/{identity}/issued - Assets issued by identity
    - /v1/assets/{identity}/owned - Assets owned by identity
    - /v1/assets/{identity}/possessed - Assets possessed by identity
    - /v2/ticks/{tickNumber}/approved-transactions - Approved transactions in tick
    - /v2/ticks/{tickNumber}/chain-hash - Chain hash for tick
    - /v2/ticks/{tickNumber}/quorum-data - Quorum data for tick
    - /v2/ticks/{tickNumber}/store-hash - Store hash for tick
    - /v2/ticks/{tickNumber}/transactions - All transactions in tick

    Available Endpoints (POST):
    - /v1/broadcast-transaction - Broadcast a transaction
    - /v1/query-smart-contract - Query smart contract
    """

    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv(
            "QUBIC_RPC_ENDPOINT", "https://rpc.qubic.org")
        self.base_url = self.base_url.rstrip('/')
        self.timeout = 10
        self._cache = {}
        self._cache_timeout = 30  # Cache for 30 seconds

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

    def _make_request(self, endpoint: str, method: str = "GET", json_data: dict = None) -> Optional[dict]:
        """Make HTTP request to Qubic RPC"""
        url = f"{self.base_url}{endpoint}"

        try:
            headers = {
                "accept": "application/json",
                "User-Agent": "QubicSmartGuard/1.0"
            }

            if method == "GET":
                response = requests.get(
                    url, headers=headers, timeout=self.timeout)
            elif method == "POST":
                headers["Content-Type"] = "application/json"
                response = requests.post(
                    url, headers=headers, json=json_data, timeout=self.timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print(f"⏱️  Timeout connecting to {url}")
            return None
        except requests.exceptions.ConnectionError:
            print(f"🔌 Connection error to {url}")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP error {e.response.status_code}: {url}")
            return None
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None

    # ============================================================================
    # Network Status and Information
    # ============================================================================

    def get_status(self) -> Optional[Dict]:
        """
        GET /v1/status
        Returns current network state including tick information and health metrics.

        Response includes:
        - lastProcessedTick: Latest processed tick
        - lastProcessedTicksPerEpoch: Ticks per epoch information
        - skippedTicks: Information about skipped ticks
        - processedTickIntervalsPerEpoch: Processing intervals
        """
        cached = self._get_cached("status")
        if cached:
            return cached

        data = self._make_request("/v1/status")
        if data:
            self._set_cache("status", data)
        return data

    def get_tick_info(self) -> Optional[Dict]:
        """
        GET /v1/tick-info
        Get current tick information including tick number and timestamp.

        Response includes:
        - tick: Current tick number
        - duration: Duration information
        - epoch: Current epoch
        - numberOfAlignedVotes: Number of aligned votes
        - numberOfMisalignedVotes: Number of misaligned votes
        """
        cached = self._get_cached("tick_info")
        if cached:
            return cached

        data = self._make_request("/v1/tick-info")
        if data:
            self._set_cache("tick_info", data)
        return data

    # ============================================================================
    # Account and Balance Operations
    # ============================================================================

    def get_balance(self, identity: str) -> Optional[Dict]:
        """
        GET /v1/balances/{identity}
        Query QU balance for any identity.

        Args:
            identity: 60-character public ID (address)

        Response includes:
        - balance: Account balance information
        - validForTick: Tick number for which data is valid
        """
        data = self._make_request(f"/v1/balances/{identity}")
        return data

    def get_issued_assets(self, identity: str) -> Optional[Dict]:
        """
        GET /v1/assets/{identity}/issued
        Retrieve all assets issued by an identity.
        """
        data = self._make_request(f"/v1/assets/{identity}/issued")
        return data

    def get_owned_assets(self, identity: str) -> Optional[Dict]:
        """
        GET /v1/assets/{identity}/owned
        Retrieve all assets owned by an identity.
        """
        data = self._make_request(f"/v1/assets/{identity}/owned")
        return data

    def get_possessed_assets(self, identity: str) -> Optional[Dict]:
        """
        GET /v1/assets/{identity}/possessed
        Retrieve all assets possessed by an identity.
        """
        data = self._make_request(f"/v1/assets/{identity}/possessed")
        return data

    # ============================================================================
    # Transaction Operations
    # ============================================================================

    def get_tick_transactions(self, tick_number: int) -> Optional[Dict]:
        """
        GET /v1/ticks/{tickNumber}/transactions
        Get all transactions for a specific tick.

        Returns dict with:
        - transactions: list of transaction objects
        """
        # Check cache first
        cached = self._get_cache(f"tick_tx_{tick_number}")
        if cached:
            return cached

        data = self._make_request(f"/v1/ticks/{tick_number}/transactions")

    def get_approved_transactions(self, tick_number: int) -> Optional[Dict]:
        """
        GET /v2/ticks/{tickNumber}/approved-transactions
        Get only approved transactions for a specific tick.
        """
        data = self._make_request(
            f"/v2/ticks/{tick_number}/approved-transactions")
        return data

    def get_tick_chain_hash(self, tick_number: int) -> Optional[Dict]:
        """
        GET /v2/ticks/{tickNumber}/chain-hash
        Get chain hash for a specific tick.
        """
        data = self._make_request(f"/v2/ticks/{tick_number}/chain-hash")
        return data

    def get_tick_quorum_data(self, tick_number: int) -> Optional[Dict]:
        """
        GET /v2/ticks/{tickNumber}/quorum-data
        Get quorum data for a specific tick.
        """
        data = self._make_request(f"/v2/ticks/{tick_number}/quorum-data")
        return data

    def get_tick_store_hash(self, tick_number: int) -> Optional[Dict]:
        """
        GET /v2/ticks/{tickNumber}/store-hash
        Get store hash for a specific tick.
        """
        data = self._make_request(f"/v2/ticks/{tick_number}/store-hash")
        return data

    # ============================================================================
    # Smart Contract Operations
    # ============================================================================

    def query_smart_contract(self, contract_index: int, input_type: int,
                             input_size: int, request_data: str) -> Optional[Dict]:
        """
        POST /v1/querySmartContract (camelCase)
        Execute read-only contract functions.

        Args:
            contract_index: Contract identifier (e.g., 1 for QX)
            input_type: Function/procedure type identifier
            input_size: Size of input data in bytes
            request_data: Base64-encoded payload

        Response:
        - responseData: Base64-encoded response (needs decoding)
        """
        payload = {
            "contractIndex": contract_index,
            "inputType": input_type,
            "inputSize": input_size,
            "requestData": request_data
        }
        data = self._make_request(
            "/v1/querySmartContract", method="POST", json_data=payload)
        return data

    def broadcast_transaction(self, encoded_transaction: str) -> Optional[Dict]:
        """
        POST /v1/broadcast-transaction
        Submit signed transaction to the network.

        Args:
            encoded_transaction: Base64-encoded signed transaction

        Response:
        - Transaction ID or error information
        """
        payload = {
            "encodedTransaction": encoded_transaction
        }
        data = self._make_request(
            "/v1/broadcast-transaction", method="POST", json_data=payload)
        return data

    # ============================================================================
    # Helper Methods for SmartGuard Integration
    # ============================================================================

    def get_network_statistics(self) -> Dict:
        """
        Get comprehensive network statistics for SmartGuard dashboard.
        Combines multiple endpoints for complete picture.
        """
        status = self.get_status()
        tick_info = self.get_tick_info()

        if not status or not tick_info:
            return {
                "status": "error",
                "error": "Failed to fetch network data"
            }

        return {
            "status": "success",
            "current_tick": tick_info.get("tick", 0),
            "epoch": tick_info.get("epoch", 0),
            "tick_duration": tick_info.get("duration", 0),
            "aligned_votes": tick_info.get("numberOfAlignedVotes", 0),
            "misaligned_votes": tick_info.get("numberOfMisalignedVotes", 0),
            "last_processed_tick": status.get("lastProcessedTick", {}).get("tickNumber", 0),
            "timestamp": datetime.now().isoformat(),
            "source": "live_qubic_rpc"
        }

    def get_recent_transaction_activity(self, num_ticks: int = 5) -> List[Dict]:
        """
        Get recent transaction activity across multiple ticks.
        Useful for activity feed in SmartGuard.
        """
        activities = []
        tick_info = self.get_tick_info()

        if not tick_info:
            return activities

        current_tick = tick_info.get("tick", 0)

        for offset in range(num_ticks):
            tick_num = current_tick - offset
            if tick_num <= 0:
                break

            tx_data = self.get_tick_transactions(tick_num)
            if tx_data and "transactions" in tx_data:
                tx_count = len(tx_data["transactions"])
                if tx_count > 0:
                    activities.append({
                        "tick": tick_num,
                        "transaction_count": tx_count,
                        "timestamp": datetime.now().isoformat(),
                        "message": f"{tx_count} transaction(s) in tick {tick_num}",
                        "is_real": True
                    })

        return activities

    def is_connected(self) -> bool:
        """Check if RPC endpoint is accessible"""
        try:
            status = self.get_status()
            return status is not None
        except:
            return False


# Singleton instance
_client_instance = None


def get_qubic_rpc_client() -> QubicRPCClient:
    """Get or create singleton RPC client instance"""
    global _client_instance
    if _client_instance is None:
        _client_instance = QubicRPCClient()
    return _client_instance

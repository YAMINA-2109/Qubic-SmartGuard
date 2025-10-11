"""
Real Qubic Network Data Fetcher
Replaces AI-generated fake data with actual blockchain queries
"""

import os
import time
from datetime import datetime
from typing import Dict, List, Optional

import requests


class RealQubicDataFetcher:
    """
    Fetches REAL data from Qubic blockchain instead of generating fake data.
    Configure with environment variables for RPC endpoints.
    """

    def __init__(self):
        # Load from environment variables
        self.rpc_endpoint = os.getenv("QUBIC_RPC_ENDPOINT", "")
        self.api_key = os.getenv("QUBIC_API_KEY", "")
        self.explorer_api = os.getenv("QUBIC_EXPLORER_API", "")
        self.archive_api = os.getenv("QUBIC_ARCHIVE_API", "")

        # Check if real endpoints are configured
        self.is_real_mode = bool(self.rpc_endpoint or self.explorer_api)

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

    def _make_request(self, url: str, params: dict = None) -> Optional[dict]:
        """Make HTTP request to Qubic API"""
        try:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            response = requests.get(
                url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ API Error: {e}")
            return None

    def get_network_status(self) -> Dict:
        """
        Get REAL network status from Qubic blockchain
        Returns actual holder count, market cap, etc.
        """
        cached = self._get_cached("network_status")
        if cached:
            return cached

        if not self.is_real_mode:
            return {
                "status": "demo_mode",
                "total_holders": 0,
                "market_cap": 0,
                "participation_rate": 0,
                "active_proposals": 0,
                "error": "No RPC endpoint configured. Set QUBIC_RPC_ENDPOINT or QUBIC_EXPLORER_API in .env"
            }

        # Try to get real data from explorer API
        if self.explorer_api:
            try:
                # Example endpoint (adjust based on actual Qubic API)
                data = self._make_request(
                    f"{self.explorer_api}/network/status")
                if data:
                    result = {
                        "status": "real_data",
                        "total_holders": data.get("totalHolders", 0),
                        "market_cap": data.get("marketCap", 0),
                        "participation_rate": data.get("participationRate", 0),
                        "active_proposals": data.get("activeProposals", 0),
                        "timestamp": datetime.now().isoformat()
                    }
                    self._set_cache("network_status", result)
                    return result
            except Exception as e:
                print(f"Error fetching network status: {e}")

        return {
            "status": "error",
            "error": "Failed to fetch real network data",
            "total_holders": 0,
            "market_cap": 0
        }

    def get_burn_transactions(self) -> Dict:
        """
        Get REAL burn transaction data from Qubic blockchain
        """
        cached = self._get_cached("burn_transactions")
        if cached:
            return cached

        if not self.is_real_mode:
            return {
                "status": "demo_mode",
                "total_burns": 0,
                "total_qubic": 0,
                "error": "Configure QUBIC_RPC_ENDPOINT or QUBIC_ARCHIVE_API for real data"
            }

        # Try archive API for burn transactions
        if self.archive_api:
            try:
                data = self._make_request(
                    f"{self.archive_api}/transactions/burns")
                if data:
                    result = {
                        "status": "real_data",
                        "total_burns": data.get("totalBurns", 0),
                        "total_qubic": data.get("totalBurned", 0),
                        "latest_burn": data.get("latestBurn", "Unknown"),
                        "average_burn": data.get("averageBurn", 0),
                        "burns_today": data.get("burnsToday", 0),
                        "qubic_today": data.get("burnedToday", 0),
                        "timestamp": datetime.now().isoformat()
                    }
                    self._set_cache("burn_transactions", result)
                    return result
            except Exception as e:
                print(f"Error fetching burn data: {e}")

        return {
            "status": "error",
            "error": "Failed to fetch burn transaction data",
            "total_burns": 0
        }

    def get_high_value_transactions(self, min_amount: int = 1000000) -> Dict:
        """
        Get REAL high-value transaction data from Qubic blockchain
        """
        cached = self._get_cached(f"high_value_{min_amount}")
        if cached:
            return cached

        if not self.is_real_mode:
            return {
                "status": "demo_mode",
                "count": 0,
                "error": "Configure QUBIC_RPC_ENDPOINT for real transaction queries"
            }

        # Try RPC endpoint for transaction queries
        if self.rpc_endpoint:
            try:
                params = {"minAmount": min_amount, "limit": 100}
                data = self._make_request(
                    f"{self.rpc_endpoint}/transactions", params)
                if data:
                    transactions = data.get("transactions", [])
                    total_value = sum(tx.get("amount", 0)
                                      for tx in transactions)

                    result = {
                        "status": "real_data",
                        "count": len(transactions),
                        "largest": max((tx.get("amount", 0) for tx in transactions), default=0),
                        "total_value": total_value,
                        "average": total_value // len(transactions) if transactions else 0,
                        "timestamp": datetime.now().isoformat()
                    }
                    self._set_cache(f"high_value_{min_amount}", result)
                    return result
            except Exception as e:
                print(f"Error fetching high-value transactions: {e}")

        return {
            "status": "error",
            "error": "Failed to fetch transaction data",
            "count": 0
        }

    def get_recent_activities(self, limit: int = 10) -> List[Dict]:
        """
        Get REAL recent blockchain activities
        This should query actual events from your database or blockchain
        """
        if not self.is_real_mode:
            return [{
                "type": "info",
                "message": "⚠️ Demo Mode - Configure real data sources",
                "timestamp": datetime.now().isoformat(),
                "is_demo": True
            }]

        # TODO: Implement real activity tracking from database
        # For now, return empty list indicating real mode is enabled but needs DB
        return [{
            "type": "info",
            "message": "📡 Connected to Qubic network - Waiting for activity data",
            "timestamp": datetime.now().isoformat(),
            "is_real": True
        }]

    def is_configured(self) -> bool:
        """Check if real data sources are configured"""
        return self.is_real_mode

    def get_configuration_status(self) -> Dict:
        """Get detailed configuration status"""
        return {
            "rpc_endpoint": "✅ Configured" if self.rpc_endpoint else "❌ Not set",
            "explorer_api": "✅ Configured" if self.explorer_api else "❌ Not set",
            "archive_api": "✅ Configured" if self.archive_api else "❌ Not set",
            "api_key": "✅ Set" if self.api_key else "ℹ️  Optional",
            "mode": "🟢 Real Data" if self.is_real_mode else "🔴 Demo Mode",
            "cache_enabled": True,
            "cache_timeout": f"{self._cache_timeout}s"
        }


# Singleton instance
_fetcher_instance = None


def get_real_data_fetcher() -> RealQubicDataFetcher:
    """Get or create singleton fetcher instance"""
    global _fetcher_instance
    if _fetcher_instance is None:
        _fetcher_instance = RealQubicDataFetcher()
    return _fetcher_instance

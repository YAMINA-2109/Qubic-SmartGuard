#!/usr/bin/env python3
"""
🚀 Production Health Check for Qubic SmartGuard
Comprehensive health monitoring for production deployment
"""

import json
import sys
import time
from datetime import datetime
from typing import Any, Dict

import requests

from real_qubic_rpc_client import RealQubicRPCClient


class ProductionHealthChecker:
    """Production-grade health checker for SmartGuard platform"""

    def __init__(self, base_url: str = "http://localhost:8501"):
        self.base_url = base_url
        self.rpc_client = RealQubicRPCClient()
        self.health_report = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "unknown",
            "checks": {},
            "metrics": {},
            "errors": []
        }

    def check_application_health(self) -> bool:
        """Check if the Streamlit application is responding"""
        try:
            response = requests.get(
                f"{self.base_url}/_stcore/health", timeout=10)
            self.health_report["checks"]["application"] = {
                "status": "healthy" if response.status_code == 200 else "unhealthy",
                "response_time_ms": response.elapsed.total_seconds() * 1000,
                "status_code": response.status_code
            }
            return response.status_code == 200
        except Exception as e:
            self.health_report["checks"]["application"] = {
                "status": "unhealthy",
                "error": str(e)
            }
            self.health_report["errors"].append(
                f"Application check failed: {e}")
            return False

    def check_qubic_connectivity(self) -> bool:
        """Check connectivity to Qubic RPC endpoints"""
        try:
            start_time = time.time()
            result = self.rpc_client.get_verified_network_data()
            end_time = time.time()

            if result["success"]:
                self.health_report["checks"]["qubic_rpc"] = {
                    "status": "healthy",
                    "response_time_ms": (end_time - start_time) * 1000,
                    "endpoint": result["endpoint"],
                    "current_tick": result["network_data"]["current_tick"],
                    "market_cap": result["network_data"]["market_cap"]
                }

                # Store key metrics
                self.health_report["metrics"]["current_tick"] = result["network_data"]["current_tick"]
                self.health_report["metrics"]["market_cap"] = result["network_data"]["market_cap"]
                self.health_report["metrics"]["active_addresses"] = result["network_data"]["active_addresses"]
                self.health_report["metrics"]["tick_quality"] = result["network_data"]["tick_quality"]

                return True
            else:
                self.health_report["checks"]["qubic_rpc"] = {
                    "status": "unhealthy",
                    "error": result.get("error", "Unknown error")
                }
                self.health_report["errors"].append(
                    f"Qubic RPC check failed: {result.get('error')}")
                return False

        except Exception as e:
            self.health_report["checks"]["qubic_rpc"] = {
                "status": "unhealthy",
                "error": str(e)
            }
            self.health_report["errors"].append(
                f"Qubic connectivity check failed: {e}")
            return False

    def check_network_health(self) -> bool:
        """Check overall network health metrics"""
        try:
            health_status = self.rpc_client.get_network_health_status()

            if health_status["status"] != "unhealthy":
                self.health_report["checks"]["network_health"] = {
                    "status": "healthy",
                    "health_score": health_status["health_score"],
                    "overall_status": health_status["status"],
                    "indicators": len(health_status["indicators"])
                }

                # Store health metrics
                self.health_report["metrics"]["health_score"] = health_status["health_score"]
                self.health_report["metrics"]["network_status"] = health_status["status"]

                return True
            else:
                self.health_report["checks"]["network_health"] = {
                    "status": "unhealthy",
                    "error": health_status.get("error", "Network unhealthy")
                }
                self.health_report["errors"].append(
                    f"Network health check failed: {health_status.get('error')}")
                return False

        except Exception as e:
            self.health_report["checks"]["network_health"] = {
                "status": "unhealthy",
                "error": str(e)
            }
            self.health_report["errors"].append(
                f"Network health check failed: {e}")
            return False

    def check_external_dependencies(self) -> bool:
        """Check external dependencies and services"""
        dependencies_healthy = True

        # Check Qubic RPC endpoint directly
        try:
            response = requests.get(
                "https://rpc.qubic.org/v1/latest-stats", timeout=15)
            self.health_report["checks"]["qubic_endpoint"] = {
                "status": "healthy" if response.status_code == 200 else "unhealthy",
                "response_time_ms": response.elapsed.total_seconds() * 1000,
                "status_code": response.status_code
            }
            if response.status_code != 200:
                dependencies_healthy = False

        except Exception as e:
            self.health_report["checks"]["qubic_endpoint"] = {
                "status": "unhealthy",
                "error": str(e)
            }
            self.health_report["errors"].append(
                f"Qubic endpoint check failed: {e}")
            dependencies_healthy = False

        return dependencies_healthy

    def run_comprehensive_check(self) -> Dict[str, Any]:
        """Run all health checks and return comprehensive report"""
        print("🏥 Running Production Health Check...")
        print("=" * 50)

        # Run all checks
        checks = [
            ("Application Health", self.check_application_health),
            ("Qubic Connectivity", self.check_qubic_connectivity),
            ("Network Health", self.check_network_health),
            ("External Dependencies", self.check_external_dependencies)
        ]

        passed_checks = 0
        total_checks = len(checks)

        for check_name, check_function in checks:
            print(f"🔍 Checking {check_name}...", end=" ")
            try:
                if check_function():
                    print("✅ PASS")
                    passed_checks += 1
                else:
                    print("❌ FAIL")
            except Exception as e:
                print(f"❌ ERROR: {e}")
                self.health_report["errors"].append(
                    f"{check_name} failed with error: {e}")

        # Calculate overall status
        health_percentage = (passed_checks / total_checks) * 100

        if health_percentage == 100:
            self.health_report["overall_status"] = "healthy"
            status_emoji = "✅"
        elif health_percentage >= 75:
            self.health_report["overall_status"] = "degraded"
            status_emoji = "⚠️"
        else:
            self.health_report["overall_status"] = "unhealthy"
            status_emoji = "❌"

        self.health_report["health_percentage"] = health_percentage
        self.health_report["checks_passed"] = passed_checks
        self.health_report["total_checks"] = total_checks

        print("\n" + "=" * 50)
        print("📊 HEALTH CHECK RESULTS")
        print("=" * 50)
        print(
            f"{status_emoji} Overall Status: {self.health_report['overall_status'].upper()}")
        print(
            f"📈 Health Score: {health_percentage:.1f}% ({passed_checks}/{total_checks} checks passed)")

        if self.health_report["metrics"]:
            print("\n📊 Live Metrics:")
            metrics = self.health_report["metrics"]
            if "current_tick" in metrics:
                print(f"   🎯 Current Tick: {metrics['current_tick']:,}")
            if "market_cap" in metrics:
                print(f"   💰 Market Cap: ${metrics['market_cap']:,.0f}")
            if "health_score" in metrics:
                print(f"   🏥 Network Health: {metrics['health_score']}/100")

        if self.health_report["errors"]:
            print(f"\n❌ Errors ({len(self.health_report['errors'])}):")
            for error in self.health_report["errors"]:
                print(f"   • {error}")

        print("=" * 50)

        return self.health_report


def main():
    """Main health check function"""
    import argparse

    parser = argparse.ArgumentParser(
        description="SmartGuard Production Health Check")
    parser.add_argument(
        "--url", default="http://localhost:8501", help="Base URL to check")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON format")
    parser.add_argument("--exit-code", action="store_true",
                        help="Exit with error code on failure")

    args = parser.parse_args()

    checker = ProductionHealthChecker(args.url)
    report = checker.run_comprehensive_check()

    if args.json:
        print(json.dumps(report, indent=2))

    # Exit with appropriate code
    if args.exit_code:
        if report["overall_status"] == "healthy":
            sys.exit(0)
        elif report["overall_status"] == "degraded":
            sys.exit(1)
        else:
            sys.exit(2)


if __name__ == "__main__":
    main()

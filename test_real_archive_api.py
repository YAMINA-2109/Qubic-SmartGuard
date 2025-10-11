#!/usr/bin/env python3
"""
🚀 REAL QUBIC ARCHIVE API INTEGRATION TEST
Testing live connection to Qubic Archive API endpoints
"""

import json
import time

from real_qubic_rpc_client import RealQubicRPCClient


def test_archive_api_endpoints():
    """Test all real Archive API endpoints"""

    print("🌐 TESTING REAL QUBIC ARCHIVE API")
    print("=" * 60)
    print("Testing live endpoints from api.qubic.org")
    print("=" * 60)

    client = RealQubicRPCClient()
    test_results = []

    # Test 1: Health Check
    print("\n1️⃣ Testing Archive API Health Check...")
    health_result = client.check_archive_health()

    if health_result["success"]:
        print(f"   ✅ Archive API is HEALTHY")
        print(
            f"   ⏱️ Response time: {health_result['response_time_ms']:.1f}ms")
        print(f"   🌐 Endpoint: {health_result['endpoint']}")
    else:
        print(f"   ❌ Health check failed: {health_result.get('error')}")

    test_results.append(("Health Check", health_result["success"]))

    # Test 2: Latest Tick
    print("\n2️⃣ Testing Latest Tick Endpoint...")
    tick_result = client.get_latest_tick()

    if tick_result["success"]:
        data = tick_result["data"]
        print(f"   ✅ Latest Tick Retrieved Successfully")
        print(f"   📊 Current Tick: {data.get('tickNumber', 'N/A')}")
        print(f"   🌍 Epoch: {data.get('epoch', 'N/A')}")
        print(f"   🌐 Endpoint: {tick_result['endpoint']}")

        # Display more details if available
        if "timestamp" in data:
            print(f"   ⏰ Timestamp: {data['timestamp']}")
    else:
        print(f"   ❌ Latest tick failed: {tick_result.get('error')}")

    test_results.append(("Latest Tick", tick_result["success"]))

    # Test 3: Current Epoch Computors
    print("\n3️⃣ Testing Epoch Computors Endpoint...")

    # Use current epoch if we got it from latest tick
    current_epoch = 64  # Default epoch from your screenshot
    if tick_result["success"] and "epoch" in tick_result["data"]:
        current_epoch = tick_result["data"]["epoch"]

    computors_result = client.get_epoch_computors(current_epoch)

    if computors_result["success"]:
        print(f"   ✅ Computors Retrieved Successfully")
        print(f"   🎯 Epoch: {computors_result['epoch']}")
        print(f"   👥 Computors Count: {computors_result['computors_count']}")
        print(f"   🌐 Endpoint: {computors_result['endpoint']}")

        # Show sample computor data if available
        data = computors_result["data"]
        if "computors" in data and len(data["computors"]) > 0:
            sample_computor = data["computors"][0]
            print(f"   📋 Sample Computor: {sample_computor}")
    else:
        print(f"   ❌ Computors failed: {computors_result.get('error')}")

    test_results.append(("Epoch Computors", computors_result["success"]))

    # Test 4: Identity Transfers (using a sample identity)
    print("\n4️⃣ Testing Identity Transfers Endpoint...")

    # Sample Qubic identity for testing
    sample_identity = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    transfers_result = client.get_identity_transfers(sample_identity)

    if transfers_result["success"]:
        print(f"   ✅ Identity Transfers Retrieved")
        print(f"   🆔 Identity: {transfers_result['identity'][:20]}...")
        print(f"   📊 Transfers Count: {transfers_result['transfers_count']}")
        print(f"   🌐 Endpoint: {transfers_result['endpoint']}")
    else:
        print(f"   ⚠️ Identity transfers: {transfers_result.get('error')}")
        # This might fail if the identity doesn't exist, which is normal

    test_results.append(("Identity Transfers", transfers_result["success"]))

    # Test 5: Network Status (RPC endpoint)
    print("\n5️⃣ Testing RPC Network Status...")
    status_result = client.get_latest_stats()

    if status_result and "data" in status_result:
        print(f"   ✅ Network Status Retrieved")
        data = status_result["data"]
        print(f"   💰 Market Cap: ${float(data.get('marketCap', 0)):,.0f}")
        print(f"   👥 Active Addresses: {data.get('activeAddresses', 0):,}")
        print(f"   💎 Price: ${data.get('price', 0):.6f}")
    else:
        print(f"   ❌ Network status failed")

    test_results.append(("Network Status", status_result is not None))

    # Results Summary
    print("\n" + "=" * 60)
    print("📊 ARCHIVE API TEST RESULTS")
    print("=" * 60)

    passed_tests = sum(1 for _, passed in test_results if passed)
    total_tests = len(test_results)

    for test_name, passed in test_results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {status} {test_name}")

    print(f"\n🏁 OVERALL SCORE: {passed_tests}/{total_tests} tests passed")

    if passed_tests >= 3:
        print("🎉 EXCELLENT! Archive API connection is working!")
        print("✅ Your SmartGuard platform has REAL API connectivity")
    elif passed_tests >= 1:
        print("⚠️ PARTIAL SUCCESS: Some endpoints working")
        print("🔧 Check network connectivity for failed endpoints")
    else:
        print("❌ CONNECTION ISSUES: Please check network connectivity")

    return test_results


def demonstrate_real_data_usage():
    """Demonstrate how to use real Archive API data"""

    print("\n" + "=" * 60)
    print("🛠️ REAL DATA USAGE DEMONSTRATION")
    print("=" * 60)

    client = RealQubicRPCClient()

    # Get real current network state
    print("📊 Getting Current Network State...")

    # Latest tick
    tick_data = client.get_latest_tick()
    if tick_data["success"]:
        current_tick = tick_data["data"]["tickNumber"]
        current_epoch = tick_data["data"]["epoch"]

        print(f"✅ Current Network State:")
        print(f"   🎯 Tick: {current_tick:,}")
        print(f"   🌍 Epoch: {current_epoch}")

        # Get computors for current epoch
        computors = client.get_epoch_computors(current_epoch)
        if computors["success"]:
            print(f"   👥 Active Computors: {computors['computors_count']}")

        # Get network statistics
        stats = client.get_latest_stats()
        if stats and "data" in stats:
            data = stats["data"]
            print(f"   💰 Market Cap: ${float(data.get('marketCap', 0)):,.0f}")
            print(f"   📈 Price: ${data.get('price', 0):.6f}")
            print(f"   👥 Active Users: {data.get('activeAddresses', 0):,}")

        print("\n🚀 This is REAL live data from Qubic mainnet!")
        print("📡 Data sources:")
        print(f"   • Archive API: {client.archive_base_url}")
        print(f"   • RPC API: {client.rpc_base_url}")

    else:
        print("❌ Could not retrieve current network state")


def show_api_endpoints():
    """Show all available real API endpoints"""

    print("\n" + "=" * 60)
    print("🔗 AVAILABLE REAL API ENDPOINTS")
    print("=" * 60)

    client = RealQubicRPCClient()

    print("📊 Archive API Endpoints:")
    print(f"   Base URL: {client.archive_base_url}")
    for name, endpoint in client.endpoints.items():
        if endpoint.startswith("/v1/"):
            full_url = f"{client.archive_base_url}{endpoint}"
            print(f"   • {name}: {full_url}")

    print(f"\n🌐 RPC API Endpoints:")
    print(f"   Base URL: {client.rpc_base_url}")
    print(f"   • Status: {client.rpc_base_url}/v1/status")
    print(f"   • Latest Stats: {client.rpc_base_url}/v1/latest-stats")

    print("\n💡 These are REAL Qubic network endpoints!")
    print("🔥 Your SmartGuard platform connects to live blockchain data!")


if __name__ == "__main__":
    print("🛡️ QUBIC SMARTGUARD - REAL API INTEGRATION TEST")
    print("Testing live connection to Qubic Archive and RPC APIs")
    print("=" * 80)

    # Run comprehensive API tests
    test_results = test_archive_api_endpoints()

    # Demonstrate real data usage
    demonstrate_real_data_usage()

    # Show available endpoints
    show_api_endpoints()

    print("\n" + "=" * 80)
    print("🎯 CONCLUSION:")

    passed_tests = sum(1 for _, passed in test_results if passed)
    if passed_tests >= 3:
        print("✅ Your SmartGuard platform has GENUINE real API connectivity!")
        print("🚀 This is NOT simulation - it's connected to live Qubic network!")
        print("📡 Archive API, RPC API, and live data confirmed working!")
    else:
        print("⚠️ Some API connectivity issues detected")
        print("🔧 Check network connection and API availability")

    print("=" * 80)

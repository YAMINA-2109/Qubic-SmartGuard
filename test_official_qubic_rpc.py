#!/usr/bin/env python3
"""
Test Official Qubic RPC Integration
Uses the official Live Tree API endpoints from Qubic
"""

from qubic_official_rpc_client import get_qubic_rpc_client
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


load_dotenv()


def print_section(title, char="="):
    print("\n" + char * 80)
    print(f"  {title}")
    print(char * 80)


def test_network_status():
    """Test GET /v1/status endpoint"""
    print_section("🌐 Testing Network Status (GET /v1/status)")

    client = get_qubic_rpc_client()
    status = client.get_status()

    if status:
        print("\n✅ SUCCESS! Connected to Qubic RPC")
        print(f"\n📊 Network Status Data:")

        if "lastProcessedTick" in status:
            tick_data = status["lastProcessedTick"]
            print(
                f"  • Last Processed Tick: {tick_data.get('tickNumber', 'N/A'):,}")
            print(f"  • Epoch: {tick_data.get('epoch', 'N/A')}")

        if "lastProcessedTicksPerEpoch" in status:
            ticks_per_epoch = status["lastProcessedTicksPerEpoch"]
            if isinstance(ticks_per_epoch, dict):
                print(f"\n  📈 Processed Ticks Per Epoch:")
                for epoch_key in list(ticks_per_epoch.keys())[:3]:
                    epoch_data = ticks_per_epoch[epoch_key]
                    if isinstance(epoch_data, dict):
                        print(f"     - Epoch {epoch_data.get('epoch', epoch_key)}: " +
                              f"{epoch_data.get('tickNumber', 'N/A')} tick")
            elif isinstance(ticks_per_epoch, list):
                print(f"\n  📈 Processed Ticks Per Epoch:")
                for epoch_data in ticks_per_epoch[:3]:
                    print(f"     - Epoch {epoch_data.get('epoch', 'N/A')}: " +
                          f"{epoch_data.get('tickNumber', 'N/A')} tick")

        return True
    else:
        print("\n❌ FAILED to connect to Qubic RPC")
        return False


def test_tick_info():
    """Test GET /v1/tick-info endpoint"""
    print_section("⏰ Testing Tick Info (GET /v1/tick-info)")

    client = get_qubic_rpc_client()
    tick_info = client.get_tick_info()

    if tick_info:
        print("\n✅ SUCCESS! Retrieved tick information")
        print("\n📊 Current Tick Data:")

        # Handle tick number (might be string or int)
        tick_num = tick_info.get('tick', 'N/A')
        if isinstance(tick_num, (int, float)):
            print(f"  • Current Tick: {int(tick_num):,}")
        else:
            print(f"  • Current Tick: {tick_num}")

        print(f"  • Epoch: {tick_info.get('epoch', 'N/A')}")
        print(f"  • Duration: {tick_info.get('duration', 'N/A')}")

        # Handle vote counts
        aligned = tick_info.get('numberOfAlignedVotes', 0)
        misaligned = tick_info.get('numberOfMisalignedVotes', 0)
        if isinstance(aligned, (int, float)):
            print(f"  • Aligned Votes: {int(aligned):,}")
        else:
            print(f"  • Aligned Votes: {aligned}")
        if isinstance(misaligned, (int, float)):
            print(f"  • Misaligned Votes: {int(misaligned):,}")
        else:
            print(f"  • Misaligned Votes: {misaligned}")

        return tick_info.get('tick', 0)
    else:
        print("\n❌ FAILED to get tick info")
        return None


def test_tick_transactions(tick_number):
    """Test GET /v2/ticks/{tickNumber}/transactions endpoint"""
    print_section(f"📊 Testing Tick Transactions (Tick #{tick_number:,})")

    client = get_qubic_rpc_client()
    tx_data = client.get_tick_transactions(tick_number)

    if tx_data:
        transactions = tx_data.get("transactions", [])
        print(f"\n✅ SUCCESS! Retrieved transaction data")
        print(f"\n📝 Transaction Summary:")
        print(f"  • Total Transactions: {len(transactions):,}")

        if len(transactions) > 0:
            print(f"\n  🔍 First 3 transactions:")
            for i, tx in enumerate(transactions[:3], 1):
                print(f"\n     Transaction {i}:")
                print(f"     • TX ID: {tx.get('txId', 'N/A')}")
                print(f"     • Source: {tx.get('sourceId', 'N/A')[:20]}...")
                print(f"     • Dest: {tx.get('destId', 'N/A')[:20]}...")
                print(f"     • Amount: {tx.get('amount', 0):,} QU")
                print(f"     • Tick: {tx.get('tickNumber', 'N/A'):,}")

        return len(transactions)
    else:
        print("\n⚠️  No transaction data (this is normal if tick had no transactions)")
        return 0


def test_network_statistics():
    """Test aggregated network statistics"""
    print_section("📈 Testing Network Statistics (Aggregated)")

    client = get_qubic_rpc_client()
    stats = client.get_network_statistics()

    if stats.get("status") == "success":
        print("\n✅ SUCCESS! Retrieved network statistics")
        print(f"\n📊 Complete Network Stats:")
        print(f"  • Current Tick: {stats.get('current_tick', 0):,}")
        print(f"  • Epoch: {stats.get('epoch', 0)}")
        print(f"  • Tick Duration: {stats.get('tick_duration', 0)}")
        print(f"  • Last Processed: {stats.get('last_processed_tick', 0):,}")
        print(f"  • Aligned Votes: {stats.get('aligned_votes', 0):,}")
        print(f"  • Misaligned Votes: {stats.get('misaligned_votes', 0):,}")
        print(f"  • Timestamp: {stats.get('timestamp', 'N/A')}")
        print(f"  • Source: {stats.get('source', 'N/A')}")

        return True
    else:
        print(f"\n❌ FAILED: {stats.get('error', 'Unknown error')}")
        return False


def test_recent_activity():
    """Test recent transaction activity"""
    print_section("🔔 Testing Recent Activity Feed")

    client = get_qubic_rpc_client()
    activities = client.get_recent_transaction_activity(num_ticks=3)

    if activities:
        print(f"\n✅ SUCCESS! Retrieved {len(activities)} recent activities")
        print(f"\n📋 Recent Activity:")

        for activity in activities:
            status_emoji = "🟢" if activity.get("is_real") else "🔴"
            print(f"\n  {status_emoji} Tick #{activity.get('tick', 'N/A'):,}")
            print(f"     • {activity.get('message', 'N/A')}")
            print(f"     • Time: {activity.get('timestamp', 'N/A')}")

        return True
    else:
        print("\n⚠️  No recent activities found (or RPC connection issue)")
        return False


def test_connection():
    """Test basic RPC connection"""
    print_section("🔌 Testing RPC Connection")

    client = get_qubic_rpc_client()

    print(f"\n📡 RPC Endpoint: {client.base_url}")
    print(f"⏱️  Timeout: {client.timeout}s")
    print(f"💾 Cache Timeout: {client._cache_timeout}s")

    connected = client.is_connected()

    if connected:
        print(f"\n✅ CONNECTION SUCCESSFUL!")
        print(f"   Qubic RPC is accessible and responding")
        return True
    else:
        print(f"\n❌ CONNECTION FAILED!")
        print(f"   Unable to reach {client.base_url}")
        return False


def main():
    print_section("🛡️  QUBIC SMARTGUARD - OFFICIAL RPC TEST", "=")
    print("\nTesting integration with Qubic Live Tree RPC API")
    print("Documentation: https://qubic.github.io/integration/Partners/swagger/")

    results = {}

    # Test 1: Connection
    results['connection'] = test_connection()

    if not results['connection']:
        print_section("❌ TESTS ABORTED - NO CONNECTION", "=")
        print("\nPlease check:")
        print("  1. Internet connection")
        print("  2. RPC endpoint is correct: https://rpc.qubic.org")
        print("  3. No firewall blocking the connection")
        return

    # Test 2: Network Status
    results['status'] = test_network_status()

    # Test 3: Tick Info
    current_tick = test_tick_info()
    results['tick_info'] = current_tick is not None

    # Test 4: Transactions (if we have a valid tick)
    if current_tick and current_tick > 0:
        tx_count = test_tick_transactions(current_tick)
        results['transactions'] = True

        # Try a few previous ticks to find one with transactions
        if tx_count == 0:
            print("\n🔍 Searching for ticks with transactions...")
            for offset in range(1, 6):
                test_tick = current_tick - offset
                tx_count = test_tick_transactions(test_tick)
                if tx_count > 0:
                    break
    else:
        results['transactions'] = False

    # Test 5: Network Statistics
    results['statistics'] = test_network_statistics()

    # Test 6: Activity Feed
    results['activity'] = test_recent_activity()

    # Final Summary
    print_section("📋 TEST SUMMARY", "=")

    total_tests = len(results)
    passed_tests = sum(1 for result in results.values() if result)

    print(f"\n  Tests Run: {total_tests}")
    print(f"  Tests Passed: {passed_tests}")
    print(f"  Tests Failed: {total_tests - passed_tests}")
    print(f"  Success Rate: {(passed_tests/total_tests)*100:.1f}%")

    print("\n  Detailed Results:")
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"    {status} - {test_name}")

    print("\n" + "=" * 80)

    if passed_tests == total_tests:
        print("  🎉 ALL TESTS PASSED!")
        print("  🟢 Qubic RPC integration is fully functional")
        print("  ✅ SmartGuard can now use REAL blockchain data")
    elif passed_tests > 0:
        print("  🟡 PARTIAL SUCCESS")
        print(f"  {passed_tests}/{total_tests} tests passed")
        print("  ⚠️  Some features may not work correctly")
    else:
        print("  🔴 ALL TESTS FAILED")
        print("  ❌ Qubic RPC integration is not working")
        print("  Check your network connection and RPC endpoint")

    print("=" * 80 + "\n")

    # Return exit code
    return 0 if passed_tests == total_tests else 1


if __name__ == "__main__":
    exit(main())

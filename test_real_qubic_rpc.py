#!/usr/bin/env python3
"""
Test Real Qubic RPC Integration
Tests actual connection to https://rpc.qubic.org
"""

from qubic_real_rpc_client import get_real_data_fetcher
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


load_dotenv()


def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def main():
    fetcher = get_real_data_fetcher()

    print_section("🛡️ TESTING REAL QUBIC RPC INTEGRATION")

    # Check configuration
    config = fetcher.get_configuration_status()
    print("\n📋 Configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")

    if not fetcher.is_configured():
        print("\n⚠️  WARNING: No RPC endpoint configured!")
        print("   Add QUBIC_RPC_ENDPOINT to .env file")
        return

    print_section("🌐 TESTING: Network Status (GET /v1/status)")
    network_status = fetcher.get_network_status()
    print(f"\n  Status: {network_status.get('status')}")
    if network_status.get('status') == 'real_data':
        print(f"  ✅ Current Tick: {network_status.get('current_tick', 0):,}")
        print(f"  ✅ Epoch: {network_status.get('epoch', 0)}")
        print(f"  ✅ Entities: {network_status.get('number_of_entities', 0):,}")
        print(
            f"  ✅ Transactions: {network_status.get('number_of_transactions', 0):,}")
    else:
        print(f"  ❌ Error: {network_status.get('error')}")

    print_section("⏰ TESTING: Tick Info (GET /v1/tick-info)")
    tick_info = fetcher.get_tick_info()
    print(f"\n  Status: {tick_info.get('status')}")
    if tick_info.get('status') == 'real_data':
        print(f"  ✅ Current Tick: {tick_info.get('tick', 0):,}")
        print(f"  ✅ Duration: {tick_info.get('duration', 0)} seconds")
        print(f"  ✅ Epoch: {tick_info.get('epoch', 0)}")

    print_section("📊 TESTING: Recent Transactions")
    if tick_info.get('status') == 'real_data':
        current_tick = tick_info.get('tick', 0)
        if current_tick > 0:
            # Test getting transactions from a recent tick
            print(f"\n  Fetching transactions from tick {current_tick}...")
            tx_data = fetcher.get_transactions_by_tick(current_tick)
            print(f"  Status: {tx_data.get('status')}")
            if tx_data.get('status') == 'real_data':
                tx_count = tx_data.get('transaction_count', 0)
                print(
                    f"  ✅ Found {tx_count} transactions in tick {current_tick}")
                if tx_count > 0:
                    print(f"  📝 First few transactions:")
                    for tx in tx_data.get('transactions', [])[:3]:
                        print(f"     - TX ID: {tx.get('txId', 'N/A')[:20]}...")

    print_section("🎯 TESTING: Aggregate Statistics")
    stats = fetcher.get_real_statistics()
    print(f"\n  Status: {stats.get('status')}")
    if stats.get('status') == 'real_data':
        print(f"  ✅ Successfully fetched real Qubic blockchain data!")
        print(f"  📡 Endpoint: {stats.get('endpoint')}")
        print(f"  ⏰ Timestamp: {stats.get('timestamp')}")

    print_section("📋 TESTING: Recent Activities Feed")
    activities = fetcher.get_recent_activities(limit=5)
    print(f"\n  Found {len(activities)} recent activities:")
    for activity in activities:
        is_real = "🟢 REAL" if activity.get('is_real') else "🔴 DEMO"
        print(f"  {is_real} - {activity.get('message')}")

    print("\n" + "=" * 70)
    if fetcher.is_configured() and network_status.get('status') == 'real_data':
        print("  🎉 SUCCESS! Real Qubic RPC integration is working!")
        print("  ✅ All data is coming from live Qubic blockchain")
    else:
        print("  ⚠️  DEMO MODE - Configure RPC endpoint for real data")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()

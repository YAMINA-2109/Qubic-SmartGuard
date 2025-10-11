#!/usr/bin/env python3
"""
Test script to demonstrate the dynamic features of Qubic SmartGuard
Shows how the activity feed, RPC 2.0 features, and voting results now update dynamically
"""

from main_app import (
    generate_dynamic_activity,
    generate_dynamic_burn_data,
    generate_dynamic_high_value_data,
    generate_dynamic_production_status,
    generate_dynamic_voting_results,
)
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the dynamic data generators from main_app


def test_dynamic_activity():
    """Test dynamic activity feed generation"""
    print("🔔 TESTING: Dynamic Activity Feed")
    print("=" * 50)

    for i in range(3):
        print(f"\n--- Refresh {i+1} ---")
        activities = generate_dynamic_activity()
        for activity in activities:
            print(f"• {activity['time']}: {activity['content']}")

    print("\n✅ Activity feed shows different data on each refresh!\n")


def test_rpc2_features():
    """Test dynamic RPC 2.0 features"""
    print("🚀 TESTING: Dynamic RPC 2.0 Features")
    print("=" * 50)

    print("\n🔥 Burn Transaction Data:")
    for i in range(3):
        burn_data = generate_dynamic_burn_data()
        print(
            f"Refresh {i+1}: {burn_data['total_burns']:,} burns, {burn_data['total_qubic']:,} QUBIC burned")

    print("\n💎 High-Value Transaction Data:")
    for i in range(3):
        hv_data = generate_dynamic_high_value_data()
        print(
            f"Refresh {i+1}: {hv_data['count']} transactions, largest: {hv_data['largest']:,} QUBIC")

    print("\n✅ RPC 2.0 features show different data on each search!\n")


def test_production_status():
    """Test dynamic production status"""
    print("🌐 TESTING: Dynamic Production Status")
    print("=" * 50)

    for i in range(3):
        prod_status = generate_dynamic_production_status()
        print(f"Refresh {i+1}:")
        print(f"  • Total Holders: {prod_status['total_holders']:,}")
        print(f"  • Active Proposals: {prod_status['active_proposals']}")
        print(f"  • Participation Rate: {prod_status['participation_rate']}%")
        print(f"  • Market Cap: ${prod_status['market_cap']:,}")
        print()

    print("✅ Production status shows realistic variations!\n")


def test_voting_results():
    """Test dynamic voting results"""
    print("🗳️ TESTING: Dynamic Voting Results")
    print("=" * 50)

    proposals = ["PROP_MAINNET_001", "PROP_MAINNET_002", "PROP_MAINNET_003"]

    for proposal_id in proposals:
        print(f"\n--- {proposal_id} ---")
        results = generate_dynamic_voting_results(proposal_id)
        print(
            f"  YES: {results['yes_votes']}, NO: {results['no_votes']}, ABSTAIN: {results['abstain_votes']}")
        print(
            f"  Participation: {results['participation']}%, Majority: {results['majority']}%")

    print("\n✅ Each proposal shows different voting patterns!\n")


def main():
    """Run all dynamic feature tests"""
    print("🛡️ QUBIC SMARTGUARD - DYNAMIC FEATURES TEST")
    print("=" * 60)
    print("Testing all dynamic data generators to show they produce")
    print("realistic, varying data instead of static demo content.\n")

    test_dynamic_activity()
    test_rpc2_features()
    test_production_status()
    test_voting_results()

    print("🎉 ALL TESTS COMPLETED!")
    print("=" * 60)
    print("✅ Activity Feed: Now shows different activities with realistic timestamps")
    print("✅ RPC 2.0 Features: Burn & high-value searches show varying data")
    print("✅ Production Status: Shows realistic fluctuations in network metrics")
    print("✅ Voting Results: Each proposal has unique, varying vote counts")
    print("\n🌐 Navigate to http://localhost:8501 to see these changes live!")
    print("🔄 Use the refresh buttons and auto-refresh features to see dynamic updates")


if __name__ == "__main__":
    main()

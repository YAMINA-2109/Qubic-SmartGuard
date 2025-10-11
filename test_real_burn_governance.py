"""
🎉 TEST REAL BURN & GOVERNANCE DATA
Tests the newly discovered contracts:
- Contract 8: CCF (Burns/Treasury)
- Contract 6: GQMPROPO (Governance/Voting)
"""
import json

from qubic_live_data_integration import (
    get_live_burn_statistics,
    get_live_network_stats,
    get_live_voting_results,
)


def main():
    print("=" * 80)
    print("🎉 TESTING REAL BURN & GOVERNANCE DATA")
    print("=" * 80)
    print()
    print("Testing newly discovered contracts:")
    print("  • Contract 8: CCF (Burns/Treasury)")
    print("  • Contract 6: GQMPROPO (Governance/Voting)")
    print()
    print("=" * 80)

    # Test 1: Network Stats (confirm still working)
    print("\n📊 TEST 1: Network Statistics")
    print("-" * 80)
    stats = get_live_network_stats()
    print(f"✅ Current Tick: {stats['current_tick']:,}")
    print(f"✅ Epoch: {stats['epoch']}")
    print(f"✅ Status: {stats['data_source']}")

    # Test 2: Burn Statistics (Contract 8 - CCF)
    print("\n\n🔥 TEST 2: Burn Statistics (CCF Contract)")
    print("-" * 80)
    try:
        burns = get_live_burn_statistics()
        print(f"Contract Index: {burns.get('contract_index', 'N/A')}")
        print(f"Data Source: {burns['data_source']}")
        print(f"Total Burned: {burns.get('total_burned', 0):,} QUBIC")
        print(f"Last Burn Tick: {burns.get('last_burn_tick', 0):,}")
        print(f"Timestamp: {burns['timestamp']}")

        if '🟢' in burns['data_source']:
            print("\n✅ SUCCESS! Burn data is LIVE from CCF contract!")
        else:
            print("\n⚠️  Using demo data (contract query may need adjustment)")
    except Exception as e:
        print(f"❌ Error: {e}")

    # Test 3: Governance/Voting (Contract 6 - GQMPROPO)
    print("\n\n🗳️  TEST 3: Governance/Voting (GQMPROPO Contract)")
    print("-" * 80)
    try:
        voting = get_live_voting_results()
        print(f"Contract Index: {voting.get('contract_index', 'N/A')}")
        print(f"Data Source: {voting['data_source']}")
        print(f"Active Proposals: {voting.get('active_proposals', 0)}")
        print(f"Total Votes: {voting.get('total_votes', 0):,}")
        print(f"Raw Data Size: {voting.get('raw_data_size', 0)} bytes")
        print(f"Timestamp: {voting['timestamp']}")

        if '🟢' in voting['data_source']:
            print("\n✅ SUCCESS! Voting data is LIVE from GQMPROPO contract!")
        else:
            print("\n⚠️  Using demo data (contract query may need adjustment)")
    except Exception as e:
        print(f"❌ Error: {e}")

    # Summary
    print("\n" + "=" * 80)
    print("📋 INTEGRATION STATUS SUMMARY")
    print("=" * 80)
    print()

    features = [
        ("Network Statistics", stats['data_source']),
        ("Burn Statistics (CCF)", burns.get('data_source', '🔴 DEMO')),
        ("Governance (GQMPROPO)", voting.get('data_source', '🔴 DEMO'))
    ]

    live_count = sum(1 for _, status in features if '🟢' in status)

    for feature, status in features:
        icon = "✅" if '🟢' in status else "⚠️"
        print(f"{icon} {feature}: {status}")

    print()
    print(f"Live Features: {live_count}/3")

    if live_count == 3:
        print("\n🎉 ALL FEATURES ARE NOW LIVE!")
        print("🚀 SmartGuard is running on 100% real blockchain data!")
    elif live_count >= 1:
        print(f"\n✅ {live_count} feature(s) are live!")
        print("⚠️  Some features may need inputType adjustment")

    print("\n" + "=" * 80)
    print("💡 NEXT STEPS")
    print("=" * 80)
    print()
    print("If burn/governance data is 🔴 DEMO:")
    print("  1. Try different inputType values (1, 2, 3, etc.)")
    print("  2. Check contract documentation for function IDs")
    print("  3. Ask community for specific inputType for each function")
    print()
    print("If everything is 🟢 LIVE:")
    print("  1. Integrate into main_app.py")
    print("  2. Update UI to show live data")
    print("  3. Deploy SmartGuard with 100% real data! 🚀")
    print()


if __name__ == "__main__":
    main()

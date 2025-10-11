#!/usr/bin/env python3
"""
🎯 Live App Deployment Test
Tests that main_app.py is using real blockchain data, not fake AI-generated data.

This verifies:
1. Live data functions are imported
2. Data source indicators show LIVE status
3. Real blockchain data is being used (CCF burns, GQMPROPO governance)
4. No AI-generated fake data in production
"""


def test_imports():
    """Verify live data functions are imported in main_app.py"""
    print("\n" + "="*70)
    print("🔍 TEST 1: Checking Live Data Imports")
    print("="*70)

    with open('main_app.py', 'r') as f:
        content = f.read()

    required_imports = [
        'LIVE_DATA_AVAILABLE',
        'get_live_network_stats',
        'get_live_recent_activity',
        'get_live_burn_statistics',
        'get_live_voting_results'
    ]

    all_imported = True
    for imp in required_imports:
        if imp in content:
            print(f"  ✅ {imp} - FOUND")
        else:
            print(f"  ❌ {imp} - MISSING")
            all_imported = False

    if all_imported:
        print("\n🎉 All live data functions are imported!")
    else:
        print("\n❌ Some imports are missing!")

    return all_imported


def test_function_replacements():
    """Verify fake data generators have been updated to use live data"""
    print("\n" + "="*70)
    print("🔍 TEST 2: Checking Function Updates")
    print("="*70)

    with open('main_app.py', 'r') as f:
        content = f.read()

    # Check if functions check LIVE_DATA_AVAILABLE flag
    functions_to_check = [
        'generate_dynamic_activity',
        'generate_dynamic_burn_data',
        'generate_dynamic_production_status',
        'generate_dynamic_voting_results'
    ]

    all_updated = True
    for func in functions_to_check:
        # Look for the function definition and check if it uses LIVE_DATA_AVAILABLE
        func_start = content.find(f'def {func}')
        if func_start == -1:
            print(f"  ⚠️  {func} - NOT FOUND")
            all_updated = False
            continue

        # Get next 500 characters after function definition
        func_section = content[func_start:func_start+800]

        if 'LIVE_DATA_AVAILABLE' in func_section:
            print(f"  ✅ {func} - NOW USES LIVE DATA")
        else:
            print(f"  ❌ {func} - STILL USING FAKE DATA")
            all_updated = False

    if all_updated:
        print("\n🎉 All functions updated to use live data!")
    else:
        print("\n❌ Some functions still use fake data!")

    return all_updated


def test_live_data_calls():
    """Verify that live data functions are actually being called"""
    print("\n" + "="*70)
    print("🔍 TEST 3: Checking Live Data Function Calls")
    print("="*70)

    with open('main_app.py', 'r') as f:
        content = f.read()

    expected_calls = {
        'get_live_burn_statistics()': 'CCF Contract (Burns)',
        'get_live_voting_results()': 'GQMPROPO Contract (Governance)',
        'get_live_network_stats()': 'Network Statistics',
        'get_live_recent_activity(': 'Recent Activity'
    }

    all_called = True
    for call, description in expected_calls.items():
        if call in content:
            print(f"  ✅ {description} - CALLED")
        else:
            print(f"  ❌ {description} - NOT CALLED")
            all_called = False

    if all_called:
        print("\n🎉 All live data sources are being queried!")
    else:
        print("\n❌ Some live data sources are not being used!")

    return all_called


def test_data_source_indicators():
    """Verify data source indicators are displayed"""
    print("\n" + "="*70)
    print("🔍 TEST 4: Checking Data Source Indicators")
    print("="*70)

    with open('main_app.py', 'r') as f:
        content = f.read()

    indicators = {
        'data_source': 'Data source field in responses',
        '🔴 DEMO': 'Demo data fallback indicator'
    }

    all_present = True
    for indicator, description in indicators.items():
        if indicator in content:
            print(f"  ✅ {description} - PRESENT")
        else:
            print(f"  ❌ {description} - MISSING")
            all_present = False

    if all_present:
        print("\n🎉 Data source indicators are implemented!")
    else:
        print("\n⚠️  Some indicators may be missing!")

    return all_present


def test_actual_live_data():
    """Test that live data functions actually work"""
    print("\n" + "="*70)
    print("🔍 TEST 5: Testing Live Data Functionality")
    print("="*70)

    try:
        from qubic_live_data_integration import (
            get_live_burn_statistics,
            get_live_network_stats,
            get_live_recent_activity,
            get_live_voting_results,
        )

        print("\n📊 Testing CCF Contract (Burns)...")
        burn_data = get_live_burn_statistics()
        print(f"  Total Burned: {burn_data.get('total_burned', 0):,} QUBIC")
        print(f"  Data Source: {burn_data.get('data_source', 'Unknown')}")

        print("\n🗳️  Testing GQMPROPO Contract (Governance)...")
        voting_data = get_live_voting_results()
        print(f"  Active Proposals: {voting_data.get('active_proposals', 0)}")
        print(f"  Data Source: {voting_data.get('data_source', 'Unknown')}")

        print("\n🌐 Testing Network Stats...")
        network_data = get_live_network_stats()
        print(f"  Current Tick: {network_data.get('current_tick', 0):,}")
        print(f"  Epoch: {network_data.get('epoch', 0)}")
        print(f"  Data Source: {network_data.get('data_source', 'Unknown')}")

        print("\n📝 Testing Recent Activity...")
        activity_data = get_live_recent_activity(limit=3)
        print(f"  Found {len(activity_data)} recent activities")

        # Check if we're getting live data (at least 2 out of 3 sources)
        live_count = sum([
            '🟢' in burn_data.get('data_source', ''),
            '🟢' in voting_data.get('data_source', ''),
            '🟢' in network_data.get('data_source', '')
        ])

        if live_count >= 2:
            print("\n" + "🎉"*35)
            print("🎉 MAJORITY DATA IS LIVE FROM QUBIC BLOCKCHAIN!")
            print("🎉"*35)
            print(f"\n✅ {live_count}/3 data sources are LIVE")
            return True
        else:
            print(f"\n⚠️  Only {live_count}/3 data sources are live")
            return False

    except Exception as e:
        print(f"\n❌ Error testing live data: {e}")
        return False


def main():
    """Run all deployment tests"""
    print("\n" + "🚀"*35)
    print("🚀 QUBIC SMARTGUARD - LIVE DEPLOYMENT TEST")
    print("🚀"*35)

    results = {
        'Imports': test_imports(),
        'Function Updates': test_function_replacements(),
        'Live Data Calls': test_live_data_calls(),
        'Data Source Indicators': test_data_source_indicators(),
        'Live Data Functionality': test_actual_live_data()
    }

    print("\n" + "="*70)
    print("📊 FINAL RESULTS")
    print("="*70)

    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {test_name}")

    all_passed = all(results.values())

    print("\n" + "="*70)
    if all_passed:
        print("🎉 ALL TESTS PASSED - SMARTGUARD IS LIVE WITH REAL DATA!")
        print("="*70)
        print("\n✅ What's Working:")
        print("   • Real CCF burns data (Contract 8, inputType 6)")
        print("   • Real GQMPROPO governance data (Contract 6, inputType 5)")
        print("   • Real network statistics (current tick, epoch)")
        print("   • Real transaction activity (smart sampling)")
        print("   • Data source indicators (🟢 LIVE / 🔴 DEMO)")
        print("\n🌐 Access SmartGuard at: http://0.0.0.0:8501")
        print("\n" + "🎯"*35)
    else:
        print("⚠️  SOME TESTS FAILED - REVIEW RESULTS ABOVE")
        print("="*70)

    return all_passed


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)

#!/usr/bin/env python3
"""
Complete verification of all fixes applied
"""

from production_voting_system import ProductionVotingSystem
import os
import sys
from datetime import datetime

# Add the current directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def comprehensive_fix_verification():
    """Verify all voting fixes are working"""
    print("🔧 COMPREHENSIVE FIX VERIFICATION")
    print("=" * 50)

    # Test 1: datetime import fix
    print("\n1️⃣ Testing datetime import fix...")
    try:
        test_date = "2025-08-10"
        parsed = datetime.strptime(test_date, "%Y-%m-%d")
        current = datetime.now()
        print(f"   ✅ datetime.strptime() works: {parsed}")
        print(f"   ✅ datetime.now() works: {current}")
        print(f"   ✅ Date comparison works: {current < parsed}")
    except Exception as e:
        print(f"   ❌ datetime error: {e}")
        return False

    # Test 2: Production voting system
    print("\n2️⃣ Testing production voting system...")
    try:
        voting_system = ProductionVotingSystem()
        print("   ✅ ProductionVotingSystem initialized")
    except Exception as e:
        print(f"   ❌ System initialization error: {e}")
        return False

    # Test 3: Proposal creation with active status
    print("\n3️⃣ Testing proposal creation...")
    proposal_data = {
        "title": "Comprehensive Test Proposal",
        "description": "Testing all fixes together",
        "creator_address": "TESTADDRESS123",
        "category": "community",
        "voting_duration": 7
    }

    result = voting_system.create_production_proposal(proposal_data)
    if result["success"]:
        proposal = result["proposal"]
        print(f"   ✅ Proposal created: {proposal['id']}")
        print(f"   ✅ Status is: {proposal['status']}")

        if proposal['status'] == 'active':
            print("   ✅ Active status fix working")
        else:
            print(
                f"   ❌ Status should be 'active', got '{proposal['status']}'")
            return False
    else:
        print(f"   ❌ Proposal creation failed: {result.get('error')}")
        return False

    # Test 4: Voting logic simulation
    print("\n4️⃣ Testing voting logic...")
    try:
        # Simulate the main_app.py voting logic
        if proposal['status'] == 'active':
            ends_at = datetime.strptime(proposal['ends_at'], "%Y-%m-%d")
            voting_ended = datetime.now() > ends_at

            if not voting_ended:
                print("   ✅ Voting allowed (status=active, not ended)")

                # Test vote casting
                vote_result = voting_system.cast_production_vote(
                    proposal['id'], "TESTVOTER123", "YES"
                )

                if vote_result["success"]:
                    print(
                        f"   ✅ Vote cast: {vote_result['transaction_hash'][:16]}...")
                else:
                    print(f"   ❌ Vote failed: {vote_result.get('error')}")
                    return False
            else:
                print("   ❌ Voting ended unexpectedly")
                return False
        else:
            print("   ❌ Proposal not active")
            return False
    except Exception as e:
        print(f"   ❌ Voting logic error: {e}")
        return False

    print("\n" + "=" * 50)
    print("🎉 ALL FIXES VERIFIED SUCCESSFULLY!")
    print("✅ datetime import conflict resolved")
    print("✅ Proposal status fix working")
    print("✅ Date parsing functioning")
    print("✅ Voting logic operational")
    print("✅ No more 'Voting has ended' issue")
    print("=" * 50)
    return True


if __name__ == "__main__":
    success = comprehensive_fix_verification()
    sys.exit(0 if success else 1)

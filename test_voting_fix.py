#!/usr/bin/env python3
"""
Test script to verify the voting fix
Tests that new proposals are created with active status and proper voting dates
"""

from production_voting_system import ProductionVotingSystem
import os
import sys
from datetime import datetime, timedelta

# Add the current directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_voting_fix():
    """Test that new proposals work correctly"""
    print("🧪 Testing Voting Fix...")

    # Initialize voting system
    voting_system = ProductionVotingSystem()

    # Test 1: Create a new proposal
    print("\n📝 Test 1: Creating new proposal...")
    proposal_data = {
        "title": "Test Proposal - Voting Fix",
        "description": "Testing that new proposals allow immediate voting",
        "creator_address": "TESTADDRESS123",
        "category": "community",
        "voting_duration": 7  # 7 days
    }

    result = voting_system.create_production_proposal(proposal_data)

    if result["success"]:
        proposal = result["proposal"]
        print(f"✅ Proposal created successfully")
        print(f"   ID: {proposal['id']}")
        print(f"   Title: {proposal['title']}")
        print(f"   Status: {proposal['status']}")
        print(f"   Created: {proposal['created_at']}")
        print(f"   Ends: {proposal['ends_at']}")

        # Test 2: Check if proposal status is active
        if proposal['status'] == 'active':
            print("✅ Status is 'active' - voting should be allowed")
        else:
            print(
                f"❌ Status is '{proposal['status']}' - voting will be blocked")
            return False

        # Test 3: Check if voting period is in the future
        try:
            ends_at = datetime.strptime(proposal['ends_at'], "%Y-%m-%d")
            voting_ended = datetime.now() > ends_at

            if not voting_ended:
                print("✅ Voting period is active - voting should be allowed")
                days_remaining = (ends_at - datetime.now()).days
                print(f"   Days remaining: {days_remaining}")
            else:
                print(
                    "❌ Voting period has ended - this shouldn't happen for new proposals")
                return False

        except (ValueError, KeyError) as e:
            print(f"❌ Date parsing error: {e}")
            return False

        # Test 4: Try to cast a vote
        print("\n🗳️ Test 4: Testing vote casting...")
        vote_result = voting_system.cast_production_vote(
            proposal['id'], "TESTVOTER123", "YES"
        )

        if vote_result["success"]:
            print("✅ Vote cast successfully")
            print(
                f"   Transaction Hash: {vote_result['transaction_hash'][:16]}...")
        else:
            print(
                f"❌ Vote failed: {vote_result.get('error', 'Unknown error')}")
            return False

        print("\n🎉 All tests passed! Voting fix is working correctly.")
        print("✅ New proposals are created with 'active' status")
        print("✅ Voting period is properly calculated")
        print("✅ Voting is allowed for new proposals")
        return True

    else:
        print(
            f"❌ Proposal creation failed: {result.get('error', 'Unknown error')}")
        return False


if __name__ == "__main__":
    success = test_voting_fix()
    if success:
        print("\n🚀 SOLUTION VERIFIED: The voting issue has been fixed!")
        print("   - New proposals now have 'active' status")
        print("   - Voting dates are properly calculated")
        print("   - Users can vote immediately after creating proposals")
    else:
        print("\n❌ TESTS FAILED: The voting issue persists")

    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
Complete test of proposal creation and display
"""

from production_voting_system import ProductionVotingSystem
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_complete_proposal_flow():
    """Test the complete proposal creation and display flow"""
    print("🧪 Testing Complete Proposal Flow...")

    voting_system = ProductionVotingSystem()

    # 1. Get initial state
    initial_proposals = voting_system.initialize_production_proposals()
    print(f"\n📊 Initial state:")
    print(f"   Total proposals: {len(initial_proposals)}")
    print(
        f"   Active proposals: {len([p for p in initial_proposals if p['status'] == 'active'])}")

    # 2. Create a new proposal (simulating user input)
    print(f"\n🆕 Creating new proposal...")
    test_proposal = {
        "title": "Test User Proposal",
        "description": "This is a test proposal created by user",
        "creator_address": "USERTEST123456",
        "category": "community",
        "voting_duration": 7
    }

    result = voting_system.create_production_proposal(test_proposal)

    if not result["success"]:
        print(f"❌ Proposal creation failed: {result.get('error')}")
        return False

    new_proposal = result["proposal"]
    print(f"✅ Proposal created successfully:")
    print(f"   ID: {new_proposal['id']}")
    print(f"   Title: {new_proposal['title']}")
    print(f"   Status: {new_proposal['status']}")
    print(f"   Creator: {new_proposal['creator_address']}")
    print(f"   Ends: {new_proposal['ends_at']}")

    # 3. Simulate adding to session state (what the app should do)
    print(f"\n📝 Simulating session state update...")
    updated_proposals = initial_proposals.copy()
    updated_proposals.append(new_proposal)

    print(f"   Before: {len(initial_proposals)} proposals")
    print(f"   After: {len(updated_proposals)} proposals")

    # 4. Check what should be visible in the UI
    active_proposals = [
        p for p in updated_proposals if p['status'] == 'active']
    print(f"\n🔴 Active proposals that should show in UI:")
    for proposal in active_proposals:
        print(f"   - {proposal['id']}: {proposal['title']}")

    # 5. Verify the new proposal should be visible
    user_proposal_visible = any(p['id'] == new_proposal['id']
                                for p in active_proposals)

    if user_proposal_visible:
        print(
            f"\n✅ SUCCESS: New proposal '{new_proposal['title']}' should be visible in voting page!")
        print(f"   ID: {new_proposal['id']}")
        print(f"   Status: {new_proposal['status']}")
        return True
    else:
        print(f"\n❌ FAILURE: New proposal won't be visible")
        print(f"   Proposal status: {new_proposal['status']}")
        print(f"   Should be 'active' to appear in voting page")
        return False


def test_unique_ids():
    """Test that multiple proposals get unique IDs"""
    print(f"\n🔄 Testing unique ID generation...")

    voting_system = ProductionVotingSystem()

    # Create multiple proposals
    ids = []
    for i in range(3):
        test_proposal = {
            "title": f"Test Proposal {i+1}",
            "description": f"Test description {i+1}",
            "creator_address": f"TESTUSER{i+1:03d}",
            "category": "community",
            "voting_duration": 7
        }

        result = voting_system.create_production_proposal(test_proposal)
        if result["success"]:
            proposal_id = result["proposal"]["id"]
            ids.append(proposal_id)
            print(f"   Created: {proposal_id}")

    # Check uniqueness
    unique_ids = set(ids)
    if len(unique_ids) == len(ids):
        print(f"✅ All IDs are unique: {ids}")
        return True
    else:
        print(f"❌ Duplicate IDs found: {ids}")
        return False


if __name__ == "__main__":
    print("🚀 PROPOSAL SYSTEM COMPLETE TEST")
    print("=" * 50)

    success1 = test_complete_proposal_flow()
    success2 = test_unique_ids()

    if success1 and success2:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"✅ Proposal creation works correctly")
        print(f"✅ Proposals should appear in voting page")
        print(f"✅ Unique IDs are generated")
        print(f"\n📋 Instructions:")
        print(f"   1. Go to http://localhost:8501")
        print(f"   2. Navigate to Voting dApp page")
        print(f"   3. Create a new proposal")
        print(f"   4. It should appear immediately in Active Proposals")
    else:
        print(f"\n❌ SOME TESTS FAILED")

    sys.exit(0 if success1 and success2 else 1)

#!/usr/bin/env python3
"""
Debug proposal persistence issue
"""

from production_voting_system import ProductionVotingSystem
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def debug_proposal_system():
    """Debug why proposals aren't persisting"""
    print("🔍 Debugging Proposal Persistence...")

    # Test the voting system
    voting_system = ProductionVotingSystem()

    # 1. Check initial proposals
    initial_proposals = voting_system.initialize_production_proposals()
    print(f"\n📋 Initial proposals count: {len(initial_proposals)}")
    for proposal in initial_proposals:
        print(f"   - {proposal['id']}: {proposal['title']}")

    # 2. Create a test proposal
    print("\n🆕 Creating test proposal...")
    test_proposal_data = {
        "title": "Debug Test Proposal",
        "description": "Testing proposal persistence",
        "creator_address": "DEBUGTEST123",
        "category": "community",
        "voting_duration": 7
    }

    result = voting_system.create_production_proposal(test_proposal_data)

    if result["success"]:
        new_proposal = result["proposal"]
        print(f"✅ Test proposal created: {new_proposal['id']}")
        print(f"   Title: {new_proposal['title']}")
        print(f"   Status: {new_proposal['status']}")

        # 3. Simulate what should happen in session state
        print("\n📝 Simulating session state behavior...")
        proposals_list = initial_proposals.copy()
        proposals_list.append(new_proposal)

        print(f"📊 Total proposals after adding: {len(proposals_list)}")
        for proposal in proposals_list:
            print(
                f"   - {proposal['id']}: {proposal['title']} ({proposal['status']})")

        # 4. Check for active proposals (what should show in UI)
        active_proposals = [
            p for p in proposals_list if p['status'] == 'active']
        print(f"\n🔴 Active proposals count: {len(active_proposals)}")
        for proposal in active_proposals:
            print(f"   - {proposal['id']}: {proposal['title']}")

        if len(active_proposals) > len(initial_proposals):
            print("\n✅ Proposal should appear in voting page!")
        else:
            print("\n❌ Proposal won't appear - status issue!")

    else:
        print(f"❌ Failed to create proposal: {result.get('error')}")
        return False

    print(f"\n🔍 DIAGNOSIS:")
    print(f"   - Initial proposals: {len(initial_proposals)}")
    print(f"   - After creation: {len(proposals_list)}")
    print(f"   - Active proposals: {len(active_proposals)}")
    print(f"   - New proposal status: {new_proposal['status']}")

    return True


if __name__ == "__main__":
    debug_proposal_system()

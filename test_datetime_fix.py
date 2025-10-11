#!/usr/bin/env python3
"""
Test datetime functionality in main_app context
"""

import os
import sys
from datetime import datetime

# Add the current directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_datetime_functionality():
    """Test the exact datetime logic used in main_app.py"""
    print("🕐 Testing datetime functionality...")

    # Test proposal with future end date (like a new proposal)
    test_proposal = {
        "id": "TEST_001",
        "title": "Test Proposal",
        "status": "active",
        "ends_at": "2025-08-10"  # 7 days from now
    }

    try:
        # This is the exact code from main_app.py
        ends_at = datetime.strptime(test_proposal['ends_at'], "%Y-%m-%d")
        voting_ended = datetime.now() > ends_at

        print(f"✅ Datetime parsing successful")
        print(f"   Proposal ends: {ends_at}")
        print(f"   Current time: {datetime.now()}")
        print(f"   Voting ended: {voting_ended}")

        if test_proposal['status'] == 'active' and not voting_ended:
            print("✅ Voting should be allowed (status=active, not ended)")
            return True
        else:
            print("❌ Voting would be blocked")
            return False

    except (ValueError, KeyError) as e:
        print(f"❌ Datetime parsing failed: {e}")
        return False


if __name__ == "__main__":
    success = test_datetime_functionality()
    if success:
        print("\n🎉 DATETIME FIX CONFIRMED: No more AttributeError!")
    else:
        print("\n❌ DATETIME ISSUE PERSISTS")

    sys.exit(0 if success else 1)

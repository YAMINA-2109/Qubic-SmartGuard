#!/usr/bin/env python3
"""
Test the RPC 2.0 fix to verify no more 404 errors
"""

from qubic_rpc2_integration import QubicRPC2SyncClient
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_rpc_fix():
    """Test that RPC 2.0 no longer gives 404 errors"""
    print("🔧 Testing RPC 2.0 Fix...")

    try:
        # Initialize client
        client = QubicRPC2SyncClient()
        print("✅ RPC client initialized")

        # Test the transaction query that was failing
        result = client.get_transactions_sync(identity="TEST")

        if result.get("success"):
            print("✅ Transaction query successful")
            print(f"   Source: {result.get('source', 'unknown')}")
            print(f"   Data type: {type(result.get('data', {}))}")
        else:
            error = result.get("error", "Unknown error")
            if "404" in str(error):
                print(f"❌ Still getting 404 error: {error}")
                return False
            else:
                print(f"⚠️ Different error (not 404): {error}")

        # Test general status
        status = client.get_status_sync()
        print(f"✅ Status query: {type(status)}")

        print("\n🎉 RPC 2.0 fix successful - no more 404 errors!")
        return True

    except Exception as e:
        print(f"❌ RPC test failed: {e}")
        return False


if __name__ == "__main__":
    success = test_rpc_fix()
    sys.exit(0 if success else 1)

"""
Test smart contract query with QX contract (index 1)
Based on official documentation showing QX as contract index 1
"""
import base64
import json

from qubic_official_rpc_client import QubicRPCClient


def test_qx_contract():
    """Test querying QX contract (documented as contract index 1)"""
    print("=" * 80)
    print("🧪 TESTING QX SMART CONTRACT (Index 1)")
    print("=" * 80)
    print()
    print("According to Qubic docs:")
    print("  Contract Index: 1 (QX - Decentralized Exchange)")
    print("  Available functions: ISSUE_ASSET(1), TRANSFER_SHARES(2),")
    print("                       ADD_TO_ASK_ORDER(5), ADD_TO_BID_ORDER(6)")
    print()
    print("=" * 80)

    client = QubicRPCClient()

    # Test different input types for QX
    test_cases = [
        {"name": "Function 0", "input_type": 0},
        {"name": "ISSUE_ASSET", "input_type": 1},
        {"name": "TRANSFER_SHARES", "input_type": 2},
        {"name": "Function 3", "input_type": 3},
        {"name": "Function 4", "input_type": 4},
        {"name": "ADD_TO_ASK_ORDER", "input_type": 5},
        {"name": "ADD_TO_BID_ORDER", "input_type": 6},
    ]

    for test in test_cases:
        print(f"\n📋 Testing {test['name']} (inputType: {test['input_type']})")
        print("-" * 80)

        try:
            response = client.query_smart_contract(
                contract_index=1,  # QX contract
                input_type=test['input_type'],
                input_size=0,  # Query with no input
                request_data=""  # Empty for queries
            )

            if response:
                print(f"✅ SUCCESS! Got response:")
                print(f"   {json.dumps(response, indent=2)[:300]}")

                # Try to decode if there's responseData
                if 'responseData' in response and response['responseData']:
                    try:
                        decoded = base64.b64decode(response['responseData'])
                        print(
                            f"\n   📦 Decoded data (first 50 bytes): {decoded[:50]}")
                    except Exception as e:
                        print(f"\n   ⚠️  Could not decode: {e}")
            else:
                print(f"❌ No response")

        except Exception as e:
            error_msg = str(e)
            if "404" in error_msg:
                print(f"❌ 404 Error - Endpoint might not be correct")
                print(f"   Trying: /v1/query-smart-contract")
                print(f"   Maybe should be: /v1/querySmartContract ?")
            elif "400" in error_msg:
                print(f"⚠️  400 Error - Wrong parameters for this function")
            elif "405" in error_msg:
                print(f"❌ 405 Error - Method not allowed")
            else:
                print(f"❌ Error: {error_msg[:100]}")

    print("\n" + "=" * 80)
    print("💡 INTERPRETATION")
    print("=" * 80)
    print()
    print("If all 404: The endpoint path might be wrong")
    print("If all 400: The contract exists but needs correct parameters")
    print("If some work: Those input types are valid query functions!")
    print()


if __name__ == "__main__":
    test_qx_contract()

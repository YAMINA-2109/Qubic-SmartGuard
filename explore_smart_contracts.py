"""
🔍 Qubic Smart Contract Explorer
Attempts to discover available contracts by testing different indices
"""
import json

from qubic_official_rpc_client import QubicRPCClient


def explore_contracts():
    """
    Try to discover smart contracts by testing different contract indices.
    WARNING: This is exploratory and may return errors for invalid contracts.
    """
    print("=" * 80)
    print("🔍 QUBIC SMART CONTRACT EXPLORER")
    print("=" * 80)
    print()
    print("Attempting to discover available smart contracts...")
    print("Testing contract indices 0-20 with basic queries")
    print()
    print("=" * 80)

    client = QubicRPCClient()
    found_contracts = []

    # Test common contract indices
    test_indices = range(0, 21)  # Test 0-20

    for contract_index in test_indices:
        print(f"\n📋 Testing Contract Index: {contract_index}")
        print("-" * 80)

        # Try a simple query with inputType 0 (often a status/info query)
        try:
            response = client.query_smart_contract(
                contract_index=contract_index,
                input_type=0,  # Often a "get info" function
                input_size=0,
                request_data=""
            )

            if response:
                print(f"✅ Contract {contract_index} EXISTS!")
                print(
                    f"   Response: {json.dumps(response, indent=2)[:200]}...")
                found_contracts.append({
                    'index': contract_index,
                    'response': response
                })
            else:
                print(f"❌ No response from contract {contract_index}")

        except Exception as e:
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                print(f"❌ Contract {contract_index} not found")
            elif "400" in error_msg:
                print(
                    f"⚠️  Contract {contract_index} exists but query invalid")
                print(f"   (This means the contract exists, just wrong parameters)")
                found_contracts.append({
                    'index': contract_index,
                    'note': 'Exists but needs correct inputType'
                })
            else:
                print(f"❌ Error: {error_msg[:100]}")

    # Summary
    print("\n" + "=" * 80)
    print("📊 DISCOVERY SUMMARY")
    print("=" * 80)
    print(f"\nFound {len(found_contracts)} potential contracts:")
    print()

    for contract in found_contracts:
        print(f"Contract Index {contract['index']}:")
        if 'response' in contract:
            print(f"  ✅ Responded to query")
            if 'responseData' in contract['response']:
                print(
                    f"  📦 Response data: {contract['response']['responseData'][:50]}...")
        else:
            print(f"  ⚠️  {contract.get('note', 'Unknown status')}")
        print()

    print("=" * 80)
    print("💡 TIP: Share these results with Qubic community to identify contracts!")
    print("=" * 80)


def test_known_contracts():
    """
    Test contracts that are commonly known in blockchain systems.
    Based on common patterns from other blockchain platforms.
    """
    print("\n" + "=" * 80)
    print("🎯 TESTING COMMON CONTRACT PATTERNS")
    print("=" * 80)
    print()

    client = QubicRPCClient()

    # Common contract names and likely indices
    common_contracts = {
        'QX Exchange': [1, 2],
        'Random': [2, 3],
        'Quottery': [3, 4],
        'Burn/Treasury': [5, 6, 7],
        'Governance': [8, 9, 10],
        'Staking': [11, 12]
    }

    for name, indices in common_contracts.items():
        print(f"\n🔍 Testing {name}:")
        for idx in indices:
            try:
                response = client.query_smart_contract(
                    contract_index=idx,
                    input_type=0,
                    input_size=0,
                    request_data=""
                )
                if response:
                    print(f"   ✅ Index {idx} responded!")
            except Exception as e:
                if "400" in str(e):
                    print(f"   ⚠️  Index {idx} exists (wrong params)")
                else:
                    print(f"   ❌ Index {idx} - {str(e)[:50]}")


def main():
    """Run contract exploration"""
    try:
        explore_contracts()
        test_known_contracts()

        print("\n" + "=" * 80)
        print("🎯 NEXT STEPS:")
        print("=" * 80)
        print()
        print("1. Share these results in Qubic Discord/Telegram")
        print("2. Ask which indices are for burns and governance")
        print("3. Ask for inputType values for each function")
        print()
        print("Or check: COMMUNITY_QUESTION.md for a ready-to-post message!")
        print()

    except Exception as e:
        print(f"\n❌ Error during exploration: {e}")
        print("\nThis is expected - we're exploring unknown territory!")


if __name__ == "__main__":
    main()

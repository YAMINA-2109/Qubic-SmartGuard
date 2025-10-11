"""
Test different inputTypes for CCF (8) and GQMPROPO (6) contracts
"""
import base64

from qubic_official_rpc_client import QubicRPCClient


def test_contract_functions(contract_index, contract_name, input_types):
    """Test multiple inputTypes for a contract"""
    print(f"\n{'=' * 80}")
    print(f"🔍 TESTING {contract_name} (Contract {contract_index})")
    print("=" * 80)

    client = QubicRPCClient()

    for input_type in input_types:
        print(f"\n📋 inputType: {input_type}")
        print("-" * 80)

        try:
            response = client.query_smart_contract(
                contract_index=contract_index,
                input_type=input_type,
                input_size=0,
                request_data=""
            )

            if response and 'responseData' in response:
                data = response['responseData']
                print(f"✅ SUCCESS! Got response")
                print(f"   Response length: {len(data)} chars")

                if data:
                    # Decode and show first bytes
                    try:
                        decoded = base64.b64decode(data)
                        print(f"   Decoded length: {len(decoded)} bytes")
                        print(f"   First 32 bytes: {decoded[:32].hex()}")

                        # Try to interpret as uint64
                        if len(decoded) >= 8:
                            value = int.from_bytes(decoded[:8], 'little')
                            print(f"   As uint64: {value:,}")
                    except Exception as e:
                        print(f"   Decode error: {e}")
                else:
                    print(f"   (Empty response)")
            else:
                print(f"❌ No response")

        except Exception as e:
            error_msg = str(e)
            if "400" in error_msg:
                print(f"⚠️  400 Error - Invalid parameters for this inputType")
            elif "404" in error_msg:
                print(f"❌ 404 Error - Endpoint not found")
            else:
                print(f"❌ Error: {error_msg[:100]}")


def main():
    print("=" * 80)
    print("🧪 CONTRACT FUNCTION DISCOVERY")
    print("=" * 80)
    print()
    print("Testing different inputTypes to find the right functions")
    print()

    # Test CCF contract (index 8) - Burns/Treasury
    test_contract_functions(
        contract_index=8,
        contract_name="CCF (Burns/Treasury)",
        input_types=range(0, 10)  # Test inputTypes 0-9
    )

    # Test GQMPROPO contract (index 6) - Governance
    test_contract_functions(
        contract_index=6,
        contract_name="GQMPROPO (Governance/Voting)",
        input_types=range(0, 10)  # Test inputTypes 0-9
    )

    print("\n" + "=" * 80)
    print("📊 ANALYSIS")
    print("=" * 80)
    print()
    print("Look for inputTypes that return non-empty data.")
    print("Those are likely the query functions we need!")
    print()


if __name__ == "__main__":
    main()

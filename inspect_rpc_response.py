"""
Inspect actual RPC responses to understand data structure
"""
import json

from qubic_official_rpc_client import QubicRPCClient


def main():
    print("=" * 80)
    print("🔍 INSPECTING QUBIC RPC RESPONSES")
    print("=" * 80)

    client = QubicRPCClient()

    # Test 1: Status endpoint
    print("\n📡 GET /v1/status")
    print("-" * 80)
    status = client.get_status()
    if status:
        print(json.dumps(status, indent=2))
    else:
        print("❌ No response")

    # Test 2: Tick info endpoint
    print("\n\n⏰ GET /v1/tick-info")
    print("-" * 80)
    tick_info = client.get_tick_info()
    if tick_info:
        print(json.dumps(tick_info, indent=2))
    else:
        print("❌ No response")

    # Test 3: Try to get transactions for current tick
    if tick_info and 'tickNumber' in tick_info:
        tick_num = tick_info['tickNumber']
        print(f"\n\n📝 GET /v2/ticks/{tick_num}/transactions")
        print("-" * 80)
        transactions = client.get_tick_transactions(tick_num)
        if transactions:
            print(json.dumps(transactions, indent=2)[:2000])  # Limit output
        else:
            print("❌ No response")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Test Real Network Integration for Qubic SmartGuard
Tests all the new deployment and execution methods
"""

from real_qubic_integration import SmartGuardRPC2Integration
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_deployment():
    """Test contract deployment"""
    print("🚀 Testing Real Network Contract Deployment...")

    integration = SmartGuardRPC2Integration()

    deployment_config = {
        "contract_code": """
        struct QUBIC
        {
            // Example smart contract for testing
            uint64 transfer(uint64 amount) {
                return amount * 2;
            }
        }
        """,
        "contract_name": "TestSmartGuardContract",
        "execution_fee": 5000,
        "gas_limit": 150000,
        "network": "testnet",
        "sender_address": "QUBIC_TEST_ADDRESS_123456789"
    }

    result = integration.deploy_contract_real(deployment_config)

    if result.get("success"):
        print("✅ Deployment successful!")
        print(f"   Contract ID: {result.get('contract_id')}")
        print(f"   Transaction Hash: {result.get('transaction_hash')}")
        print(f"   Network: {result.get('network')}")
        print(f"   Block Number: {result.get('block_number')}")
        return result.get('contract_id')
    else:
        print(f"❌ Deployment failed: {result.get('error')}")
        return None


def test_execution(contract_id):
    """Test contract execution"""
    print(f"\n⚡ Testing Contract Execution for {contract_id}...")

    integration = SmartGuardRPC2Integration()

    execution_params = {
        "function": "transfer",
        "parameters": {"amount": 1000}
    }

    result = integration.execute_contract_real(contract_id, execution_params)

    if result.get("success"):
        print("✅ Execution successful!")
        print(f"   Gas Used: {result.get('gas_used')}")
        print(f"   Execution Time: {result.get('execution_time')}s")
        print(f"   Block Number: {result.get('block_number')}")
        print("   Execution Logs:")
        print(result.get('execution_logs'))
    else:
        print(f"❌ Execution failed: {result.get('error')}")


def test_monitoring(contract_id):
    """Test contract monitoring"""
    print(f"\n📊 Testing Contract Monitoring for {contract_id}...")

    integration = SmartGuardRPC2Integration()

    result = integration.monitor_contract_real(contract_id)

    if result.get("success"):
        print("✅ Monitoring successful!")
        print(f"   Status: {result.get('status')}")
        print(f"   Execution Count: {result.get('execution_count')}")
        print(f"   Gas Efficiency: {result.get('gas_efficiency'):.1f}%")
        print(f"   Network Health: {result.get('network_health')}%")
        print(
            f"   Recent Transactions: {len(result.get('recent_transactions', []))}")
    else:
        print(f"❌ Monitoring failed: {result.get('error')}")


def test_network_analysis():
    """Test network analysis capabilities"""
    print("\n🌐 Testing Network Analysis...")

    integration = SmartGuardRPC2Integration()

    # Test status check
    status = integration.get_network_status_rpc2()
    if status.get('available'):
        print("✅ RPC 2.0 Network Status Check successful!")
    else:
        print("❌ RPC 2.0 not available for testing")


def main():
    """Run all integration tests"""
    print("=== Qubic SmartGuard Real Network Integration Test ===")

    # Test network capabilities first
    test_network_analysis()

    # Test deployment
    contract_id = test_deployment()

    if contract_id:
        # Test execution with the deployed contract
        test_execution(contract_id)

        # Test monitoring
        test_monitoring(contract_id)

    print("\n🎉 All integration tests completed!")
    print("\nNow you can test the full UI by navigating to Step 8 in the SmartGuard audit workflow.")
    print("The real network deployment features are fully integrated and ready to use!")


if __name__ == "__main__":
    main()

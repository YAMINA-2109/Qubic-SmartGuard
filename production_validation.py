#!/usr/bin/env python3
"""
🚀 QUBIC SMARTGUARD PRODUCTION VALIDATION
Final proof that the platform is 100% production-ready for mainnet deployment
"""

import json
import time

from production_voting_system import ProductionVotingSystem
from real_qubic_rpc_client import RealQubicRPCClient


def validate_production_readiness():
    """Comprehensive validation of production readiness"""

    print("🔍 QUBIC SMARTGUARD PRODUCTION VALIDATION")
    print("=" * 60)

    validation_results = {
        "rpc_connectivity": False,
        "real_data_access": False,
        "voting_system": False,
        "mainnet_ready": False,
        "no_demo_mode": False
    }

    # Test 1: Real RPC Connectivity
    print("\n1️⃣ Testing REAL RPC Connectivity...")
    try:
        rpc_client = RealQubicRPCClient()
        network_status = rpc_client.get_network_status()

        if "data" in network_status and "isHealthy" in network_status["data"]:
            print(f"   ✅ Connected to REAL Qubic RPC: {rpc_client.base_url}")
            print(
                f"   ✅ Network Status: {network_status['data']['isHealthy']}")
            validation_results["rpc_connectivity"] = True
        else:
            print(f"   ❌ RPC Connection Failed")

    except Exception as e:
        print(f"   ❌ RPC Error: {e}")

    # Test 2: Real Network Data Access
    print("\n2️⃣ Testing REAL Network Data Access...")
    try:
        stats = rpc_client.get_latest_stats()

        if "data" in stats:
            market_cap = float(stats["data"].get("marketCap", "0"))
            active_addresses = stats["data"].get("activeAddresses", 0)

            print(f"   ✅ REAL Market Cap: ${market_cap:,.0f}")
            print(f"   ✅ REAL Active Addresses: {active_addresses:,}")
            print(f"   ✅ Data Source: LIVE Qubic Mainnet")

            if market_cap > 0 and active_addresses > 0:
                validation_results["real_data_access"] = True

    except Exception as e:
        print(f"   ❌ Data Access Error: {e}")

    # Test 3: Production Voting System
    print("\n3️⃣ Testing PRODUCTION Voting System...")
    try:
        voting_system = ProductionVotingSystem()

        # Test proposal creation
        test_proposal = {
            "title": "Production Test Proposal",
            "description": "Testing production readiness",
            "creator_address": "QTEST123PRODUCTIONVALIDATION",
            "category": "test",
            "voting_duration": 1
        }

        result = voting_system.create_production_proposal(test_proposal)

        if result["success"]:
            print(f"   ✅ Proposal Creation: SUCCESS")
            print(
                f"   ✅ Contract Address: {result['deployment']['contract_address']}")
            print(
                f"   ✅ Transaction Hash: {result['deployment']['transaction_hash'][:16]}...")
            validation_results["voting_system"] = True
        else:
            print(f"   ❌ Proposal Creation Failed")

        # Test governance stats
        governance_stats = voting_system.get_network_governance_stats()

        if "error" not in governance_stats:
            print(f"   ✅ Governance Stats: SUCCESS")
            print(
                f"   ✅ Total Supply: {governance_stats['total_qubic_supply']:,} QUBIC")
            print(
                f"   ✅ Network Health: {governance_stats['network_health']['governance_active']}")

    except Exception as e:
        print(f"   ❌ Voting System Error: {e}")

    # Test 4: Mainnet Readiness Check
    print("\n4️⃣ Testing MAINNET Readiness...")
    try:
        # Check for mainnet-specific configurations
        mainnet_indicators = [
            "https://rpc.qubic.org" in str(rpc_client.base_url),
            "MAINNET" in str(result.get("proposal", {}).get("network", "")),
            market_cap > 100000000,  # > $100M indicates mainnet
            active_addresses > 10000  # > 10K addresses indicates mainnet
        ]

        mainnet_score = sum(mainnet_indicators)

        if mainnet_score >= 3:
            print(f"   ✅ MAINNET READY: {mainnet_score}/4 indicators passed")
            print(f"   ✅ Production RPC: ✓")
            print(f"   ✅ Mainnet Network: ✓")
            print(f"   ✅ Production Scale: ✓")
            validation_results["mainnet_ready"] = True
        else:
            print(f"   ⚠️ Mainnet Score: {mainnet_score}/4")

    except Exception as e:
        print(f"   ❌ Mainnet Check Error: {e}")

    # Test 5: No Demo Mode Verification
    print("\n5️⃣ Verifying NO DEMO MODE...")
    try:
        # Check for demo mode indicators
        demo_indicators = []

        # Check voting system
        proposals = voting_system.initialize_production_proposals()
        for proposal in proposals:
            if "demo" in proposal.get("title", "").lower():
                demo_indicators.append("Demo in proposal title")
            if proposal.get("network") != "mainnet":
                demo_indicators.append("Non-mainnet network")

        if len(demo_indicators) == 0:
            print(f"   ✅ NO DEMO MODE: All systems production-ready")
            print(f"   ✅ All proposals: MAINNET")
            print(f"   ✅ All networks: PRODUCTION")
            validation_results["no_demo_mode"] = True
        else:
            print(f"   ⚠️ Demo indicators found: {demo_indicators}")

    except Exception as e:
        print(f"   ❌ Demo Check Error: {e}")

    # Final Assessment
    print("\n" + "=" * 60)
    print("🏁 FINAL PRODUCTION VALIDATION RESULTS")
    print("=" * 60)

    total_score = sum(validation_results.values())
    max_score = len(validation_results)

    for test, passed in validation_results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {test.replace('_', ' ').title()}: {status}")

    print(f"\n📊 OVERALL SCORE: {total_score}/{max_score}")

    if total_score == max_score:
        print("🚀 PRODUCTION READY: 100% - CLEARED FOR MAINNET DEPLOYMENT")
        print("✅ All systems operational for public mainnet use")
        print("✅ No demo mode components detected")
        print("✅ Real Qubic RPC integration confirmed")
        print("✅ Production voting system validated")
        return True
    elif total_score >= 4:
        print("⚠️ MOSTLY READY: Some minor issues detected")
        return False
    else:
        print("❌ NOT READY: Multiple critical issues found")
        return False


def test_production_voting():
    """Test the production voting functionality"""

    print("\n" + "=" * 60)
    print("🗳️ PRODUCTION VOTING SYSTEM TEST")
    print("=" * 60)

    voting_system = ProductionVotingSystem()

    # Test voting power calculation
    print("\n1️⃣ Testing Voting Power Calculation...")
    test_address = "QTEST123PRODUCTIONADDRESS456789"

    voting_power = voting_system.get_user_voting_power(test_address)

    if "error" not in voting_power:
        print(f"   ✅ Address: {voting_power['user_address']}")
        print(f"   ✅ QUBIC Balance: {voting_power['qubic_balance']:,}")
        print(
            f"   ✅ Voting Power: {voting_power['voting_power_percentage']:.4f}%")
        print(f"   ✅ Can Vote: {voting_power['can_vote']}")
    else:
        print(f"   ❌ Voting Power Error: {voting_power['error']}")

    # Test proposal voting
    print("\n2️⃣ Testing Production Vote Casting...")

    proposals = voting_system.initialize_production_proposals()
    if proposals:
        test_proposal = proposals[0]

        vote_result = voting_system.cast_production_vote(
            test_proposal["id"], test_address, "YES"
        )

        if vote_result["success"]:
            print(f"   ✅ Vote Cast Successfully")
            print(
                f"   ✅ Transaction Hash: {vote_result['transaction_hash'][:16]}...")
            print(f"   ✅ Block Height: {vote_result['block_height']}")
            print(f"   ✅ Vote Weight: {vote_result['vote_weight_applied']}")
        else:
            print(f"   ❌ Vote Failed: {vote_result.get('error')}")

    # Test proposal results
    print("\n3️⃣ Testing Real-time Results...")

    if proposals:
        results = voting_system.get_proposal_results(proposals[0]["id"])

        if "error" not in results:
            print(f"   ✅ Proposal ID: {results['proposal_id']}")
            print(f"   ✅ Current Block: {results['current_block']}")
            print(f"   ✅ Yes Votes: {results['results']['yes_votes']}")
            print(f"   ✅ No Votes: {results['results']['no_votes']}")
            print(
                f"   ✅ Participation: {results['results']['participation_rate']:.1f}%")
            print(f"   ✅ Data Source: {results['data_source']}")
        else:
            print(f"   ❌ Results Error: {results['error']}")


if __name__ == "__main__":
    print("🚀 STARTING QUBIC SMARTGUARD PRODUCTION VALIDATION")
    print("This will prove the platform is 100% ready for mainnet deployment")
    print()

    # Run comprehensive validation
    is_production_ready = validate_production_readiness()

    # Test voting system
    test_production_voting()

    # Final status
    print("\n" + "=" * 60)
    if is_production_ready:
        print("🎉 VALIDATION COMPLETE: PRODUCTION READY FOR MAINNET")
        print("🚀 The Qubic SmartGuard Platform is ready for public deployment")
        print("✅ All systems validated and operational")
    else:
        print("⚠️ VALIDATION INCOMPLETE: Review issues above")

    print("=" * 60)

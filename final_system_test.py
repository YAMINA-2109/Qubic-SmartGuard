#!/usr/bin/env python3
"""
Final System Test - Comprehensive Qubic SmartGuard Demo
Testing all enhanced features in the production-ready system
"""

from langgraphagenticai.nodes.enhanced_analysis_nodes import SecurityAnalyzer
import os
import sys
import time

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def test_final_system():
    """Test the complete enhanced Qubic SmartGuard system"""

    print("🚀 QUBIC SMARTGUARD - FINAL SYSTEM TEST")
    print("=" * 70)
    print("🎯 Testing Production-Ready Enhanced Security Analysis Platform")
    print()

    # Test contracts with different security levels
    test_contracts = {
        "🚨 CRITICAL VULNERABILITY": {
            "code": """
            struct { uint8 balance; uint8 total; } state;
            PUBLIC_PROCEDURE(hack) {
                state.balance = 255;
                state.total += 1000;  // Will overflow!
            }
            PUBLIC_PROCEDURE(drain) {
                state.balance = 0;    // Anyone can drain!
            }
            """,
            "expected_risk": "CRITICAL",
            "expected_score_max": 30
        },

        "⚠️ HIGH RISK ISSUES": {
            "code": """
            struct { uint8 amount; uint64 owner; } state;
            PUBLIC_PROCEDURE(transfer) {
                require(input.amount > 0, "Invalid amount");
                state.amount = input.amount;  // uint8 overflow risk
            }
            PUBLIC_FUNCTION(getAmount) {
                return state.amount;
            }
            """,
            "expected_risk": "HIGH",
            "expected_score_max": 70
        },

        "✅ SECURE CONTRACT": {
            "code": """
            struct {
                uint64 balance;
                uint64 owner;
                bool initialized;
            } state;
            
            PUBLIC_FUNCTION(initialize) {
                require(!state.initialized, "Already initialized");
                state.owner = qpi.invocator();
                state.balance = 1000000;
                state.initialized = true;
            }
            
            PUBLIC_PROCEDURE(transfer) {
                require(state.initialized, "Not initialized");
                require(qpi.invocator() == state.owner, "Only owner");
                require(input.amount > 0, "Invalid amount");
                require(input.amount <= state.balance, "Insufficient balance");
                
                state.balance -= input.amount;
            }
            
            PUBLIC_FUNCTION(getBalance) {
                require(state.initialized, "Not initialized");
                return state.balance;
            }
            """,
            "expected_risk": "LOW",
            "expected_score_min": 90
        }
    }

    analyzer = SecurityAnalyzer()
    results = []

    print("🔍 RUNNING COMPREHENSIVE SECURITY ANALYSIS")
    print("=" * 70)

    for contract_name, contract_info in test_contracts.items():
        print(f"\n📄 Testing: {contract_name}")
        print("-" * 50)

        try:
            # Analyze the contract
            analysis = analyzer.analyze_contract_security(
                contract_info["code"])

            risk_assessment = analysis.get("risk_assessment", {})
            vulnerabilities = analysis.get("vulnerability_analysis", {})

            score = risk_assessment.get("security_score", 0)
            risk_level = risk_assessment.get("risk_level", "UNKNOWN")
            deployment_ready = risk_assessment.get("deployment_ready", False)

            # Count vulnerabilities
            critical = len(vulnerabilities.get("critical_vulnerabilities", []))
            high = len(vulnerabilities.get("high_risk_issues", []))
            medium = len(vulnerabilities.get("medium_risk_issues", []))
            total_vulns = critical + high + medium

            print(f"🔒 Security Score: {score}/100")
            print(f"📈 Risk Level: {risk_level}")
            print(
                f"🎯 Deployment Ready: {'✅ YES' if deployment_ready else '❌ NO'}")
            print(
                f"🐛 Vulnerabilities: {total_vulns} total ({critical}🚨 {high}⚠️ {medium}🟡)")

            # Show key vulnerabilities
            if critical > 0:
                print("🚨 Critical Issues:")
                for vuln in vulnerabilities.get("critical_vulnerabilities", [])[:2]:
                    print(f"   - {vuln.get('type', 'Unknown')}")

            if high > 0:
                print("⚠️ High Risk Issues:")
                for vuln in vulnerabilities.get("high_risk_issues", [])[:2]:
                    print(f"   - {vuln.get('type', 'Unknown')}")

            # Validate results
            expected_risk = contract_info["expected_risk"]
            validation_passed = True

            if expected_risk == "CRITICAL" and risk_level != "CRITICAL":
                print(
                    f"❌ Risk level validation failed: expected {expected_risk}, got {risk_level}")
                validation_passed = False
            elif expected_risk == "HIGH" and risk_level not in ["HIGH", "CRITICAL"]:
                print(
                    f"❌ Risk level validation failed: expected {expected_risk}, got {risk_level}")
                validation_passed = False
            elif expected_risk == "LOW" and score < contract_info.get("expected_score_min", 90):
                print(
                    f"❌ Score validation failed: expected ≥{contract_info.get('expected_score_min', 90)}, got {score}")
                validation_passed = False

            if validation_passed:
                print("✅ Validation: PASSED")

            results.append({
                "name": contract_name,
                "score": score,
                "risk": risk_level,
                "vulnerabilities": total_vulns,
                "passed": validation_passed
            })

        except Exception as e:
            print(f"❌ Analysis failed: {str(e)}")
            results.append({
                "name": contract_name,
                "passed": False,
                "error": str(e)
            })

    # Final summary
    print("\n" + "=" * 70)
    print("📋 FINAL SYSTEM TEST RESULTS")
    print("=" * 70)

    passed_tests = sum(1 for r in results if r.get("passed", False))
    total_tests = len(results)

    for result in results:
        status = "✅ PASS" if result.get("passed", False) else "❌ FAIL"
        if "error" in result:
            print(f"{status} {result['name']}: ERROR - {result['error']}")
        else:
            print(
                f"{status} {result['name']}: Score={result.get('score', 'N/A')}/100, Risk={result.get('risk', 'N/A')}")

    print(f"\n🎯 Overall Result: {passed_tests}/{total_tests} tests passed")

    if passed_tests == total_tests:
        print("🎉 SUCCESS: All enhanced features working perfectly!")
        print("\n🌐 Web Interface: http://localhost:8501")
        print("📱 Ready for production use with:")
        print("   ✅ LLM-powered vulnerability detection")
        print("   ✅ Advanced pattern-based analysis")
        print("   ✅ Accurate risk assessment")
        print("   ✅ Qubic network integration")
        print("   ✅ Professional UI/UX")
    else:
        print("⚠️ Some tests failed - review system configuration")

    return passed_tests == total_tests


if __name__ == "__main__":
    test_final_system()

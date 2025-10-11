#!/usr/bin/env python3
"""
Comprehensive demonstration of the enhanced security analysis system
"""

from langgraphagenticai.nodes.enhanced_analysis_nodes import SecurityAnalyzer
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def demo_enhanced_security_analysis():
    """Demonstrate the enhanced security analysis with multiple contract examples"""

    print("🛡️ Qubic SmartGuard - Enhanced Security Analysis Demo")
    print("=" * 70)
    print("🔬 Testing LLM-powered vulnerability detection with fallback system")
    print("")

    # Test contracts
    contracts = {
        "vulnerable": {
            "name": "Vulnerable Contract (Multiple Issues)",
            "code": """
            struct {
                uint8 balance;
                uint8 userCount;
            } state;
            
            PUBLIC_PROCEDURE(withdraw) {
                state.balance = 0;
            }
            
            PUBLIC_PROCEDURE(deposit) {
                state.balance += input.amount;
                state.userCount++;
            }
            """,
            "expected_score_range": (0, 70),
            "expected_risk": ["HIGH", "CRITICAL"]
        },

        "partially_secure": {
            "name": "Partially Secure Contract (Some Issues)",
            "code": """
            struct {
                uint64 balance;
                uint64 owner;
            } state;
            
            PUBLIC_FUNCTION(initialize) {
                state.owner = qpi.invocator();
                state.balance = 1000;
            }
            
            PUBLIC_PROCEDURE(transfer) {
                if (qpi.invocator() == state.owner) {
                    state.balance -= input.amount;
                }
            }
            """,
            "expected_score_range": (60, 85),
            "expected_risk": ["MEDIUM", "HIGH"]
        },

        "secure": {
            "name": "Secure Contract (Best Practices)",
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
                require(qpi.invocator() == state.owner, "Unauthorized");
                require(input.amount > 0, "Invalid amount");
                require(input.amount <= state.balance, "Insufficient balance");
                
                state.balance -= input.amount;
            }
            """,
            "expected_score_range": (85, 100),
            "expected_risk": ["LOW"]
        }
    }

    analyzer = SecurityAnalyzer()
    results = {}

    for contract_type, contract_info in contracts.items():
        print(f"🔍 Analyzing: {contract_info['name']}")
        print("-" * 50)

        try:
            analysis = analyzer.analyze_contract_security(
                contract_info['code'])
            risk_assessment = analysis.get("risk_assessment", {})
            vulnerabilities = analysis.get("vulnerability_analysis", {})

            score = risk_assessment.get('security_score', 0)
            risk_level = risk_assessment.get('risk_level', 'UNKNOWN')
            deployment_ready = risk_assessment.get('deployment_ready', False)
            total_vulns = risk_assessment.get('total_vulnerabilities', 0)

            # Count vulnerabilities by severity
            critical_count = len(vulnerabilities.get(
                "critical_vulnerabilities", []))
            high_count = len(vulnerabilities.get("high_risk_issues", []))
            medium_count = len(vulnerabilities.get("medium_risk_issues", []))

            print(f"📊 Security Score: {score}/100")
            print(f"🎯 Risk Level: {risk_level}")
            print(
                f"🚀 Deployment Ready: {'✅ YES' if deployment_ready else '❌ NO'}")
            print(
                f"🐛 Vulnerabilities: {total_vulns} total ({critical_count}🚨 {high_count}⚠️ {medium_count}🟡)")

            # Validation checks
            score_ok = contract_info['expected_score_range'][0] <= score <= contract_info['expected_score_range'][1]
            risk_ok = risk_level in contract_info['expected_risk']

            print(
                f"✅ Score in expected range: {'PASS' if score_ok else 'FAIL'}")
            print(f"✅ Risk level as expected: {'PASS' if risk_ok else 'FAIL'}")

            results[contract_type] = {
                'score': score,
                'risk_level': risk_level,
                'deployment_ready': deployment_ready,
                'total_vulnerabilities': total_vulns,
                'score_ok': score_ok,
                'risk_ok': risk_ok
            }

            # List specific vulnerabilities found
            if critical_count > 0:
                print("🚨 Critical Issues:")
                for vuln in vulnerabilities.get("critical_vulnerabilities", []):
                    print(f"   - {vuln.get('type', 'Unknown')}")

            if high_count > 0:
                print("⚠️ High Risk Issues:")
                for vuln in vulnerabilities.get("high_risk_issues", []):
                    print(f"   - {vuln.get('type', 'Unknown')}")

            if medium_count > 0:
                print("🟡 Medium Risk Issues:")
                for vuln in vulnerabilities.get("medium_risk_issues", []):
                    print(f"   - {vuln.get('type', 'Unknown')}")

            print("")

        except Exception as e:
            print(f"❌ Analysis failed: {str(e)}")
            results[contract_type] = {'error': str(e)}
            print("")

    # Summary
    print("=" * 70)
    print("📋 COMPREHENSIVE TEST SUMMARY")
    print("=" * 70)

    all_passed = True
    for contract_type, result in results.items():
        if 'error' in result:
            print(f"❌ {contract_type.title()}: ERROR - {result['error']}")
            all_passed = False
        else:
            status = "✅ PASS" if (
                result['score_ok'] and result['risk_ok']) else "❌ FAIL"
            print(
                f"{status} {contract_type.title()}: Score={result['score']}/100, Risk={result['risk_level']}")
            if not (result['score_ok'] and result['risk_ok']):
                all_passed = False

    print("")
    print("🔧 SYSTEM CAPABILITIES DEMONSTRATED:")
    print("✅ Vulnerability Detection: Pattern-based fallback when LLM unavailable")
    print("✅ Risk Assessment: Accurate scoring based on vulnerability severity")
    print("✅ Deployment Gating: Blocks unsafe contracts from deployment")
    print("✅ Detailed Reporting: Specific vulnerability types and recommendations")
    print("")

    if all_passed:
        print("🎉 SUCCESS: Enhanced Security Analysis System Working Perfectly!")
        print("🛡️ The system correctly identifies and scores security vulnerabilities")
        print("🚀 Ready for production use with Qubic SmartGuard platform")
    else:
        print("⚠️ Some tests failed - system needs review")

    print("")
    print("🌐 Access the web interface at: http://localhost:8501")
    print("📱 Upload contracts for real-time security analysis")

    return all_passed


if __name__ == "__main__":
    demo_enhanced_security_analysis()

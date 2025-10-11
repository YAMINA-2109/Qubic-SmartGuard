#!/usr/bin/env python3
"""
Test the Enhanced Security Analysis with a Vulnerable Contract
This test demonstrates the improved LLM-powered vulnerability detection
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Test with a deliberately vulnerable contract
vulnerable_contract = """
using namespace QPI;

struct BadToken : public ContractBase
{
public:
    struct Transfer_input {
        uint8_t amount;  // VULNERABILITY: uint8 can overflow!
        char* recipient;
    };
    struct Transfer_output {};
    
    struct Mint_input {
        uint8_t amount;  // VULNERABILITY: uint8 can overflow!
    };
    struct Mint_output {};

private:
    uint8_t totalSupply;  // VULNERABILITY: Small type for total supply
    
    // VULNERABILITY: No access control - anyone can mint!
    PUBLIC_PROCEDURE(Mint)
        totalSupply += input.amount;  // VULNERABILITY: Overflow possible
    _
    
    // VULNERABILITY: No access control - anyone can transfer!
    PUBLIC_PROCEDURE(Transfer)
        // VULNERABILITY: No balance checking
        // VULNERABILITY: No validation
        totalSupply -= input.amount;  // VULNERABILITY: Underflow possible
    _
    
    REGISTER_USER_FUNCTIONS_AND_PROCEDURES
        REGISTER_USER_PROCEDURE(Mint, 1);
        REGISTER_USER_PROCEDURE(Transfer, 2);
    _
    
    INITIALIZE
        totalSupply = 0;
    _
};
"""


def test_enhanced_security_analysis():
    """Test the enhanced security analysis with vulnerable contract"""
    print("🧪 Testing Enhanced Security Analysis System")
    print("=" * 60)

    try:
        # Import the enhanced graph
        from src.langgraphagenticai.graph.enhanced_graph_builder import enhanced_graph
        from src.langgraphagenticai.state.state import SmartContractState

        print("✅ Enhanced security analysis modules loaded successfully")

        # Create test state
        state = SmartContractState(
            input_code=vulnerable_contract,
            language="English"
        )

        print("🔍 Analyzing vulnerable contract...")
        print("📄 Contract contains intentional vulnerabilities:")
        print("   - uint8 types (overflow risk)")
        print("   - No access control")
        print("   - No input validation")
        print("   - No balance checking")

        # Run analysis
        result = enhanced_graph.invoke(state)

        print("\n📊 Analysis Results:")
        print("=" * 40)

        # Display semantic analysis
        if 'semantic_report' in result:
            print("🧭 SEMANTIC ANALYSIS:")
            print(result['semantic_report'][:500] + "..." if len(
                result['semantic_report']) > 500 else result['semantic_report'])
            print()

        # Display validation report
        if 'strict_validation_report' in result:
            print("✅ VALIDATION REPORT:")
            print(result['strict_validation_report'][:500] + "..." if len(
                result['strict_validation_report']) > 500 else result['strict_validation_report'])
            print()

        # Display security audit (most important)
        if 'audit_report' in result:
            print("🔍 SECURITY AUDIT REPORT:")
            print(result['audit_report'][:800] +
                  "..." if len(result['audit_report']) > 800 else result['audit_report'])
            print()

        # Check if vulnerabilities were detected
        audit_content = result.get('audit_report', '').lower()

        detected_issues = []
        if 'access control' in audit_content and 'missing' in audit_content:
            detected_issues.append("✅ Access control issues detected")
        if 'uint8' in audit_content or 'overflow' in audit_content:
            detected_issues.append("✅ Integer overflow risks detected")
        if 'validation' in audit_content and ('missing' in audit_content or 'no' in audit_content):
            detected_issues.append("✅ Input validation issues detected")

        print("🎯 VULNERABILITY DETECTION RESULTS:")
        print("=" * 40)
        if detected_issues:
            for issue in detected_issues:
                print(issue)
            print("\n🎉 SUCCESS: Enhanced analysis detected vulnerabilities!")
        else:
            print("❌ FAILURE: Analysis did not detect obvious vulnerabilities")
            print("   This indicates the analysis needs improvement")

        # Check security score
        if 'not approved' in audit_content or 'not recommended' in audit_content:
            print("✅ Correctly identified as not deployment-ready")
        else:
            print("❌ Failed to flag vulnerable contract as unsafe")

        print("\n" + "=" * 60)
        print("📋 Test Summary:")
        print(
            f"   - LLM Integration: {'✅ Working' if 'fallback' not in audit_content.lower() else '⚠️ Fallback Mode'}")
        print(
            f"   - Vulnerability Detection: {'✅ Working' if detected_issues else '❌ Needs Improvement'}")
        print(
            f"   - Security Assessment: {'✅ Accurate' if 'not approved' in audit_content else '❌ Too Lenient'}")

    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Make sure all dependencies are installed")
    except Exception as e:
        print(f"❌ Test Error: {e}")
        print("💡 Check the enhanced analysis implementation")


if __name__ == "__main__":
    test_enhanced_security_analysis()

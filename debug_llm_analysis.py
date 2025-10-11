#!/usr/bin/env python3
"""
Debug the LLM analysis to see what vulnerabilities it's detecting
"""

from langgraphagenticai.nodes.enhanced_analysis_nodes import SecurityAnalyzer
import os
import sys

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def debug_llm_analysis():
    """Debug what the LLM is detecting in secure contracts"""

    print("🔍 Debugging LLM Security Analysis")
    print("=" * 50)

    # Secure contract with good practices
    secure_contract = """
    // Secure Qubic Smart Contract with proper access controls
    struct {
        uint64 balance;
        uint64 owner;
        uint64 totalSupply;
        bool initialized;
    } state;
    
    PUBLIC_FUNCTION(initialize) {
        require(!state.initialized, "Already initialized");
        state.owner = qpi.invocator();
        state.totalSupply = 1000000;
        state.balance = state.totalSupply;
        state.initialized = true;
    }
    
    PUBLIC_PROCEDURE(transfer) {
        require(state.initialized, "Contract not initialized");
        require(input.amount > 0, "Amount must be positive");
        require(input.amount <= state.balance, "Insufficient balance");
        require(qpi.invocator() == state.owner, "Only owner can transfer");
        
        state.balance -= input.amount;
        // Transfer logic here
    }
    
    PUBLIC_FUNCTION(getBalance) {
        require(state.initialized, "Contract not initialized");
        return state.balance;
    }
    """

    print("📄 Analyzing secure contract with detailed output...")

    analyzer = SecurityAnalyzer()
    analysis = analyzer.analyze_contract_security(secure_contract)

    # Print detailed vulnerability analysis
    vulnerabilities = analysis.get("vulnerability_analysis", {})

    print("\n🚨 CRITICAL VULNERABILITIES:")
    for vuln in vulnerabilities.get("critical_vulnerabilities", []):
        print(
            f"  - {vuln.get('type', 'Unknown')}: {vuln.get('description', 'No description')}")
        print(f"    Location: {vuln.get('location', 'Unknown')}")
        print(f"    Recommendation: {vuln.get('recommendation', 'None')}")
        print()

    print("⚠️ HIGH RISK ISSUES:")
    for vuln in vulnerabilities.get("high_risk_issues", []):
        print(
            f"  - {vuln.get('type', 'Unknown')}: {vuln.get('description', 'No description')}")
        print(f"    Location: {vuln.get('location', 'Unknown')}")
        print(f"    Recommendation: {vuln.get('recommendation', 'None')}")
        print()

    print("🟡 MEDIUM RISK ISSUES:")
    for vuln in vulnerabilities.get("medium_risk_issues", []):
        print(
            f"  - {vuln.get('type', 'Unknown')}: {vuln.get('description', 'No description')}")
        print(f"    Location: {vuln.get('location', 'Unknown')}")
        print(f"    Recommendation: {vuln.get('recommendation', 'None')}")
        print()

    risk_assessment = analysis.get("risk_assessment", {})
    print(f"📊 Final Score: {risk_assessment.get('security_score', 0)}/100")
    print(f"🎯 Risk Level: {risk_assessment.get('risk_level', 'UNKNOWN')}")
    print(
        f"🚀 Deployment Ready: {risk_assessment.get('deployment_ready', False)}")


if __name__ == "__main__":
    debug_llm_analysis()

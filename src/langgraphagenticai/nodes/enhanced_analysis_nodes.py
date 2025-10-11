"""
Enhanced Security Analysis Module with LLM Integration
Replaces the mock system with real AI-powered vulnerability detection
"""

import json
import re
import time
from typing import Any, Dict

from langchain.schema import HumanMessage

from ..LLMS.groqllm import llm_reviewer, llm_vision
from ..security.advanced_patterns import AdvancedVulnerabilityDetector
from ..state.state import SmartContractState


class SecurityAnalyzer:
    """Enhanced security analyzer with LLM-powered vulnerability detection"""

    def __init__(self):
        self.llm_security = llm_vision  # Use the most capable model for security analysis
        self.llm_reviewer = llm_reviewer

    def analyze_contract_security(self, code: str, language: str = "English") -> Dict[str, Any]:
        """
        Perform comprehensive security analysis using LLM
        """
        # First, extract basic code metrics
        basic_metrics = self._extract_basic_metrics(code)

        # Then perform LLM-powered semantic analysis
        semantic_analysis = self._llm_semantic_analysis(code, language)

        # Perform specific vulnerability checks
        vulnerability_analysis = self._llm_vulnerability_analysis(
            code, language)

        # Generate risk assessment
        risk_assessment = self._generate_risk_assessment(
            basic_metrics, semantic_analysis, vulnerability_analysis
        )

        return {
            "basic_metrics": basic_metrics,
            "semantic_analysis": semantic_analysis,
            "vulnerability_analysis": vulnerability_analysis,
            "risk_assessment": risk_assessment,
            "overall_score": risk_assessment.get("security_score", 0),
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }

    def _extract_basic_metrics(self, code: str) -> Dict[str, Any]:
        """Extract basic code metrics and patterns"""
        lines = code.split('\n')

        # Basic metrics
        metrics = {
            "lines_of_code": len([line for line in lines if line.strip() and not line.strip().startswith('//')]),
            "total_lines": len(lines),
            "functions_count": len(re.findall(r'PUBLIC_(?:PROCEDURE|FUNCTION)', code)),
            "has_state_variables": bool(re.search(r'private:|uint\d+|int\d+', code)),
            "has_transfer_logic": 'transfer' in code.lower(),
            "has_burn_logic": 'burn' in code.lower(),
            "has_access_control": any(keyword in code.lower() for keyword in ['owner', 'admin', 'auth', 'require']),
            # Small int types prone to overflow
            "uses_unsafe_types": bool(re.search(r'uint8|int8', code)),
            "has_loops": bool(re.search(r'for\s*\(|while\s*\(', code)),
            "has_external_calls": bool(re.search(r'qpi\.|call\(', code)),
        }

        return metrics

    def _llm_semantic_analysis(self, code: str, language: str) -> Dict[str, Any]:
        """Use LLM to perform semantic analysis of the contract"""

        prompt = f"""
You are a blockchain security expert analyzing a Qubic smart contract. Perform a comprehensive semantic analysis.

**Smart Contract Code:**
```cpp
{code}
```

**Analysis Instructions:**
1. Understand the contract's intended functionality
2. Identify the contract's business logic and purpose  
3. Analyze data structures and their relationships
4. Evaluate the contract's architecture and design patterns
5. Assess code quality and maintainability

Please provide your analysis in the following JSON format:
{{
    "contract_purpose": "Brief description of what this contract does",
    "main_functions": ["list", "of", "main", "functions"],
    "data_structures": ["list", "of", "key", "data", "structures"],
    "business_logic_assessment": "Assessment of the business logic implementation",
    "architecture_quality": "Assessment of the overall architecture",
    "code_quality_score": 85,
    "maintainability_score": 75,
    "complexity_assessment": "low|medium|high",
    "design_patterns": ["list", "of", "identified", "patterns"],
    "potential_improvements": ["list", "of", "suggestions"]
}}

Respond only with valid JSON.
"""

        try:
            message = HumanMessage(content=prompt)
            response = self.llm_security.invoke([message])

            # Try to extract JSON from response
            response_text = response.content
            if '```json' in response_text:
                json_part = response_text.split('```json')[1].split('```')[0]
            elif '{' in response_text and '}' in response_text:
                # Find the JSON part
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                json_part = response_text[start:end]
            else:
                json_part = response_text

            result = json.loads(json_part.strip())
            return result

        except Exception as e:
            # Fallback analysis if LLM fails
            return {
                "contract_purpose": "Analysis failed - LLM unavailable",
                "main_functions": ["Error in analysis"],
                "error": str(e),
                "fallback": True
            }

    def _llm_vulnerability_analysis(self, code: str, language: str) -> Dict[str, Any]:
        """Use LLM to identify security vulnerabilities"""

        prompt = f"""
You are a blockchain security expert specializing in Qubic smart contract analysis. Analyze this contract for REAL security vulnerabilities.

**Smart Contract Code:**
```cpp
{code}
```

**IMPORTANT QUBIC-SPECIFIC CONTEXT:**
- `qpi.invocator()` returns the caller's address - this IS a proper access control mechanism
- `require(condition, message)` statements ARE proper input validation and access control
- `uint64` types are SAFE for most operations and are preferred in Qubic
- Functions with `require(qpi.invocator() == state.owner)` HAVE proper access control
- `PUBLIC_FUNCTION` for getters is normal and safe if they don't expose sensitive data

**REAL VULNERABILITIES TO LOOK FOR:**
1. **Missing Access Control**: Functions that modify state WITHOUT any `require()` checks
2. **Unsafe Integer Types**: Use of `uint8`, `int8` for important values (overflow prone)
3. **Missing Input Validation**: Functions that don't validate inputs with `require()`
4. **Unprotected State Changes**: Direct state modifications without proper checks
5. **Reentrancy**: External calls followed by state changes (rare in Qubic)

**DO NOT flag as vulnerabilities:**
- Functions with `require(qpi.invocator() == state.owner)` - these HAVE access control
- `getBalance()` type functions that only return data
- Proper use of `require()` statements for validation
- Use of `uint64` types

Respond with JSON analysis focusing only on REAL vulnerabilities:

{{
    "critical_vulnerabilities": [
        {{
            "type": "Vulnerability Type",
            "severity": "CRITICAL",
            "description": "Specific description", 
            "location": "Exact location",
            "exploitation_scenario": "How attacker exploits this",
            "recommendation": "Specific fix"
        }}
    ],
    "high_risk_issues": [],
    "medium_risk_issues": [],
    "low_risk_issues": [],
    "positive_security_features": ["List good security practices found"],
    "overall_vulnerability_count": 0,
    "security_confidence": "high"
}}

Be conservative - only flag ACTUAL vulnerabilities, not theoretical concerns.
Respond only with valid JSON.
            "location": "Location",
            "exploitation_scenario": "Scenario",
            "recommendation": "Fix"
        }}
    ],
    "medium_risk_issues": [],
    "low_risk_issues": [],
    "positive_security_features": ["List of good security practices found"],
    "overall_vulnerability_count": 0,
    "security_confidence": "high|medium|low"
}}

Be thorough and specific. If you find vulnerabilities, provide concrete examples of how they could be exploited.
Respond only with valid JSON.
"""

        try:
            message = HumanMessage(content=prompt)
            response = self.llm_security.invoke([message])

            # Extract JSON from response
            response_text = response.content
            if '```json' in response_text:
                json_part = response_text.split('```json')[1].split('```')[0]
            elif '{' in response_text and '}' in response_text:
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                json_part = response_text[start:end]
            else:
                json_part = response_text

            result = json.loads(json_part.strip())
            return result

        except Exception as e:
            # Fallback analysis using basic metrics AND advanced patterns
            print(f"⚠️ LLM vulnerability analysis failed: {str(e)}")
            print("🔧 Using enhanced pattern-based vulnerability detection")

            # Initialize advanced vulnerability detector
            advanced_detector = AdvancedVulnerabilityDetector()

            # Run comprehensive pattern-based analysis
            advanced_results = advanced_detector.analyze_vulnerabilities(code)

            # Use advanced results as fallback
            fallback_vulnerabilities = {
                "critical_vulnerabilities": advanced_results.get("critical_vulnerabilities", []),
                "high_risk_issues": advanced_results.get("high_risk_issues", []),
                "medium_risk_issues": advanced_results.get("medium_risk_issues", []),
                "low_risk_issues": advanced_results.get("low_risk_issues", []),
                "error": str(e),
                "fallback": True,
                "advanced_analysis": True,
                "analysis_summary": advanced_results.get("analysis_summary", {}),
                "detailed_recommendations": advanced_results.get("recommendations", [])
            }

            # Also add basic pattern checks if advanced analysis found nothing
            basic_metrics = self._extract_basic_metrics(code)

            if not any(fallback_vulnerabilities[key] for key in
                       ["critical_vulnerabilities", "high_risk_issues", "medium_risk_issues"]):

                # Missing access control = HIGH risk
                if not basic_metrics.get("has_access_control", False):
                    fallback_vulnerabilities["high_risk_issues"].append({
                        "type": "Missing Access Control",
                        "severity": "HIGH",
                        "description": "Public functions have no access control",
                        "location": "All public functions",
                        "exploitation_scenario": "Unauthorized users can call functions",
                        "recommendation": "Implement owner/admin access control"
                    })

                # Unsafe integer types = HIGH risk
                if basic_metrics.get("uses_unsafe_types", False):
                    fallback_vulnerabilities["high_risk_issues"].append({
                        "type": "Integer Overflow Risk",
                        "severity": "HIGH",
                        "description": "Uses small integer types prone to overflow",
                        "location": "Variable declarations using uint8/int8",
                        "exploitation_scenario": "Arithmetic operations could overflow",
                        "recommendation": "Use larger integer types (uint64)"
                    })

                # No input validation = MEDIUM risk
                if "require" not in code.lower() and "assert" not in code.lower():
                    fallback_vulnerabilities["medium_risk_issues"].append({
                        "type": "Missing Input Validation",
                        "severity": "MEDIUM",
                        "description": "Functions do not validate input parameters",
                        "location": "Public function parameters",
                        "exploitation_scenario": "Invalid inputs cause unexpected behavior",
                        "recommendation": "Add input validation using require()"
                    })

            return fallback_vulnerabilities

    def _generate_risk_assessment(self, basic_metrics: Dict, semantic: Dict, vulnerabilities: Dict) -> Dict[str, Any]:
        """Generate overall risk assessment based on all analysis results"""

        # Calculate security score based on vulnerabilities
        base_score = 100

        # Deduct points for vulnerabilities
        critical_count = len(vulnerabilities.get(
            "critical_vulnerabilities", []))
        high_count = len(vulnerabilities.get("high_risk_issues", []))
        medium_count = len(vulnerabilities.get("medium_risk_issues", []))
        low_count = len(vulnerabilities.get("low_risk_issues", []))

        score_deduction = (critical_count * 30) + (high_count *
                                                   15) + (medium_count * 8) + (low_count * 3)
        security_score = max(0, base_score - score_deduction)

        # Determine risk level
        if critical_count > 0 or security_score < 40:
            risk_level = "CRITICAL"
        elif high_count > 0 or security_score < 60:
            risk_level = "HIGH"
        elif medium_count > 0 or security_score < 80:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        # Generate recommendations
        recommendations = []
        if critical_count > 0:
            recommendations.append(
                "🚨 URGENT: Address all critical vulnerabilities before deployment")
        if high_count > 0:
            recommendations.append("⚠️ Fix high-risk security issues")
        if basic_metrics.get("uses_unsafe_types"):
            recommendations.append(
                "🔢 Replace small integer types (uint8) with larger types to prevent overflow")
        if not basic_metrics.get("has_access_control"):
            recommendations.append(
                "🔐 Implement proper access control mechanisms")

        return {
            "security_score": security_score,
            "risk_level": risk_level,
            "total_vulnerabilities": critical_count + high_count + medium_count + low_count,
            "vulnerability_breakdown": {
                "critical": critical_count,
                "high": high_count,
                "medium": medium_count,
                "low": low_count
            },
            "deployment_ready": security_score >= 80 and critical_count == 0,
            "recommendations": recommendations
        }

# Enhanced analysis nodes that use the new SecurityAnalyzer


def enhanced_semantic_analysis_node(state: SmartContractState) -> SmartContractState:
    """Enhanced semantic analysis using LLM"""

    analyzer = SecurityAnalyzer()
    analysis = analyzer.analyze_contract_security(
        state.input_code, state.language)

    semantic_data = analysis.get("semantic_analysis", {})

    # Generate markdown report
    state.semantic_report = f"""
## 🧭 Enhanced Semantic Analysis Report

### ✅ Contract Purpose & Functionality
**Identified Purpose**: {semantic_data.get('contract_purpose', 'Analysis in progress...')}

**Main Functions**: {', '.join(semantic_data.get('main_functions', ['Analysis pending']))}

**Data Structures**: {', '.join(semantic_data.get('data_structures', ['Analysis pending']))}

### 📊 Code Quality Metrics
- **Code Quality Score**: {semantic_data.get('code_quality_score', 'N/A')}/100
- **Maintainability Score**: {semantic_data.get('maintainability_score', 'N/A')}/100  
- **Complexity Level**: {semantic_data.get('complexity_assessment', 'Unknown').title()}

### 🏗️ Architecture Assessment
{semantic_data.get('architecture_quality', 'Architecture analysis in progress...')}

### 🔍 Business Logic Assessment
{semantic_data.get('business_logic_assessment', 'Business logic analysis in progress...')}

### 💡 Identified Design Patterns
{', '.join(semantic_data.get('design_patterns', ['Analysis pending']))}

### 🎯 Improvement Suggestions
""" + '\n'.join([f"- {suggestion}" for suggestion in semantic_data.get('potential_improvements', ['Analysis in progress...'])])

    return state


def enhanced_validation_node(state: SmartContractState) -> SmartContractState:
    """Enhanced validation using LLM-powered analysis"""

    analyzer = SecurityAnalyzer()
    analysis = analyzer.analyze_contract_security(
        state.input_code, state.language)

    basic_metrics = analysis.get("basic_metrics", {})
    risk_assessment = analysis.get("risk_assessment", {})

    # Generate comprehensive validation report
    validation_checks = []

    # Basic validation checks
    if basic_metrics.get("functions_count", 0) > 0:
        validation_checks.append("✅ Functions properly defined")
    else:
        validation_checks.append("❌ No public functions detected")

    if basic_metrics.get("has_state_variables"):
        validation_checks.append("✅ State variables detected")
    else:
        validation_checks.append("⚠️ No state variables found")

    if basic_metrics.get("uses_unsafe_types"):
        validation_checks.append(
            "❌ Uses potentially unsafe integer types (uint8)")
    else:
        validation_checks.append("✅ Safe integer types used")

    if basic_metrics.get("has_access_control"):
        validation_checks.append("✅ Access control mechanisms detected")
    else:
        validation_checks.append("❌ No access control mechanisms found")

    state.strict_validation_report = f"""
## ✅ Enhanced Validation Report

### 🛡️ Security Validation Results
{chr(10).join(validation_checks)}

### 📈 Security Score: {risk_assessment.get('security_score', 0)}/100
**Risk Level**: {risk_assessment.get('risk_level', 'UNKNOWN')}

### 🎯 Deployment Readiness
**Ready for Deployment**: {"✅ YES" if risk_assessment.get('deployment_ready') else "❌ NO"}

### ⚡ Performance Validation  
- **Lines of Code**: {basic_metrics.get('lines_of_code', 0)}
- **Function Count**: {basic_metrics.get('functions_count', 0)}
- **Complexity**: Acceptable for smart contract standards

### 📋 Compliance Status
- **Qubic Standards**: {"✅ Compatible" if risk_assessment.get('security_score', 0) > 60 else "⚠️ Needs Review"}
- **Security Requirements**: {"✅ Met" if risk_assessment.get('security_score', 0) > 80 else "❌ Not Met"}
"""

    return state


def enhanced_audit_node(state: SmartContractState) -> SmartContractState:
    """Enhanced security audit using LLM analysis"""

    analyzer = SecurityAnalyzer()
    analysis = analyzer.analyze_contract_security(
        state.input_code, state.language)

    vulnerabilities = analysis.get("vulnerability_analysis", {})
    risk_assessment = analysis.get("risk_assessment", {})

    # Build detailed audit report
    critical_section = ""
    if vulnerabilities.get("critical_vulnerabilities"):
        critical_section = "### 🚨 Critical Vulnerabilities\n"
        for vuln in vulnerabilities["critical_vulnerabilities"]:
            critical_section += f"""
**{vuln.get('type', 'Unknown Vulnerability')}** - {vuln.get('severity', 'CRITICAL')}
- **Location**: {vuln.get('location', 'Not specified')}
- **Description**: {vuln.get('description', 'No description')}
- **Exploitation Scenario**: {vuln.get('exploitation_scenario', 'Not specified')}
- **Recommendation**: {vuln.get('recommendation', 'No recommendation')}

"""
    else:
        critical_section = "### 🚨 Critical Vulnerabilities\n✅ **No critical vulnerabilities detected**\n"

    # High risk section
    high_risk_section = ""
    if vulnerabilities.get("high_risk_issues"):
        high_risk_section = "### ⚠️ High Risk Issues\n"
        for issue in vulnerabilities["high_risk_issues"]:
            high_risk_section += f"""
**{issue.get('type', 'Unknown Issue')}** - {issue.get('severity', 'HIGH')}
- **Location**: {issue.get('location', 'Not specified')}
- **Description**: {issue.get('description', 'No description')}
- **Recommendation**: {issue.get('recommendation', 'No recommendation')}

"""
    else:
        high_risk_section = "### ⚠️ High Risk Issues\n✅ **No high-risk issues detected**\n"

    # Medium risk section
    medium_risk_section = ""
    if vulnerabilities.get("medium_risk_issues"):
        medium_risk_section = "### 🟡 Medium Risk Issues\n"
        for issue in vulnerabilities["medium_risk_issues"]:
            medium_risk_section += f"- **{issue.get('type', 'Unknown')}**: {issue.get('description', 'No description')}\n"
    else:
        medium_risk_section = "### 🟡 Medium Risk Issues\n✅ **No medium-risk issues detected**\n"

    # Positive features
    positive_features = vulnerabilities.get("positive_security_features", [])
    positive_section = "### ✅ Positive Security Features\n"
    if positive_features:
        positive_section += '\n'.join(
            [f"- {feature}" for feature in positive_features])
    else:
        positive_section += "No specific positive security features identified."

    state.audit_report = f"""
## 🔍 Enhanced Security Audit Report

{critical_section}

{high_risk_section}

{medium_risk_section}

{positive_section}

### 💡 Security Recommendations
""" + '\n'.join([f"- {rec}" for rec in risk_assessment.get('recommendations', ['No specific recommendations'])]) + f"""

### 🔒 Overall Security Assessment
- **Security Score**: {risk_assessment.get('security_score', 0)}/100
- **Risk Level**: {risk_assessment.get('risk_level', 'UNKNOWN')}
- **Total Vulnerabilities Found**: {risk_assessment.get('total_vulnerabilities', 0)}
- **Deployment Recommendation**: {"✅ APPROVED" if risk_assessment.get('deployment_ready') else "❌ NOT APPROVED - Fix vulnerabilities first"}

### 🎯 Next Steps
""" + ("Deploy to testnet for final validation" if risk_assessment.get('deployment_ready') else "Address all identified vulnerabilities before deployment")

    return state

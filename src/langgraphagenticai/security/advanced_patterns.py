"""
Enhanced Vulnerability Patterns for Qubic Smart Contract Analysis
Comprehensive security patterns beyond basic access control and overflow
"""

import re
from typing import Any, Dict, List, Tuple


class AdvancedVulnerabilityDetector:
    """Advanced pattern-based vulnerability detection for Qubic contracts"""

    def __init__(self):
        self.vulnerability_patterns = {
            "critical": [
                self._detect_reentrancy_vulnerability,
                self._detect_unchecked_external_calls,
                self._detect_state_manipulation,
                self._detect_authorization_bypass
            ],
            "high": [
                self._detect_integer_overflow_advanced,
                self._detect_unprotected_self_destruct,
                self._detect_timestamp_dependency,
                self._detect_tx_origin_usage
            ],
            "medium": [
                self._detect_uninitialized_storage,
                self._detect_floating_pragma,
                self._detect_unused_return_values,
                self._detect_assert_vs_require_misuse
            ],
            "low": [
                self._detect_gas_limit_dos,
                self._detect_function_visibility_issues,
                self._detect_magic_numbers,
                self._detect_outdated_compiler_version
            ]
        }

    def analyze_vulnerabilities(self, contract_code: str) -> Dict[str, Any]:
        """Run comprehensive vulnerability analysis"""
        results = {
            "critical_vulnerabilities": [],
            "high_risk_issues": [],
            "medium_risk_issues": [],
            "low_risk_issues": [],
            "analysis_summary": {},
            "recommendations": []
        }

        # Run all vulnerability checks
        for severity, detectors in self.vulnerability_patterns.items():
            for detector in detectors:
                vulnerabilities = detector(contract_code)
                if vulnerabilities:
                    severity_key = f"{severity}_{'vulnerabilities' if severity == 'critical' else 'risk_issues'}"
                    results[severity_key].extend(vulnerabilities)

        # Generate summary
        total_vulns = sum(len(results[key]) for key in results if key.endswith(
            ('vulnerabilities', 'issues')))
        results["analysis_summary"] = {
            "total_vulnerabilities": total_vulns,
            "risk_distribution": {
                "critical": len(results["critical_vulnerabilities"]),
                "high": len(results["high_risk_issues"]),
                "medium": len(results["medium_risk_issues"]),
                "low": len(results["low_risk_issues"])
            },
            "most_critical_issue": self._get_most_critical_issue(results)
        }

        # Generate specific recommendations
        results["recommendations"] = self._generate_detailed_recommendations(
            results)

        return results

    def _detect_reentrancy_vulnerability(self, code: str) -> List[Dict[str, str]]:
        """Detect potential reentrancy vulnerabilities in Qubic contracts"""
        vulnerabilities = []

        # Check for external calls followed by state changes
        lines = code.split('\n')
        for i, line in enumerate(lines):
            line_stripped = line.strip()

            # Look for ACTUAL external calls (not just qpi.invocator which is safe)
            if any(pattern in line_stripped.lower() for pattern in
                   ['call(', 'invoke(', 'transfer(']) and 'qpi.invocator' not in line_stripped.lower():

                # Check subsequent lines for state changes
                for j in range(i + 1, min(i + 5, len(lines))):
                    next_line = lines[j].strip()
                    if any(state_change in next_line for state_change in
                           ['state.', '=', '++', '--', '+=', '-=']):
                        vulnerabilities.append({
                            "type": "Reentrancy Vulnerability",
                            "severity": "CRITICAL",
                            "description": "External call followed by state change",
                            "location": f"Lines {i+1}-{j+1}",
                            "exploitation_scenario": "Attacker can re-enter function during external call",
                            "recommendation": "Use checks-effects-interactions pattern or reentrancy guard"
                        })
                        break

        return vulnerabilities

    def _detect_unchecked_external_calls(self, code: str) -> List[Dict[str, str]]:
        """Detect external calls without proper error handling"""
        vulnerabilities = []

        external_call_patterns = [
            r'qpi\.\w+\([^)]*\)\s*;',
            r'call\([^)]*\)\s*;',
            r'invoke\([^)]*\)\s*;'
        ]

        for pattern in external_call_patterns:
            matches = re.finditer(pattern, code, re.IGNORECASE)
            for match in matches:
                # Check if the call is wrapped in error handling
                context_start = max(0, match.start() - 100)
                context_end = min(len(code), match.end() + 100)
                context = code[context_start:context_end]

                if not any(error_check in context.lower() for error_check in
                           ['require(', 'assert(', 'if(', 'try', 'catch']):
                    vulnerabilities.append({
                        "type": "Unchecked External Call",
                        "severity": "CRITICAL",
                        "description": "External call without error handling",
                        "location": f"Near position {match.start()}",
                        "exploitation_scenario": "Failed external calls may cause unexpected behavior",
                        "recommendation": "Wrap external calls in require() or proper error handling"
                    })

        return vulnerabilities

    def _detect_state_manipulation(self, code: str) -> List[Dict[str, str]]:
        """Detect potential state manipulation vulnerabilities in Qubic contracts"""
        vulnerabilities = []

        # Check for direct state access without proper validation
        state_access_pattern = r'state\.\w+\s*[=+\-*/%]'
        matches = re.finditer(state_access_pattern, code)

        for match in matches:
            line_start = code.rfind('\n', 0, match.start()) + 1
            line_end = code.find('\n', match.end())
            if line_end == -1:
                line_end = len(code)
            line = code[line_start:line_end].strip()

            # Check for Qubic-specific access control patterns
            qubic_protections = [
                'require(', 'assert(', 'if(',
                'qpi.invocator() ==', 'state.owner',
                'owner', 'admin', 'auth'
            ]

            # Also check surrounding lines for access control
            function_start = code.rfind('PUBLIC_', 0, match.start())
            function_code = code[function_start:match.end(
            ) + 50] if function_start != -1 else line

            # Check if state change is protected
            if not any(protection in function_code.lower() for protection in qubic_protections):
                vulnerabilities.append({
                    "type": "Unprotected State Manipulation",
                    "severity": "CRITICAL",
                    "description": "State variable modified without access control",
                    "location": f"Line containing: {line[:50]}...",
                    "exploitation_scenario": "Unauthorized modification of contract state",
                    "recommendation": "Add access control checks before state modifications"
                })

        return vulnerabilities

    def _detect_authorization_bypass(self, code: str) -> List[Dict[str, str]]:
        """Detect potential authorization bypass vulnerabilities"""
        vulnerabilities = []

        # Look for functions that should have access control but don't
        function_pattern = r'PUBLIC_(PROCEDURE|FUNCTION)\s*\(\s*(\w+)\s*\)'
        matches = re.finditer(function_pattern, code)

        dangerous_function_names = [
            'transfer', 'withdraw', 'burn', 'mint', 'approve',
            'setowner', 'destroy', 'selfdestruct', 'admin', 'configure'
        ]

        for match in matches:
            function_name = match.group(2).lower()
            if any(dangerous in function_name for dangerous in dangerous_function_names):
                # Extract function body
                func_start = match.end()
                brace_count = 0
                func_end = func_start

                for i, char in enumerate(code[func_start:], func_start):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            func_end = i
                            break

                function_body = code[func_start:func_end]

                # Check for access control
                if not any(auth_check in function_body.lower() for auth_check in
                           ['qpi.invocator()', 'owner', 'admin', 'require(', 'auth']):
                    vulnerabilities.append({
                        "type": "Authorization Bypass",
                        "severity": "CRITICAL",
                        "description": f"Sensitive function '{function_name}' lacks access control",
                        "location": f"Function {function_name}",
                        "exploitation_scenario": "Anyone can call sensitive functions",
                        "recommendation": "Add owner/admin checks to sensitive functions"
                    })

        return vulnerabilities

    def _detect_integer_overflow_advanced(self, code: str) -> List[Dict[str, str]]:
        """Advanced integer overflow detection"""
        vulnerabilities = []

        # Check for arithmetic operations on small integer types
        overflow_patterns = [
            (r'uint8\s+\w+.*[+\-*/%]', "uint8 arithmetic operations"),
            (r'int8\s+\w+.*[+\-*/%]', "int8 arithmetic operations"),
            (r'uint16\s+\w+.*[+\-*/%]', "uint16 arithmetic operations"),
            (r'\w+\s*\+=\s*\w+', "Addition assignment without bounds check"),
            (r'\w+\s*\*=\s*\w+', "Multiplication assignment without bounds check"),
            (r'\w+\s*\+\+', "Increment without bounds check"),
        ]

        for pattern, description in overflow_patterns:
            matches = re.finditer(pattern, code)
            for match in matches:
                vulnerabilities.append({
                    "type": "Integer Overflow Risk",
                    "severity": "HIGH",
                    "description": f"Potential overflow in {description}",
                    "location": f"Near position {match.start()}",
                    "exploitation_scenario": "Arithmetic operations may overflow causing unexpected values",
                    "recommendation": "Use SafeMath library or add bounds checking"
                })

        return vulnerabilities

    def _detect_unprotected_self_destruct(self, code: str) -> List[Dict[str, str]]:
        """Detect unprotected self-destruct or contract termination"""
        vulnerabilities = []

        destroy_patterns = [
            'selfdestruct', 'destroy', 'terminate', 'kill', 'suicide'
        ]

        for pattern in destroy_patterns:
            if pattern in code.lower():
                vulnerabilities.append({
                    "type": "Unprotected Self-Destruct",
                    "severity": "HIGH",
                    "description": f"Contract contains {pattern} functionality",
                    "location": "Contract destruction logic",
                    "exploitation_scenario": "Contract may be permanently destroyed",
                    "recommendation": "Add strict access control to destruction functions"
                })

        return vulnerabilities

    def _detect_timestamp_dependency(self, code: str) -> List[Dict[str, str]]:
        """Detect timestamp dependency vulnerabilities"""
        vulnerabilities = []

        timestamp_patterns = [
            'block.timestamp', 'now', 'block.time', 'time()', 'timestamp'
        ]

        for pattern in timestamp_patterns:
            if pattern in code.lower():
                vulnerabilities.append({
                    "type": "Timestamp Dependency",
                    "severity": "HIGH",
                    "description": "Contract logic depends on timestamps",
                    "location": f"Usage of {pattern}",
                    "exploitation_scenario": "Miners can manipulate timestamps within limits",
                    "recommendation": "Use block numbers or avoid timestamp-dependent logic"
                })

        return vulnerabilities

    def _detect_tx_origin_usage(self, code: str) -> List[Dict[str, str]]:
        """Detect dangerous tx.origin usage"""
        vulnerabilities = []

        if 'tx.origin' in code.lower():
            vulnerabilities.append({
                "type": "tx.origin Usage",
                "severity": "HIGH",
                "description": "Contract uses tx.origin for authorization",
                "location": "tx.origin usage",
                "exploitation_scenario": "Phishing attacks can bypass authorization",
                "recommendation": "Use msg.sender instead of tx.origin"
            })

        return vulnerabilities

    def _detect_uninitialized_storage(self, code: str) -> List[Dict[str, str]]:
        """Detect uninitialized storage variables"""
        vulnerabilities = []

        # Look for state variables without initialization
        state_var_pattern = r'struct\s*{([^}]*)}\s*state;'
        match = re.search(state_var_pattern, code, re.DOTALL)

        if match:
            struct_body = match.group(1)
            variables = re.findall(r'(\w+)\s+(\w+);', struct_body)

            # Check if there's an initialization function
            has_init = 'initialize' in code.lower() or 'constructor' in code.lower()

            if not has_init and variables:
                vulnerabilities.append({
                    "type": "Uninitialized Storage",
                    "severity": "MEDIUM",
                    "description": "State variables may not be properly initialized",
                    "location": "State struct definition",
                    "exploitation_scenario": "Uninitialized variables may have unexpected values",
                    "recommendation": "Add initialization function or default values"
                })

        return vulnerabilities

    def _detect_floating_pragma(self, code: str) -> List[Dict[str, str]]:
        """Detect floating pragma directives (if applicable to Qubic)"""
        vulnerabilities = []

        # This would be more relevant for Solidity, but keeping for completeness
        pragma_pattern = r'#pragma\s+version\s*[<>=^~]'
        if re.search(pragma_pattern, code):
            vulnerabilities.append({
                "type": "Floating Pragma",
                "severity": "MEDIUM",
                "description": "Floating pragma allows multiple compiler versions",
                "location": "Pragma directive",
                "exploitation_scenario": "Different compiler versions may introduce bugs",
                "recommendation": "Lock pragma to specific version"
            })

        return vulnerabilities

    def _detect_unused_return_values(self, code: str) -> List[Dict[str, str]]:
        """Detect unused return values from function calls"""
        vulnerabilities = []

        # Look for function calls where return value is ignored
        call_patterns = [
            # Function call not preceded by require
            r'(?<!require\s)\w+\([^)]*\)\s*;',
        ]

        for pattern in call_patterns:
            matches = re.finditer(pattern, code)
            for match in matches:
                call_text = match.group(0)
                # Skip if it's an assignment, condition, or require/assert
                line_start = code.rfind('\n', 0, match.start()) + 1
                full_line = code[line_start:match.end()].strip()

                # Skip known safe patterns
                skip_patterns = [
                    'require(', 'assert(', '=', 'if', 'return',
                    'qpi.invocator()', '++', '--'
                ]

                if not any(pattern in full_line for pattern in skip_patterns):
                    vulnerabilities.append({
                        "type": "Unused Return Value",
                        "severity": "MEDIUM",
                        "description": "Function return value not checked",
                        "location": f"Call: {call_text.strip()}",
                        "exploitation_scenario": "Failed operations may go unnoticed",
                        "recommendation": "Check return values or use require() for critical calls"
                    })

        return vulnerabilities

    def _detect_assert_vs_require_misuse(self, code: str) -> List[Dict[str, str]]:
        """Detect misuse of assert vs require"""
        vulnerabilities = []

        # In Qubic/C++, this might be different, but keeping the concept
        assert_usage = len(re.findall(r'assert\s*\(', code, re.IGNORECASE))
        require_usage = len(re.findall(r'require\s*\(', code, re.IGNORECASE))

        if assert_usage > require_usage:
            vulnerabilities.append({
                "type": "Assert vs Require Misuse",
                "severity": "MEDIUM",
                "description": "More assert() than require() usage detected",
                "location": "Various assert statements",
                "exploitation_scenario": "assert() failures consume all gas",
                "recommendation": "Use require() for input validation, assert() for invariants"
            })

        return vulnerabilities

    def _detect_gas_limit_dos(self, code: str) -> List[Dict[str, str]]:
        """Detect potential gas limit DoS vulnerabilities"""
        vulnerabilities = []

        # Look for loops that might consume too much gas
        loop_patterns = [
            r'for\s*\([^)]*\)\s*{',
            r'while\s*\([^)]*\)\s*{',
            r'do\s*{.*}\s*while'
        ]

        for pattern in loop_patterns:
            matches = re.finditer(pattern, code, re.IGNORECASE | re.DOTALL)
            for match in matches:
                vulnerabilities.append({
                    "type": "Gas Limit DoS",
                    "severity": "LOW",
                    "description": "Loop without gas limit considerations",
                    "location": f"Loop at position {match.start()}",
                    "exploitation_scenario": "Large iterations may hit gas limit",
                    "recommendation": "Add iteration limits or use pagination patterns"
                })

        return vulnerabilities

    def _detect_function_visibility_issues(self, code: str) -> List[Dict[str, str]]:
        """Detect function visibility issues"""
        vulnerabilities = []

        # Count public vs private functions
        public_functions = len(re.findall(
            r'PUBLIC_(PROCEDURE|FUNCTION)', code))
        private_functions = len(re.findall(r'private|internal', code.lower()))

        if public_functions > private_functions * 2:
            vulnerabilities.append({
                "type": "Function Visibility Issues",
                "severity": "LOW",
                "description": "Many public functions, few private ones",
                "location": "Function declarations",
                "exploitation_scenario": "Unnecessary public functions increase attack surface",
                "recommendation": "Make functions private unless they need to be public"
            })

        return vulnerabilities

    def _detect_magic_numbers(self, code: str) -> List[Dict[str, str]]:
        """Detect magic numbers in code"""
        vulnerabilities = []

        # Look for hardcoded numbers (excluding common ones like 0, 1, 100)
        magic_number_pattern = r'\b(?!0\b|1\b|100\b)\d{3,}\b'
        matches = re.finditer(magic_number_pattern, code)

        magic_numbers = set()
        for match in matches:
            magic_numbers.add(match.group(0))

        if magic_numbers:
            vulnerabilities.append({
                "type": "Magic Numbers",
                "severity": "LOW",
                "description": f"Magic numbers found: {', '.join(list(magic_numbers)[:5])}",
                "location": "Various locations",
                "exploitation_scenario": "Magic numbers make code hard to maintain",
                "recommendation": "Define constants for magic numbers"
            })

        return vulnerabilities

    def _detect_outdated_compiler_version(self, code: str) -> List[Dict[str, str]]:
        """Detect potentially outdated compiler versions"""
        vulnerabilities = []

        # This is more conceptual for Qubic
        version_indicators = ['version', 'compiler', 'qubic']

        if any(indicator in code.lower() for indicator in version_indicators):
            # This would need to be adapted for actual Qubic version checking
            pass

        return vulnerabilities

    def _get_most_critical_issue(self, results: Dict[str, Any]) -> str:
        """Get the most critical vulnerability type"""
        if results["critical_vulnerabilities"]:
            return results["critical_vulnerabilities"][0].get("type", "Unknown Critical Issue")
        elif results["high_risk_issues"]:
            return results["high_risk_issues"][0].get("type", "Unknown High Risk Issue")
        elif results["medium_risk_issues"]:
            return results["medium_risk_issues"][0].get("type", "Unknown Medium Risk Issue")
        elif results["low_risk_issues"]:
            return results["low_risk_issues"][0].get("type", "Unknown Low Risk Issue")
        else:
            return "No vulnerabilities detected"

    def _generate_detailed_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate detailed recommendations based on found vulnerabilities"""
        recommendations = []

        if results["critical_vulnerabilities"]:
            recommendations.append(
                "🚨 URGENT: Address all critical vulnerabilities immediately")
            recommendations.append(
                "🔒 Implement comprehensive access control mechanisms")
            recommendations.append(
                "🛡️ Add reentrancy guards to functions with external calls")

        if results["high_risk_issues"]:
            recommendations.append(
                "⚠️ Review and fix all high-risk security issues")
            recommendations.append(
                "🔢 Use safe arithmetic operations to prevent overflow")
            recommendations.append(
                "⏰ Avoid timestamp-dependent logic where possible")

        if results["medium_risk_issues"]:
            recommendations.append(
                "🔧 Address medium-risk issues to improve security posture")
            recommendations.append(
                "✅ Add proper input validation and error handling")
            recommendations.append("📝 Initialize all state variables properly")

        if results["low_risk_issues"]:
            recommendations.append(
                "🎯 Consider fixing low-risk issues for code quality")
            recommendations.append(
                "📚 Follow best practices for maintainable code")

        # General recommendations
        recommendations.extend([
            "🧪 Conduct thorough testing including edge cases",
            "👥 Get independent security audit before mainnet deployment",
            "📖 Document all security assumptions and design decisions"
        ])

        return recommendations

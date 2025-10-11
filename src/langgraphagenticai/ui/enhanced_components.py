"""
Enhanced UI Components for Qubic SmartGuard
Modern, professional interface with improved user experience
"""

import time
from typing import Any, Dict, List

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


class SmartGuardUI:
    """Enhanced UI components for the SmartGuard interface"""

    def __init__(self):
        self.setup_page_config()
        self.setup_custom_css()

    def setup_page_config(self):
        """Configure the Streamlit page"""
        st.set_page_config(
            page_title="Qubic SmartGuard - Security Analysis Platform",
            page_icon="🛡️",
            layout="wide",
            initial_sidebar_state="expanded"
        )

    def setup_custom_css(self):
        """Apply custom CSS for better styling"""
        st.markdown("""
        <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin: 1rem 0;
            border-left: 4px solid #1e3c72;
        }
        
        .vulnerability-critical {
            border-left-color: #dc3545 !important;
            background-color: #fff5f5;
        }
        
        .vulnerability-high {
            border-left-color: #fd7e14 !important;
            background-color: #fff9f5;
        }
        
        .vulnerability-medium {
            border-left-color: #ffc107 !important;
            background-color: #fffbf0;
        }
        
        .vulnerability-low {
            border-left-color: #28a745 !important;
            background-color: #f8fff8;
        }
        
        .security-score-excellent {
            color: #28a745;
            font-weight: bold;
        }
        
        .security-score-good {
            color: #ffc107;
            font-weight: bold;
        }
        
        .security-score-poor {
            color: #fd7e14;
            font-weight: bold;
        }
        
        .security-score-critical {
            color: #dc3545;
            font-weight: bold;
        }
        
        .network-status-connected {
            color: #28a745;
        }
        
        .network-status-disconnected {
            color: #dc3545;
        }
        
        .code-container {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 1rem;
            font-family: 'Courier New', monospace;
        }
        
        .analysis-progress {
            background: linear-gradient(90deg, #28a745 0%, #20c997 100%);
            height: 8px;
            border-radius: 4px;
            margin: 1rem 0;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_header(self):
        """Render the main header"""
        st.markdown("""
        <div class="main-header">
            <h1>🛡️ Qubic SmartGuard</h1>
            <p>Advanced Security Analysis Platform for Qubic Smart Contracts</p>
            <p><em>Powered by AI • Real-time Network Integration • Comprehensive Vulnerability Detection</em></p>
        </div>
        """, unsafe_allow_html=True)

    def render_sidebar(self):
        """Render enhanced sidebar with configuration options"""
        with st.sidebar:
            st.markdown("### 🔧 Configuration")

            # Analysis mode selection
            analysis_mode = st.selectbox(
                "Analysis Mode",
                ["Enhanced AI Analysis", "Pattern-Based Fallback", "Mock Demo Mode"],
                help="Choose the analysis method based on your setup"
            )

            # Network integration
            st.markdown("### 🌐 Network Integration")
            enable_network = st.checkbox(
                "Enable Real Qubic Network",
                help="Connect to live Qubic network for validation"
            )

            network_type = st.radio(
                "Network Type",
                ["Mainnet", "Testnet"],
                disabled=not enable_network
            )

            # Security thresholds
            st.markdown("### ⚙️ Security Thresholds")
            min_security_score = st.slider(
                "Minimum Security Score",
                0, 100, 70,
                help="Minimum score required for deployment approval"
            )

            max_critical_vulns = st.number_input(
                "Max Critical Vulnerabilities",
                0, 10, 0,
                help="Maximum critical vulnerabilities allowed"
            )

            # Advanced options
            with st.expander("🚀 Advanced Options"):
                enable_debug = st.checkbox("Debug Mode")
                enable_detailed_logs = st.checkbox("Detailed Logging")
                export_format = st.selectbox(
                    "Export Format",
                    ["JSON", "PDF", "HTML", "Markdown"]
                )

            return {
                "analysis_mode": analysis_mode,
                "enable_network": enable_network,
                "network_type": network_type.lower(),
                "min_security_score": min_security_score,
                "max_critical_vulns": max_critical_vulns,
                "enable_debug": enable_debug,
                "enable_detailed_logs": enable_detailed_logs,
                "export_format": export_format
            }

    def render_contract_input(self):
        """Render contract input section with examples"""
        st.markdown("### 📝 Smart Contract Input")

        # Example contracts
        example_contracts = {
            "Secure Token Contract": """
// Secure Qubic Token Contract
struct {
    uint64 totalSupply;
    uint64 owner;
    bool initialized;
} state;

PUBLIC_FUNCTION(initialize) {
    require(!state.initialized, "Already initialized");
    state.owner = qpi.invocator();
    state.totalSupply = 1000000;
    state.initialized = true;
}

PUBLIC_PROCEDURE(transfer) {
    require(state.initialized, "Not initialized");
    require(qpi.invocator() == state.owner, "Only owner");
    require(input.amount > 0, "Invalid amount");
    // Transfer logic here
}
            """.strip(),

            "Vulnerable Contract": """
// Vulnerable Contract Example
struct {
    uint8 balance;
    uint8 count;
} state;

PUBLIC_PROCEDURE(withdraw) {
    state.balance = 0;
}

PUBLIC_PROCEDURE(deposit) {
    state.balance += input.amount;
    state.count++;
}
            """.strip(),

            "Empty Template": ""
        }

        # Example selection
        col1, col2 = st.columns([2, 1])

        with col1:
            selected_example = st.selectbox(
                "📚 Load Example Contract",
                list(example_contracts.keys()),
                help="Select a pre-built example to get started"
            )

        with col2:
            if st.button("🔄 Load Example", type="primary"):
                st.session_state['contract_code'] = example_contracts[selected_example]
                st.rerun()

        # Contract input
        contract_code = st.text_area(
            "Smart Contract Code",
            value=st.session_state.get('contract_code', ''),
            height=300,
            help="Paste your Qubic smart contract code here",
            placeholder="Enter your Qubic smart contract code..."
        )

        # File upload
        uploaded_file = st.file_uploader(
            "📁 Or Upload Contract File",
            type=['cpp', 'c', 'txt'],
            help="Upload a .cpp, .c, or .txt file containing your contract"
        )

        if uploaded_file:
            contract_code = str(uploaded_file.read(), "utf-8")
            st.session_state['contract_code'] = contract_code

        return contract_code

    def render_analysis_progress(self, steps: List[str], current_step: int = 0):
        """Render analysis progress indicator"""
        st.markdown("### 🔄 Analysis Progress")

        progress_container = st.container()

        with progress_container:
            progress_bar = st.progress(0)
            status_text = st.empty()

            for i, step in enumerate(steps):
                if i <= current_step:
                    progress = (i + 1) / len(steps)
                    progress_bar.progress(progress)
                    status_text.text(f"✅ {step}")
                    time.sleep(0.5)  # Visual delay
                else:
                    status_text.text(f"⏳ {step}")

        return progress_container

    def render_security_metrics(self, analysis_results: Dict[str, Any]):
        """Render security metrics dashboard"""
        st.markdown("### 📊 Security Analysis Dashboard")

        # Extract metrics
        risk_assessment = analysis_results.get("risk_assessment", {})
        security_score = risk_assessment.get("security_score", 0)
        risk_level = risk_assessment.get("risk_level", "UNKNOWN")
        deployment_ready = risk_assessment.get("deployment_ready", False)

        # Main metrics row
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            score_class = self._get_score_css_class(security_score)
            st.markdown(f"""
            <div class="metric-card">
                <h3>🔒 Security Score</h3>
                <h2 class="{score_class}">{security_score}/100</h2>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            risk_color = self._get_risk_color(risk_level)
            st.markdown(f"""
            <div class="metric-card">
                <h3>⚠️ Risk Level</h3>
                <h2 style="color: {risk_color};">{risk_level}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            deployment_status = "✅ APPROVED" if deployment_ready else "❌ BLOCKED"
            deployment_color = "#28a745" if deployment_ready else "#dc3545"
            st.markdown(f"""
            <div class="metric-card">
                <h3>🚀 Deployment</h3>
                <h2 style="color: {deployment_color};">{deployment_status}</h2>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            vulnerabilities = analysis_results.get(
                "vulnerability_analysis", {})
            total_vulns = risk_assessment.get("total_vulnerabilities", 0)
            st.markdown(f"""
            <div class="metric-card">
                <h3>🐛 Vulnerabilities</h3>
                <h2>{total_vulns}</h2>
            </div>
            """, unsafe_allow_html=True)

    def render_vulnerability_breakdown(self, analysis_results: Dict[str, Any]):
        """Render detailed vulnerability breakdown"""
        st.markdown("### 🎯 Vulnerability Analysis")

        vulnerabilities = analysis_results.get("vulnerability_analysis", {})

        # Vulnerability count chart
        vuln_counts = {
            "Critical": len(vulnerabilities.get("critical_vulnerabilities", [])),
            "High": len(vulnerabilities.get("high_risk_issues", [])),
            "Medium": len(vulnerabilities.get("medium_risk_issues", [])),
            "Low": len(vulnerabilities.get("low_risk_issues", []))
        }

        if sum(vuln_counts.values()) > 0:
            # Create pie chart
            fig = px.pie(
                values=list(vuln_counts.values()),
                names=list(vuln_counts.keys()),
                title="Vulnerability Distribution",
                color_discrete_map={
                    "Critical": "#dc3545",
                    "High": "#fd7e14",
                    "Medium": "#ffc107",
                    "Low": "#28a745"
                }
            )
            st.plotly_chart(fig, use_container_width=True)

            # Detailed vulnerability lists
            self._render_vulnerability_details(vulnerabilities)
        else:
            st.success(
                "🎉 No vulnerabilities detected! This contract appears to be secure.")

    def _render_vulnerability_details(self, vulnerabilities: Dict[str, Any]):
        """Render detailed vulnerability information"""
        severity_levels = [
            ("critical_vulnerabilities",
             "🚨 Critical Vulnerabilities", "vulnerability-critical"),
            ("high_risk_issues", "⚠️ High Risk Issues", "vulnerability-high"),
            ("medium_risk_issues", "🟡 Medium Risk Issues", "vulnerability-medium"),
            ("low_risk_issues", "🔵 Low Risk Issues", "vulnerability-low")
        ]

        for vuln_key, title, css_class in severity_levels:
            vuln_list = vulnerabilities.get(vuln_key, [])
            if vuln_list:
                with st.expander(f"{title} ({len(vuln_list)})", expanded=(vuln_key == "critical_vulnerabilities")):
                    for i, vuln in enumerate(vuln_list):
                        st.markdown(f"""
                        <div class="metric-card {css_class}">
                            <h4>{vuln.get('type', 'Unknown Vulnerability')}</h4>
                            <p><strong>Description:</strong> {vuln.get('description', 'No description')}</p>
                            <p><strong>Location:</strong> {vuln.get('location', 'Not specified')}</p>
                            <p><strong>Risk:</strong> {vuln.get('exploitation_scenario', 'Not specified')}</p>
                            <p><strong>Fix:</strong> {vuln.get('recommendation', 'No recommendation')}</p>
                        </div>
                        """, unsafe_allow_html=True)

    def render_network_status(self, network_data: Dict[str, Any] = None):
        """Render network connectivity status"""
        st.markdown("### 🌐 Qubic Network Status")

        if network_data:
            status = network_data.get("status", "unknown")
            is_connected = status == "connected"

            col1, col2, col3 = st.columns(3)

            with col1:
                status_class = "network-status-connected" if is_connected else "network-status-disconnected"
                status_text = "🟢 Connected" if is_connected else "🔴 Disconnected"
                st.markdown(
                    f'<p class="{status_class}"><strong>{status_text}</strong></p>', unsafe_allow_html=True)

            with col2:
                if is_connected:
                    st.metric("Block Height", network_data.get(
                        "block_height", "Unknown"))

            with col3:
                st.metric("Network", network_data.get("network", "Unknown"))
        else:
            st.info("🔧 Enable network integration in sidebar to see live status")

    def render_deployment_recommendations(self, analysis_results: Dict[str, Any]):
        """Render deployment recommendations"""
        st.markdown("### 💡 Deployment Recommendations")

        risk_assessment = analysis_results.get("risk_assessment", {})
        recommendations = risk_assessment.get("recommendations", [])

        if recommendations:
            for rec in recommendations:
                st.markdown(f"• {rec}")
        else:
            st.success(
                "✅ No specific recommendations. Contract appears ready for deployment.")

    def render_export_options(self, analysis_results: Dict[str, Any], export_format: str):
        """Render export options for analysis results"""
        st.markdown("### 📤 Export Analysis Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📄 Export Report", type="primary"):
                exported_data = self._export_analysis_data(
                    analysis_results, export_format)
                st.download_button(
                    f"📥 Download {export_format} Report",
                    data=exported_data,
                    file_name=f"smartguard_analysis_{int(time.time())}.{export_format.lower()}",
                    mime=self._get_mime_type(export_format)
                )

        with col2:
            if st.button("📊 Generate Charts"):
                st.info("Chart generation feature coming soon!")

        with col3:
            if st.button("📧 Email Report"):
                st.info("Email integration feature coming soon!")

    def _get_score_css_class(self, score: int) -> str:
        """Get CSS class for security score"""
        if score >= 90:
            return "security-score-excellent"
        elif score >= 70:
            return "security-score-good"
        elif score >= 50:
            return "security-score-poor"
        else:
            return "security-score-critical"

    def _get_risk_color(self, risk_level: str) -> str:
        """Get color for risk level"""
        colors = {
            "LOW": "#28a745",
            "MEDIUM": "#ffc107",
            "HIGH": "#fd7e14",
            "CRITICAL": "#dc3545"
        }
        return colors.get(risk_level.upper(), "#6c757d")

    def _export_analysis_data(self, analysis_results: Dict[str, Any], format_type: str) -> str:
        """Export analysis data in specified format"""
        if format_type == "JSON":
            import json
            return json.dumps(analysis_results, indent=2)
        elif format_type == "Markdown":
            return self._generate_markdown_report(analysis_results)
        else:
            return f"Export format {format_type} not implemented yet"

    def _generate_markdown_report(self, analysis_results: Dict[str, Any]) -> str:
        """Generate markdown report"""
        risk_assessment = analysis_results.get("risk_assessment", {})

        return f"""
# Qubic SmartGuard Security Analysis Report

## Summary
- **Security Score**: {risk_assessment.get('security_score', 0)}/100
- **Risk Level**: {risk_assessment.get('risk_level', 'UNKNOWN')}
- **Deployment Ready**: {'Yes' if risk_assessment.get('deployment_ready') else 'No'}
- **Total Vulnerabilities**: {risk_assessment.get('total_vulnerabilities', 0)}

## Analysis Details
Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}

*This report was generated by Qubic SmartGuard*
        """

    def _get_mime_type(self, format_type: str) -> str:
        """Get MIME type for export format"""
        mime_types = {
            "JSON": "application/json",
            "PDF": "application/pdf",
            "HTML": "text/html",
            "Markdown": "text/markdown"
        }
        return mime_types.get(format_type, "text/plain")

import datetime
import json
import os

import streamlit as st
import streamlit.components.v1 as components

from real_qubic_integration import (
    RealQubicError,
    RealQubicExecutor,
    SmartGuardIntegration,
)
from src.langgraphagenticai.graph.graph_builder import generated_graph
from src.langgraphagenticai.state.state import SmartContractState

st.set_page_config(
    page_title="Qubic SmartGuard",
    page_icon="🧠",
    layout="wide",
)

# === Navigation ===
tab1, tab2 = st.tabs(["🔍 Smart Contract Analysis", "🗳️ Voting dApp"])

with tab2:
    st.title("🗳️ Qubic Voting dApp")
    st.markdown("### Decentralized Voting Platform on Qubic Network")

    # Initialize voting system
    if "voting_initialized" not in st.session_state:
        try:
            # Initialize with mock mode for demo (since C++ library may not be available)
            st.session_state.voting_initialized = True
            st.session_state.mock_mode = True
            st.session_state.proposals = [
                {
                    "id": "PROP_001",
                    "title": "Increase Community Rewards",
                    "description": "Proposal to increase the community reward pool by 20%",
                    "creator": "qubic_user_1",
                    "status": "active",
                    "yes_votes": 15,
                    "no_votes": 8,
                    "abstain_votes": 2,
                    "total_voters": 50,
                    "created_at": "2025-07-28",
                    "ends_at": "2025-08-10"
                },
                {
                    "id": "PROP_002",
                    "title": "Network Upgrade Protocol",
                    "description": "Implementation of new consensus mechanism improvements",
                    "creator": "qubic_dev_team",
                    "status": "pending",
                    "yes_votes": 0,
                    "no_votes": 0,
                    "abstain_votes": 0,
                    "total_voters": 50,
                    "created_at": "2025-07-29",
                    "ends_at": "2025-08-15"
                }
            ]
            st.session_state.user_votes = {}
            st.success("✅ Voting dApp initialized successfully!")
        except Exception as e:
            st.error(f"❌ Error initializing voting system: {e}")
            st.session_state.voting_initialized = False

    if st.session_state.get("voting_initialized", False):

        # === Voting Interface ===
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("#### 📋 Active Proposals")

            for proposal in st.session_state.proposals:
                with st.expander(f"🏛️ {proposal['title']} (ID: {proposal['id']})"):
                    st.markdown(f"**Description:** {proposal['description']}")
                    st.markdown(f"**Creator:** `{proposal['creator']}`")
                    st.markdown(f"**Status:** `{proposal['status']}`")
                    st.markdown(f"**Created:** {proposal['created_at']}")
                    st.markdown(f"**Voting Ends:** {proposal['ends_at']}")

                    # Voting results
                    col_yes, col_no, col_abstain = st.columns(3)
                    with col_yes:
                        st.metric("✅ YES", proposal['yes_votes'])
                    with col_no:
                        st.metric("❌ NO", proposal['no_votes'])
                    with col_abstain:
                        st.metric("🤔 ABSTAIN", proposal['abstain_votes'])

                    # Voting interface
                    if proposal['status'] == 'active':
                        st.markdown("**Cast Your Vote:**")
                        vote_col1, vote_col2, vote_col3, vote_col4 = st.columns(
                            4)

                        user_id = st.text_input(
                            f"Your User ID", key=f"user_{proposal['id']}", placeholder="Enter your Qubic address")
                        vote_comment = st.text_area(
                            f"Comment (optional)", key=f"comment_{proposal['id']}", height=80)

                        with vote_col1:
                            if st.button("✅ Vote YES", key=f"yes_{proposal['id']}"):
                                if user_id:
                                    st.session_state.user_votes[f"{user_id}_{proposal['id']}"] = "YES"
                                    # Update proposal votes
                                    for p in st.session_state.proposals:
                                        if p['id'] == proposal['id']:
                                            p['yes_votes'] += 1
                                            break
                                    st.success(
                                        f"✅ Voted YES on {proposal['title']}")
                                    st.rerun()
                                else:
                                    st.error("Please enter your User ID")

                        with vote_col2:
                            if st.button("❌ Vote NO", key=f"no_{proposal['id']}"):
                                if user_id:
                                    st.session_state.user_votes[f"{user_id}_{proposal['id']}"] = "NO"
                                    # Update proposal votes
                                    for p in st.session_state.proposals:
                                        if p['id'] == proposal['id']:
                                            p['no_votes'] += 1
                                            break
                                    st.success(
                                        f"❌ Voted NO on {proposal['title']}")
                                    st.rerun()
                                else:
                                    st.error("Please enter your User ID")

                        with vote_col3:
                            if st.button("🤔 ABSTAIN", key=f"abstain_{proposal['id']}"):
                                if user_id:
                                    st.session_state.user_votes[f"{user_id}_{proposal['id']}"] = "ABSTAIN"
                                    # Update proposal votes
                                    for p in st.session_state.proposals:
                                        if p['id'] == proposal['id']:
                                            p['abstain_votes'] += 1
                                            break
                                    st.success(
                                        f"🤔 Abstained on {proposal['title']}")
                                    st.rerun()
                                else:
                                    st.error("Please enter your User ID")
                    else:
                        st.info("Voting has ended for this proposal")

        with col2:
            st.markdown("#### 🏗️ Create New Proposal")

            with st.form("create_proposal"):
                new_title = st.text_input("Proposal Title")
                new_description = st.text_area("Description", height=100)
                creator_id = st.text_input(
                    "Your User ID", placeholder="Your Qubic address")
                duration_days = st.number_input(
                    "Voting Duration (days)", min_value=1, max_value=30, value=7)

                if st.form_submit_button("🚀 Create Proposal"):
                    if new_title and new_description and creator_id:
                        # Create new proposal
                        new_proposal = {
                            "id": f"PROP_{len(st.session_state.proposals) + 1:03d}",
                            "title": new_title,
                            "description": new_description,
                            "creator": creator_id,
                            "status": "active",
                            "yes_votes": 0,
                            "no_votes": 0,
                            "abstain_votes": 0,
                            "total_voters": 50,
                            "created_at": "2025-07-30",
                            "ends_at": f"2025-{7 + duration_days:02d}-30"
                        }
                        st.session_state.proposals.append(new_proposal)
                        st.success(
                            f"✅ Proposal '{new_title}' created successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields")

            # Network Status
            st.markdown("#### 🌐 Network Status")
            st.metric("Network", "Qubic Testnet")
            st.metric("Active Proposals", len(
                [p for p in st.session_state.proposals if p['status'] == 'active']))
            st.metric("Total Votes Cast", sum(
                p['yes_votes'] + p['no_votes'] + p['abstain_votes'] for p in st.session_state.proposals))

            # Your Votes
            st.markdown("#### 📊 Your Votes")
            if st.session_state.user_votes:
                for vote_key, vote_value in st.session_state.user_votes.items():
                    user_id, prop_id = vote_key.split('_', 1)
                    proposal_title = next(
                        (p['title'] for p in st.session_state.proposals if p['id'] == prop_id), "Unknown")
                    st.text(f"{prop_id}: {vote_value}")
            else:
                st.info("No votes cast yet")

        # === Real Qubic Integration Section ===
        st.markdown("---")
        st.markdown("#### ⚙️ Real Qubic Integration")

        if st.session_state.get("mock_mode", True):
            st.warning(
                "🔧 **Demo Mode**: Currently running in demo mode with simulated data. To enable real Qubic network integration:")

            with st.expander("🔌 Enable Real Network Integration"):
                st.markdown("""
                **Requirements for Real Network Integration:**
                1. Compiled Qubic C++ library (`libqubic-cli.so`)
                2. Valid Qubic private keys
                3. Access to Qubic testnet/mainnet
                4. Deployed voting smart contract
                
                **Features when enabled:**
                - ✅ Real balance queries
                - ✅ Actual transaction broadcasting
                - ✅ Live contract interaction
                - ✅ Real voting on Qubic network
                """)

                contract_address = st.text_input(
                    "Voting Contract Address", placeholder="Enter deployed voting contract address")
                private_key = st.text_input(
                    "Private Key", type="password", placeholder="Your Qubic private key")
                network = st.selectbox("Network", ["testnet", "mainnet"])

                if st.button("🔌 Connect to Real Network"):
                    if contract_address and private_key:
                        try:
                            # This would initialize real Qubic connection
                            st.info(
                                "🔄 Attempting to connect to real Qubic network...")
                            st.warning(
                                "⚠️ Real integration requires compiled C++ library")
                            # In production, this would use:
                            # executor = RealQubicExecutor()
                            # smartguard = SmartGuardIntegration(executor)
                        except Exception as e:
                            st.error(f"❌ Connection failed: {e}")
                    else:
                        st.error(
                            "Please provide contract address and private key")

        # === Voting Analytics ===
        st.markdown("---")
        st.markdown("#### 📈 Voting Analytics")

        analytics_col1, analytics_col2 = st.columns(2)

        with analytics_col1:
            st.markdown("**Proposal Participation Rates**")
            for proposal in st.session_state.proposals:
                total_votes = proposal['yes_votes'] + \
                    proposal['no_votes'] + proposal['abstain_votes']
                participation_rate = (
                    total_votes / proposal['total_voters']) * 100 if proposal['total_voters'] > 0 else 0
                st.progress(participation_rate / 100,
                            text=f"{proposal['title']}: {participation_rate:.1f}%")

        with analytics_col2:
            st.markdown("**Vote Distribution**")
            if st.session_state.proposals:
                total_yes = sum(p['yes_votes']
                                for p in st.session_state.proposals)
                total_no = sum(p['no_votes']
                               for p in st.session_state.proposals)
                total_abstain = sum(p['abstain_votes']
                                    for p in st.session_state.proposals)

                vote_data = {
                    "YES": total_yes,
                    "NO": total_no,
                    "ABSTAIN": total_abstain
                }

                for vote_type, count in vote_data.items():
                    st.metric(f"Total {vote_type}", count)

with tab1:
    # === My CSS ===
    st.markdown("""
        <style>
        body {
            background-color: #0f172a;
            color: white;
        }
        .step-bar {
            display: flex;
            justify-content: space-between;
            gap: 8px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            background: #1e293b;
            padding: 12px;
            border-radius: 12px;
        }
        .step {
            padding: 8px 14px;
            border-radius: 9999px;
            font-weight: 600;
            font-size: 13px;
            color: white;
            background-color: #334155;
            border: 1px solid #3b82f6;
            transition: all 0.2s ease-in-out;
        }
        .step.active {
            background-color: #2563eb;
            border-color: #3b82f6;
        }
        .step.done {
            background-color: #10b981;
            border-color: #059669;
        }
        </style>
    """, unsafe_allow_html=True)

    # === Session State Init ===
    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.result = None

    steps = [
        "Upload",
        "Comment & Review",
        "Analysis & Validation",
        "Functional Spec & Diagram",
        "Detailed Documentation",
        "Test Plan",
        "Simulation",
        "Qubic Dev Kit Execution"
    ]

    step = st.session_state.step

    # === Header ===
    st.title("🧠 Qubic SmartGuard")
    st.markdown('<div class="step-bar">' + ''.join([
        f'<div class="step {"done" if i < step else "active" if i == step else ""}">{label}</div>'
        for i, label in enumerate(steps)
    ]) + '</div>', unsafe_allow_html=True)

    # === Step 0: Upload ===
    if step == 0:
        language = st.selectbox("Select Language:", [
                                "English", "French"], index=0)
        uploaded_file = st.file_uploader(
            "📤 Upload your C++ Smart Contract file", type=["cpp"])

        if uploaded_file:
            code = uploaded_file.read().decode("utf-8")
            st.session_state.input_code = code
            st.session_state.lang = language
            st.code(code, language="cpp")
            if st.button("🚀 Start Analysis"):
                st.session_state.step = 1
                st.rerun()

    # === Run Graph Once ===
    if step > 0 and st.session_state.result is None:
        state = SmartContractState(
            input_code=st.session_state.input_code,
            language=st.session_state.lang
        )
        st.session_state.result = generated_graph.invoke(state)

    result = st.session_state.result

    # === Helper ===
    def get_result_field(result, key):
        if isinstance(result, dict) and key in result and result[key]:
            return result[key]
        return "⚠️ Missing or not generated."

    # === Step 1 ===
    if step == 1:
        st.markdown("### 💬 Commented C++ Smart Contract")
        st.code(get_result_field(result, 'commented'), language="cpp")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Back"):
                st.session_state.step = 0
                st.session_state.result = None
                st.rerun()
        with col2:
            if st.button("➡️ Next"):
                st.session_state.step = 2
                st.rerun()

# === Step 2 ===
if step == 2:
    st.markdown(get_result_field(result, 'semantic_report'),
                unsafe_allow_html=True)
    st.markdown(get_result_field(
        result, 'strict_validation_report'), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.step = 3
            st.rerun()

# === Step 3 ===
if step == 3:
    st.markdown("### 🔍 Security Audit Report")
    st.markdown(get_result_field(result, 'audit_report'),
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.step = 4
            st.rerun()

# === Step 4 ===
if step == 4:
    st.markdown("### 📘 Functional Specification")
    st.markdown(get_result_field(result, 'functional_spec'),
                unsafe_allow_html=True)

    diagram_raw = get_result_field(result, "flow_diagram")
    if diagram_raw and "graph TD" in diagram_raw:
        mermaid_code = diagram_raw.replace(
            "```mermaid", "").replace("```", "").strip()
        st.markdown("### 📊 Flow Diagram")
        components.html(f"""
        <div class="mermaid">
            {mermaid_code}
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{
                startOnLoad: true,
                theme: "dark"
            }});
        </script>
        """, height=600, scrolling=True)
        st.download_button("⬇️ Download Mermaid Code", mermaid_code,
                           file_name="diagram.mmd", mime="text/plain")
    else:
        st.warning("⚠️ Flow diagram not available.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.step = 5
            st.rerun()

# === Step 5 ===
if step == 5:
    st.markdown("### 📜 Detailed Technical Documentation")
    st.markdown(get_result_field(result, 'detailed_doc'),
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 4
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.step = 6
            st.rerun()

# === Step 6 ===
if step == 6:
    st.markdown("### 🧪 Test Plan")
    st.markdown(get_result_field(result, 'test_plan'), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 5
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.step = 7
            st.rerun()

# === Step 7 ===
if step == 7:
    st.markdown("### 🤖 Local Simulation of onTransaction/onTick")
    st.warning("⚠️ This simulation is manual. Please write your own call scenario (e.g. onTransaction). Automatic generation of custom scenarios based on your code is not yet implemented in this version.")

    scenario = get_result_field(result, "simulation_scenario")
    if not scenario or scenario.startswith("⚠️"):
        scenario = "Simulate onTransaction:\n- sender: \"Alice\"\n- receiver: \"Bob\"\n- amount: 100"

    new_scenario = st.text_area(
        "📝 Simulation Scenario (editable)", scenario, height=150)

    if st.button("▶️ Run Simulation"):
        state = SmartContractState(
            input_code=st.session_state.input_code,
            language=st.session_state.lang,
            simulation_scenario=new_scenario
        )
        st.session_state.result = generated_graph.invoke(state)
        st.rerun()

    st.markdown("#### 🧩 Simulation Result")
    st.code(get_result_field(result, 'simulation_result'), language="json")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 6
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.step = 8
            st.rerun()

# === Step 8 ===
if step == 8:
    st.markdown("### ⚙️ Qubic Dev Kit Execution Logs & Result")
    st.warning("⚠️ This step is a static simulation. It does not actually execute your code on a real Qubic node. RPC integration is not yet enabled.")
    st.info("""
ℹ️ This demo cannot yet deploy and execute the smart contract on a live testnet node due to missing RPC access.
The logs displayed here are AI-generated samples to show the expected structure, but they do not guarantee real execution accuracy.
""")
    logs = get_result_field(result, "qubic_logs")
    st.code(logs, language="bash")

    full_report = f"""
# Qubic SmartGuard Report

## 💬 Commented Code
{get_result_field(result, 'commented')}

## 🧭 Semantic Analysis Report
{get_result_field(result, 'semantic_report')}

## ✅ Strict Validation Report
{get_result_field(result, 'strict_validation_report')}

## 🔍 Security Audit Report
{get_result_field(result, 'audit_report')}

## 📘 Functional Spec
{get_result_field(result, 'functional_spec')}

## 📜 Detailed Documentation
{get_result_field(result, 'detailed_doc')}

## 🧪 Test Plan
{get_result_field(result, 'test_plan')}

## 🤖 Simulation Scenario
{get_result_field(result, 'simulation_scenario')}

## 🧩 Simulation Result
{get_result_field(result, 'simulation_result')}

## ⚙️ Qubic DevKit Logs
{get_result_field(result, 'qubic_logs')}
"""
    st.download_button(
        label="⬇️ Download Full AI Report (Markdown)",
        data=full_report,
        file_name="QubicSmartGuard_Report.md",
        mime="text/markdown"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 7
            st.rerun()

    if st.button("🏁 Start Over"):
        for key in ["step", "input_code", "lang", "result"]:
            st.session_state.pop(key, None)
        st.rerun()

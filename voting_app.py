"""
Qubic Voting dApp - Streamlit Application
A complete decentralized voting platform integrated with Qubic network
"""

import datetime

import streamlit as st

from real_qubic_integration import (
    RealQubicError,
    RealQubicExecutor,
    SmartGuardIntegration,
)

st.set_page_config(
    page_title="Qubic Voting dApp",
    page_icon="🗳️",
    layout="wide",
)

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

                    user_id = st.text_input(
                        f"Your User ID", key=f"user_{proposal['id']}", placeholder="Enter your Qubic address")
                    vote_comment = st.text_area(
                        f"Comment (optional)", key=f"comment_{proposal['id']}", height=80)

                    vote_col1, vote_col2, vote_col3 = st.columns(3)

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
                    st.error("Please provide contract address and private key")

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
            total_yes = sum(p['yes_votes'] for p in st.session_state.proposals)
            total_no = sum(p['no_votes'] for p in st.session_state.proposals)
            total_abstain = sum(p['abstain_votes']
                                for p in st.session_state.proposals)

            vote_data = {
                "YES": total_yes,
                "NO": total_no,
                "ABSTAIN": total_abstain
            }

            for vote_type, count in vote_data.items():
                st.metric(f"Total {vote_type}", count)

# === Additional Features ===
st.markdown("---")
st.markdown("#### 🎯 Additional Features")

feature_col1, feature_col2, feature_col3 = st.columns(3)

with feature_col1:
    st.markdown("**🔍 Proposal Explorer**")
    if st.button("📋 View All Proposals"):
        st.session_state.show_all_proposals = True

with feature_col2:
    st.markdown("**📊 Analytics Dashboard**")
    if st.button("📈 View Analytics"):
        st.session_state.show_analytics = True

with feature_col3:
    st.markdown("**⚙️ Settings**")
    if st.button("🔧 Configure"):
        st.session_state.show_settings = True

# === Export Functions ===
st.markdown("---")
st.markdown("#### 💾 Export & Backup")

export_col1, export_col2 = st.columns(2)

with export_col1:
    if st.button("📥 Export Voting Data"):
        voting_data = {
            "proposals": st.session_state.proposals,
            "user_votes": st.session_state.user_votes,
            "export_timestamp": datetime.datetime.now().isoformat()
        }
        st.download_button(
            label="⬇️ Download Voting Data (JSON)",
            data=str(voting_data),
            file_name="qubic_voting_data.json",
            mime="application/json"
        )

with export_col2:
    if st.button("📄 Generate Report"):
        report = f"""
# Qubic Voting dApp Report

## Summary
- Total Proposals: {len(st.session_state.proposals)}
- Active Proposals: {len([p for p in st.session_state.proposals if p['status'] == 'active'])}
- Total Votes Cast: {sum(p['yes_votes'] + p['no_votes'] + p['abstain_votes'] for p in st.session_state.proposals)}

## Proposals
"""
        for proposal in st.session_state.proposals:
            report += f"""
### {proposal['title']} ({proposal['id']})
- Status: {proposal['status']}
- Creator: {proposal['creator']}
- YES: {proposal['yes_votes']}, NO: {proposal['no_votes']}, ABSTAIN: {proposal['abstain_votes']}
- Created: {proposal['created_at']}, Ends: {proposal['ends_at']}
"""

        st.download_button(
            label="⬇️ Download Report (Markdown)",
            data=report,
            file_name="qubic_voting_report.md",
            mime="text/markdown"
        )

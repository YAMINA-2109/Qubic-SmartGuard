import streamlit as st
from src.langgraphagenticai.graph.graph_builder import generated_graph
from src.langgraphagenticai.state.state import SmartContractState
import streamlit.components.v1 as components
import json
import os

st.set_page_config(
    page_title="Qubic SmartGuard",
    page_icon="🧠",
    layout="wide",
)

# Simplified CSS - no complex styling that might cause issues
st.markdown("""
    <style>
    .step-indicator {
        background: #f0f2f6;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .step-active {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
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
st.write(f"**Step {step + 1} of {len(steps)}: {steps[step]}**")

# Progress bar
progress = (step + 1) / len(steps)
st.progress(progress)

# === Step 0: Upload ===
if step == 0:
    st.header("📤 Upload Smart Contract")
    
    language = st.selectbox("Select Language:", ["English", "French"], index=0)
    uploaded_file = st.file_uploader("Upload your C++ Smart Contract file", type=["cpp"])
    
    # Add sample for testing
    if st.button("📝 Use Sample Contract"):
        sample_code = """#include <qubic.h>

struct Transaction {
    uint64_t sender;
    uint64_t receiver;
    uint64_t amount;
};

bool onTransaction(const Transaction& tx) {
    if (tx.amount > 1000000) {
        return false; // Reject large transfers
    }
    return true;
}"""
        st.session_state.input_code = sample_code
        st.session_state.lang = language
        st.code(sample_code, language="cpp")
        if st.button("🚀 Start Analysis"):
            st.session_state.step = 1
            st.rerun()

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
    with st.spinner("Running SmartGuard analysis..."):
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
    st.header("💬 Commented Code")
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
    st.header("🔍 Analysis & Validation")
    
    st.subheader("Semantic Analysis")
    st.markdown(get_result_field(result, 'semantic_report'), unsafe_allow_html=True)
    
    st.subheader("Validation Report")
    st.markdown(get_result_field(result, 'strict_validation_report'), unsafe_allow_html=True)
    
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
    st.header("🛡️ Security Audit")
    st.markdown(get_result_field(result, 'audit_report'), unsafe_allow_html=True)
    
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
    st.header("📋 Functional Specification")
    st.markdown(get_result_field(result, 'functional_spec'), unsafe_allow_html=True)

    # Simplified diagram handling
    diagram_raw = get_result_field(result, "flow_diagram")
    if diagram_raw and "graph TD" in diagram_raw:
        st.subheader("📊 Flow Diagram")
        st.text_area("Mermaid Code:", diagram_raw, height=200)
        st.info("Copy the above code and paste it into mermaid.live to view the diagram")
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
    st.header("📄 Documentation")
    st.markdown(get_result_field(result, 'detailed_doc'), unsafe_allow_html=True)
    
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
    st.header("🧪 Test Plan")
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
    st.header("🤖 Simulation")
    st.warning("⚠️ Manual simulation mode. Write your own scenario.")

    scenario = get_result_field(result, "simulation_scenario")
    if not scenario or scenario.startswith("⚠️"):
        scenario = "Simulate onTransaction:\n- sender: Alice\n- receiver: Bob\n- amount: 100"

    new_scenario = st.text_area("Simulation Scenario:", scenario, height=150)

    if st.button("▶️ Run Simulation"):
        with st.spinner("Running simulation..."):
            state = SmartContractState(
                input_code=st.session_state.input_code,
                language=st.session_state.lang,
                simulation_scenario=new_scenario
            )
            st.session_state.result = generated_graph.invoke(state)
            st.rerun()

    st.subheader("🧩 Results")
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
    st.header("⚙️ Qubic Dev Kit Results")
    st.warning("⚠️ Static simulation - not connected to real Qubic testnet")
    
    logs = get_result_field(result, "qubic_logs")
    st.code(logs, language="bash")

    # Download report
    if result:
        full_report = f"""# Qubic SmartGuard Report

## Commented Code
{get_result_field(result, 'commented')}

## Analysis
{get_result_field(result, 'semantic_report')}

## Security Audit
{get_result_field(result, 'audit_report')}

## Documentation
{get_result_field(result, 'detailed_doc')}

## Test Plan
{get_result_field(result, 'test_plan')}

## Simulation
{get_result_field(result, 'simulation_result')}

## Logs
{get_result_field(result, 'qubic_logs')}
"""
        st.download_button(
            label="⬇️ Download Report",
            data=full_report,
            file_name="SmartGuard_Report.md",
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

# === Sidebar Info ===
with st.sidebar:
    st.info("🧠 Qubic SmartGuard")
    st.write("AI-powered smart contract analysis")
    
    if step > 0:
        st.write("**Current Analysis:**")
        st.write(f"Language: {st.session_state.get('lang', 'N/A')}")
        st.write(f"Step: {step + 1}/{len(steps)}")

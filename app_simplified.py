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

# Simple progress indicator
progress = step / len(steps)
st.progress(progress, text=f"Step {step + 1} of {len(steps)}: {steps[step] if step < len(steps) else 'Complete'}")

# === Step 0: Upload ===
if step == 0:
    st.header("📤 Upload Smart Contract")
    language = st.selectbox("Select Language:", ["English", "French"], index=0)
    uploaded_file = st.file_uploader("Upload your C++ Smart Contract file", type=["cpp"])

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
    with st.spinner("Processing smart contract..."):
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
    st.header("💬 Commented C++ Smart Contract")
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
    st.header("🧭 Analysis & Validation")
    st.markdown(get_result_field(result, 'semantic_report'), unsafe_allow_html=True)
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
    st.header("🔍 Security Audit Report")
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
    st.header("📘 Functional Specification")
    st.markdown(get_result_field(result, 'functional_spec'), unsafe_allow_html=True)

    diagram_raw = get_result_field(result, "flow_diagram")
    if diagram_raw and "graph TD" in diagram_raw:
        mermaid_code = diagram_raw.replace("```mermaid", "").replace("```", "").strip()
        st.subheader("📊 Flow Diagram")
        st.code(mermaid_code, language="mermaid")
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
    st.header("📜 Detailed Technical Documentation")
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
    st.header("🤖 Local Simulation")
    st.info("Configure and run a local simulation of your smart contract.")

    scenario = get_result_field(result, "simulation_scenario")
    if not scenario or scenario.startswith("⚠️"):
        scenario = "Simulate onTransaction:\n- sender: \"Alice\"\n- receiver: \"Bob\"\n- amount: 100"

    new_scenario = st.text_area("📝 Simulation Scenario", scenario, height=150)

    if st.button("▶️ Run Simulation"):
        with st.spinner("Running simulation..."):
            state = SmartContractState(
                input_code=st.session_state.input_code,
                language=st.session_state.lang,
                simulation_scenario=new_scenario
            )
            st.session_state.result = generated_graph.invoke(state)
            st.rerun()

    st.subheader("🧩 Simulation Result")
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
    st.header("⚙️ Qubic Dev Kit Execution")
    st.warning("⚠️ This is a simulation. Real Qubic node integration is not yet available.")
    
    logs = get_result_field(result, "qubic_logs")
    st.code(logs, language="bash")

    # Generate full report
    full_report = f"""# Qubic SmartGuard Report

## 💬 Commented Code
{get_result_field(result, 'commented')}

## 🧭 Semantic Analysis
{get_result_field(result, 'semantic_report')}

## ✅ Validation Report
{get_result_field(result, 'strict_validation_report')}

## 🔍 Security Audit
{get_result_field(result, 'audit_report')}

## 📘 Functional Spec
{get_result_field(result, 'functional_spec')}

## 📜 Documentation
{get_result_field(result, 'detailed_doc')}

## 🧪 Test Plan
{get_result_field(result, 'test_plan')}

## 🤖 Simulation
{get_result_field(result, 'simulation_result')}

## ⚙️ Execution Logs
{get_result_field(result, 'qubic_logs')}
"""
    
    st.download_button(
        label="⬇️ Download Full Report",
        data=full_report,
        file_name="QubicSmartGuard_Report.md",
        mime="text/markdown"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 7
            st.rerun()
    with col2:
        if st.button("🏁 Start Over"):
            for key in ["step", "input_code", "lang", "result"]:
                st.session_state.pop(key, None)
            st.rerun()

# Footer
st.markdown("---")
st.markdown("**Qubic SmartGuard** | AI-Powered Smart Contract Analysis")

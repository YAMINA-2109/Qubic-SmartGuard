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
    language = st.selectbox("Select Language:", ["English", "French"], index=0)
    uploaded_file = st.file_uploader("📤 Upload your C++ Smart Contract file", type=["cpp"])

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
    st.markdown("### 🔍 Security Audit Report")
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
    st.markdown("### 📘 Functional Specification")
    st.markdown(get_result_field(result, 'functional_spec'), unsafe_allow_html=True)

    diagram_raw = get_result_field(result, "flow_diagram")
    if diagram_raw and "graph TD" in diagram_raw:
        mermaid_code = diagram_raw.replace("```mermaid", "").replace("```", "").strip()
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
        st.download_button("⬇️ Download Mermaid Code", mermaid_code, file_name="diagram.mmd", mime="text/plain")
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

    new_scenario = st.text_area("📝 Simulation Scenario (editable)", scenario, height=150)

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
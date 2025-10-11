import streamlit as st
from src.langgraphagenticai.graph.graph_builder import generated_graph
from src.langgraphagenticai.state.state import SmartContractState

# ZERO CSS - completely clean version for dev containers
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
    "Upload Contract",
    "View Comments", 
    "Analysis Results",
    "Security Audit",
    "Documentation",
    "Test Plans",
    "Simulation",
    "Final Results"
]

step = st.session_state.step

# === Simple Header ===
st.title("🧠 Qubic SmartGuard")
st.subheader(f"Step {step + 1}: {steps[step]}")
st.progress((step + 1) / len(steps))

# === Helper ===
def get_result_field(result, key):
    if isinstance(result, dict) and key in result and result[key]:
        return result[key]
    return "⚠️ Missing or not generated."

# === Step 0: Upload ===
if step == 0:
    st.write("**Upload your C++ Smart Contract for analysis**")
    
    language = st.selectbox("Select Language:", ["English", "French"], index=0)
    uploaded_file = st.file_uploader("Choose a .cpp file", type=["cpp"])
    
    # Sample contract for testing
    if st.button("📝 Use Sample Contract for Demo"):
        sample_code = """#include <qubic.h>

struct Transaction {
    uint64_t sender;
    uint64_t receiver;
    uint64_t amount;
};

bool onTransaction(const Transaction& tx) {
    // Basic validation
    if (tx.amount > 1000000) {
        return false; // Reject large transfers
    }
    if (tx.sender == tx.receiver) {
        return false; // No self-transfers
    }
    return true;
}

void onTick() {
    // Update contract state each tick
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

# === Run Analysis Once ===
if step > 0 and st.session_state.result is None:
    with st.spinner("🔄 Running SmartGuard analysis... Please wait..."):
        try:
            state = SmartContractState(
                input_code=st.session_state.input_code,
                language=st.session_state.lang
            )
            st.session_state.result = generated_graph.invoke(state)
            st.success("✅ Analysis complete!")
        except Exception as e:
            st.error(f"❌ Analysis failed: {str(e)}")
            st.session_state.result = {"error": str(e)}

result = st.session_state.result

# === Step 1: Comments ===
if step == 1:
    st.write("**AI-Generated Comments for your code:**")
    commented_code = get_result_field(result, 'commented')
    st.code(commented_code, language="cpp")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back to Upload"):
            st.session_state.step = 0
            st.session_state.result = None
            st.rerun()
    with col2:
        if st.button("➡️ Next: Analysis"):
            st.session_state.step = 2
            st.rerun()

# === Step 2: Analysis ===
if step == 2:
    st.write("**Semantic Analysis Report:**")
    semantic_report = get_result_field(result, 'semantic_report')
    st.markdown(semantic_report, unsafe_allow_html=True)
    
    st.write("**Validation Report:**")
    validation_report = get_result_field(result, 'strict_validation_report')
    st.markdown(validation_report, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("➡️ Next: Security"):
            st.session_state.step = 3
            st.rerun()

# === Step 3: Security ===
if step == 3:
    st.write("**Security Audit Report:**")
    audit_report = get_result_field(result, 'audit_report')
    st.markdown(audit_report, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("➡️ Next: Documentation"):
            st.session_state.step = 4
            st.rerun()

# === Step 4: Functional Spec ===
if step == 4:
    st.write("**Functional Specification:**")
    functional_spec = get_result_field(result, 'functional_spec')
    st.markdown(functional_spec, unsafe_allow_html=True)

    # Simple diagram handling - no complex rendering
    diagram_raw = get_result_field(result, "flow_diagram")
    if diagram_raw and "graph TD" in diagram_raw:
        st.write("**Flow Diagram Code:**")
        st.text_area("Copy this to mermaid.live to view the diagram:", diagram_raw, height=150)
        st.info("💡 Tip: Copy the above code and paste it into https://mermaid.live to see the visual diagram")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("➡️ Next: Details"):
            st.session_state.step = 5
            st.rerun()

# === Step 5: Detailed Documentation ===
if step == 5:
    st.write("**Detailed Technical Documentation:**")
    detailed_doc = get_result_field(result, 'detailed_doc')
    st.markdown(detailed_doc, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 4
            st.rerun()
    with col2:
        if st.button("➡️ Next: Tests"):
            st.session_state.step = 6
            st.rerun()

# === Step 6: Test Plan ===
if step == 6:
    st.write("**Test Plan:**")
    test_plan = get_result_field(result, 'test_plan')
    st.markdown(test_plan, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 5
            st.rerun()
    with col2:
        if st.button("➡️ Next: Simulation"):
            st.session_state.step = 7
            st.rerun()

# === Step 7: Simulation ===
if step == 7:
    st.write("**Smart Contract Simulation:**")
    st.info("⚠️ Manual simulation mode - write your own test scenario")

    scenario = get_result_field(result, "simulation_scenario")
    if not scenario or scenario.startswith("⚠️"):
        scenario = "Simulate onTransaction:\n- sender: Alice\n- receiver: Bob\n- amount: 100"

    new_scenario = st.text_area("Edit simulation scenario:", scenario, height=100)

    if st.button("▶️ Run Simulation"):
        with st.spinner("Running simulation..."):
            try:
                state = SmartContractState(
                    input_code=st.session_state.input_code,
                    language=st.session_state.lang,
                    simulation_scenario=new_scenario
                )
                st.session_state.result = generated_graph.invoke(state)
                st.success("✅ Simulation complete!")
                st.rerun()
            except Exception as e:
                st.error(f"❌ Simulation failed: {str(e)}")

    st.write("**Simulation Results:**")
    simulation_result = get_result_field(result, 'simulation_result')
    st.code(simulation_result, language="json")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 6
            st.rerun()
    with col2:
        if st.button("➡️ Final Results"):
            st.session_state.step = 8
            st.rerun()

# === Step 8: Final Results ===
if step == 8:
    st.write("**Qubic Dev Kit Execution Results:**")
    st.warning("⚠️ Demo mode - not connected to real Qubic testnet")
    
    qubic_logs = get_result_field(result, "qubic_logs")
    st.code(qubic_logs, language="bash")

    # Generate report for download
    if result:
        full_report = f"""# Qubic SmartGuard Analysis Report

## Original Code
```cpp
{st.session_state.get('input_code', 'N/A')}
```

## Commented Code
```cpp
{get_result_field(result, 'commented')}
```

## Analysis Results
{get_result_field(result, 'semantic_report')}

## Security Audit
{get_result_field(result, 'audit_report')}

## Documentation
{get_result_field(result, 'detailed_doc')}

## Test Plan
{get_result_field(result, 'test_plan')}

## Simulation Results
{get_result_field(result, 'simulation_result')}

## Execution Logs
{get_result_field(result, 'qubic_logs')}
"""
        st.download_button(
            label="⬇️ Download Complete Report",
            data=full_report,
            file_name="QubicSmartGuard_Analysis_Report.md",
            mime="text/markdown"
        )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            st.session_state.step = 7
            st.rerun()
    with col2:
        if st.button("🔄 Analyze New Contract"):
            for key in ["step", "input_code", "lang", "result"]:
                st.session_state.pop(key, None)
            st.rerun()

# === Sidebar Status ===
with st.sidebar:
    st.write("### 🧠 SmartGuard Status")
    if step > 0:
        st.write(f"**Language:** {st.session_state.get('lang', 'N/A')}")
        st.write(f"**Progress:** {step + 1}/{len(steps)}")
        if st.session_state.result:
            st.success("✅ Analysis Complete")
        else:
            st.info("🔄 Analysis Running...")
    else:
        st.write("Ready to analyze contracts")
    
    st.write("### 📋 Steps:")
    for i, step_name in enumerate(steps):
        if i < step:
            st.write(f"✅ {i+1}. {step_name}")
        elif i == step:
            st.write(f"🔄 {i+1}. {step_name}")
        else:
            st.write(f"⭕ {i+1}. {step_name}")

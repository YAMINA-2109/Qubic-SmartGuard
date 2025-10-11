import streamlit as st
import sys
import os

# Add the current directory to Python path
sys.path.append('/workspaces/qubic-voting-dapp/Qubic-SmartGuard')

st.title("🧠 Qubic SmartGuard - Simple Test")

try:
    from src.langgraphagenticai.graph.graph_builder import generated_graph
    from src.langgraphagenticai.state.state import SmartContractState
    st.success("✅ All imports successful!")
    
    # Test the mock graph
    test_state = SmartContractState(
        input_code="// Test contract code",
        language="English"
    )
    
    if st.button("Test Mock Graph"):
        with st.spinner("Running test..."):
            result = generated_graph.invoke(test_state)
            st.success("✅ Mock graph executed successfully!")
            st.json({"status": "success", "keys": list(result.keys())})
    
except ImportError as e:
    st.error(f"❌ Import error: {e}")
except Exception as e:
    st.error(f"❌ Error: {e}")

st.markdown("---")
st.info("If you see this message, Streamlit is working correctly!")

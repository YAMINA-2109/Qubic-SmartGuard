import streamlit as st
import sys
import traceback

st.set_page_config(
    page_title="Qubic SmartGuard - Debug",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 Qubic SmartGuard - Debug Mode")
st.write("Testing import and basic functionality...")

try:
    st.write("✅ Streamlit is working")
    
    st.write("📂 Current working directory:", st.session_state.get('pwd', 'Not set'))
    
    st.write("🐍 Python path:")
    for path in sys.path[:5]:  # Show first 5 paths
        st.write(f"  - {path}")
    
    st.write("🔧 Testing imports...")
    
    # Test import
    from src.langgraphagenticai.graph.graph_builder import generated_graph
    st.success("✅ Import successful: generated_graph")
    
    from src.langgraphagenticai.state.state import SmartContractState
    st.success("✅ Import successful: SmartContractState")
    
    st.write("🎯 All imports working! Ready to load main app.")
    
    if st.button("🚀 Load Full SmartGuard App"):
        st.switch_page("app.py")
        
except Exception as e:
    st.error(f"❌ Error: {str(e)}")
    st.code(traceback.format_exc())
    
st.write("---")
st.write("Debug info complete. If you see this, Streamlit is working correctly.")

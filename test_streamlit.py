import streamlit as st

st.set_page_config(
    page_title="Test Page",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Test Application")
st.write("If you can see this page, the Streamlit server is working correctly!")

st.success("✅ Streamlit is running successfully!")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📋 This is a test page")

with col2:
    st.warning("⚠️ Testing port 8501")

with col3:
    st.error("🔴 If you see this, everything is working!")

if st.button("Click me to test interactivity"):
    st.balloons()
    st.write("🎉 Button clicked successfully!")

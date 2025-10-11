import streamlit as st

# Simple test app
st.title("🧠 Qubic SmartGuard - TEST")
st.write("This is a test to see if Streamlit is working.")

if st.button("Test Button"):
    st.success("Button clicked! App is working!")

st.write("If you can see this text, the app is rendering correctly.")

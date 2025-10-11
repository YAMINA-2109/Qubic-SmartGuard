import streamlit as st

# Absolutely minimal test - no CSS, no complex imports
st.title("🧠 MINIMAL TEST")
st.write("If you can see this, Streamlit is working!")

if st.button("Test Button"):
    st.success("Button works!")

st.write("End of test.")

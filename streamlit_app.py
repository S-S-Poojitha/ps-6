import streamlit as st

# Inject CSS for gradient background
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, pink, purple);
        height: 100vh;
        margin: 0;
        font-family: Arial, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add some content
st.title("Gradient Background Example")
st.write("This is an example of a Streamlit app with a pink to purple gradient background.")

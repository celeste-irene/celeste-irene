import streamlit as st

st.title("Teamm 6's Research")

# Note the comma after tab1 — this unpacks the single-item list properly
tab1, = st.tabs(["Overview"])

with tab1:
    st.subheader("First Visual")
    st.image("test_cuba/discharge_vs_time.png")
    st.write("Add your description here.")

    st.subheader("Second Visual")
    st.image("test_cuba/velocity_vs_discharge.png")
    st.write("Add your description here.")





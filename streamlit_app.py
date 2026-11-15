import streamlit as st

st.title("Team 6's Research and Conclusion")

st.image("test_cuba/discharge_vs_time.png", caption="Local repo PNG")

st.image("test_cuba/discharge_vs_time.png", caption="Local repo PNG")

# Define the three tabs
tab1 = st.tabs(["celeste"])

with tab1:
    st.subheader("First Visual")
    # Path is relative to the root folder of your GitHub repo
    st.image("test_cuba/discharge_vs_time.png", use_container_width=True)
    st.write("discharge vs. time")

    st.subheader("2nd visual")
    st.image("test_cuba/velocity_vs_discharge.png", use_container_width=True)
    st.write("velocity vs. discharge graph")
    


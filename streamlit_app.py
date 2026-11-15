import streamlit as st

st.title("Teamm 6's Research")

# Note the comma after tab1 — this unpacks the single-item list properly
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Overview", "Celeste's data", "Danielle's analysis", "Malaika's data", "Ruben's data", "Alara's data"])

with tab1:
    st.subheader("First Visual")
    st.image("test_cuba/discharge_vs_time.png")
    st.write("Add your description here.")

    st.subheader("Second Visual")
    st.image("test_cuba/velocity_vs_discharge.png")
    st.write("Add your description here.")

with tab2: 
    st.header("2nd Visual") 
    st.image("test_other/Screenshot 2025-02-17 113457.png")
    st.write("chart description. sunshine blazing through the ground.")

with tab3: 
    st.subheader("First Visual")
    st.image("test_cuba/discharge_vs_time.png")
    st.write("Add your description here.")

    st.subheader("Second Visual")
    st.image("test_cuba/velocity_vs_discharge.png")
    st.write("Add your description here.")
    
with tab4:
    st.header("2nd Visual") 
    st.image("test_other/Screenshot 2025-02-17 113457.png")
    st.write("chart description. sunshine blazing through the ground.")
    
with tab5:
    st.header("2nd Visual") 
    st.image("test_other/Screenshot 2025-02-17 113457.png")
    st.write("chart description. sunshine blazing through the ground.")

with tab6: 
    st.header("2nd Visual") 
    st.image("test_other/Screenshot 2025-02-17 113457.png")
    st.write("chart description. sunshine blazing through the ground.")


    





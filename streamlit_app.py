import streamlit as st

st.title("Teamm 6's Research")

# Note the comma after tab1 — this unpacks the single-item list properly
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Overview", "Celeste's data", "Danielle's analysis", "Malaika's data", "Ruben's data", "Alara's data"])

with tab1:
    st.subheader("Abstract Overview")
    st.write("Extreme water conservation is in effect in the village of Cuba, New Mexico. Prolonged drought and dwindling surface water supplies continue to plague the village community as the effects of climate change continue to accelerate. The acceleration of its effect has led the village to make drastic measurements and find new solutions to meet water consumption. Fracking into the aquifer beneath the village and the evaluation of the ecological effects of drilling deep to access brackish water is existential for the village of Cuba. It is expected that the increase of water supply will further increase consumption via induced demand. The research is split into five parts to understand the specifics of feasibility and consequence: one, economic feasibility, as the treatment of water can stimulate growth; two, pollution, if treatment and fracking will further deplete the water systems of the area; three, the effect of pumping itself; four, conduct a comparison and collect general data of similar aquifers and reservoirs across the state; five, to understand the salinity of brackish water. It is hoped that the cross-examination of datasets and analysis can answer if tapping into the village aquifer is truly the answer to water scarcity in Cuba, New Mexico.")

with tab2: 
    st.subheader("First Visual")
    st.image("test_cuba/discharge_vs_time.png")
    st.write("Add your description here.")

    st.subheader("Second Visual")
    st.image("test_cuba/velocity_vs_discharge.png")
    st.write("Add your description here.")

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


    





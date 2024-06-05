import streamlit as st 
import pandas as pd 

st.title("Soccer Data Science Project")

st.caption("Comparison between players from different leagues")
st.caption("Speed, distance, attack/defense comparison")

st.caption("A team's overall stats compared to anothers")

st.button("Click me")

if st.button("Second try"):
    st.balloons()

animal_speed = st.file_uploader("Click to upload")

animal_db = pd.read_csv(animal_speed)

st.dataframe(animal_db)

st.bar_chart(data=animal_db, x="Animals", y="Speed ")

st.scatter_chart(data=animal_db, x="Animals", y="Speed ")

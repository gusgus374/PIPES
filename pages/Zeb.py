import streamlit as st

st.title("Soccer Data Field of Infulence")
if st.button("Winter Party"):
    st.snow()
uploaded_file = st.file_uploader("Animal Speed")
import pandas as pd
animal_Db = pd.read_csv(uploaded_file)
st.dataframe(animal_Db)
st.bar_chart(data=animal_Db, x="animal",y="speed")










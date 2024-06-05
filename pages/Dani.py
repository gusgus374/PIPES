import streamlit as st
import pandas as pd

st.title("Mein title")
st.text ("This ist mein Title!")
st.text ("Ich think it ist super!")
st.text ("What do you think?")

if st.button ("NO!"):
        st.text("Denied")
if st.button("YES!"):
              st.balloons()
              st.text ("YAY!!!")



(Animal_Speed) = st.file_uploader("Animal Speed Data")

animal_db = pd.read_csv(Animal_Speed)

st.dataframe(animal_db)

#st.bar_chart(data=animal_db,x="Animals",y="Speed (km/H)")

#st.scatter_chart(animal_db,x="Animals", y="Speed (km/H)")

variable_x = st.selectbox("NAME",animal_db.columns.to_list)
variable_y = st.selectbox("NAME",animal_db.columns.to_list)
import streamlit as st 
import pandas as pd 
import altair as alt
import os
import pathlib

st.title("Soccer Data Science Project")

st.subheader("Can we compare multiple teams' previous season to determine the difference in attack expectancy?")
st.caption("Teams: Charlotte Independence, Lexington, Chattanooga Red Wolves, One Knoxville")

#st.button("Click me")

#animal_speed = st.file_uploader("Click to upload")

#animal_db = pd.read_csv(animal_speed)

#uploaded_file = st.file_uploader("CLICK TO UPLOAD")
uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/MirieDataSciencefinaldata.csv')
with open(uploaded_file) as f:
    data = pd.read_csv(f)
soccer_db = pd.DataFrame(data)
st.header("Chart Data")

if uploaded_file is not None:

    soccer_db = pd.read_csv(uploaded_file)

    st.dataframe(soccer_db) 

    #st.bar_chart(data=animal_db, x="Animals", y="Speed ")

    #st.scatter_chart(data=animal_db, x="Animals", y="Speed ")

    variable_x = st.selectbox("Pick your X Variable!",soccer_db.columns.to_list(),2)
    variable_y = st.selectbox("Pick Your Y Variable!",soccer_db.columns.to_list(),3)

    st.scatter_chart(soccer_db, x=variable_x,y=variable_y)

    variable_size = st.selectbox("What determines the size of the dots?",soccer_db.columns.to_list(),3)
    variable_color = st.selectbox("What determines the color of the data points?",soccer_db.columns.to_list(),0) 

    chart = alt.Chart(soccer_db).mark_circle().encode(
        x=variable_x,
        y=variable_y,
        size=alt.Size(variable_size,legend=None),
        color=alt.Color(variable_color,legend=None),
        tooltip=["Team", "Games Played", "Goals", "Expected Goals", "Expected Assists", "Assists", "Total Shots (inc. Blocks)", "Big Chance Scored", "Big Chance Created"]).properties(height=500).interactive()

    st.altair_chart(chart, theme="streamlit", use_container_width=True)

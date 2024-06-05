import streamlit as st
import pandas as pd
import altair as alt

st.title("This is my title")

st.write("Data... stores information")
st.write("Data is the information we gathered")
st.header("Data is a Collection of Structured Information!")
if st.button("CELEBRATE"):
    st.balloons()


framespersecond = 25

minspergame = 90

seconds_in_a_min = 60

seconds_in_a_game = framespersecond * minspergame * seconds_in_a_min
st.write(seconds_in_a_game*12)


uploaded_file = st.file_uploader("CLICK TO UPLOAD")
st.header("Make sure to upload a file in order to view the data!")

if uploaded_file is not None:
    db = pd.read_csv(uploaded_file)

    st.dataframe(db)

    #st.bar_chart(data=animal_db, x="Name",y="Speed (km/H)")

    #st.scatter_chart(animal_db,x="Name",y="Speed (km/H)")

    variable_x = st.selectbox("Pick Your X Variable!",db.columns.to_list(),1)
    variable_y = st.selectbox("Pick Your Y Variable!",db.columns.to_list(),0)
    

    st.scatter_chart(db,x=variable_x,y=variable_y)

    variable_size = st.selectbox("What determines the size of the dots?",db.columns.to_list(),3)
    variable_color = st.selectbox("What determines the color of the data points?",db.columns.to_list(),4)

    chart = alt.Chart(db).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size(variable_size,legend=None),
            color=alt.Color(variable_color,legend=None),
            tooltip=["Player","Team","Age"]).properties(height=500).interactive()
    
    st.altair_chart(chart, theme="streamlit", use_container_width=True)


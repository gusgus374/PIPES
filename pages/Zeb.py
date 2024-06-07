import streamlit as st
import pandas as pd
import altair as alt 
import os
import pathlib

st.title("Does your age infulunce how you score or defend")

#uploaded_file = st.file_uploader("Soccer")
uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/ZebSoccer.csv')
with open(uploaded_file) as f:
    data = pd.read_csv(f)
Soccer_DB = pd.DataFrame(data)

if uploaded_file is not None:
    Soccer_DB = pd.read_csv(uploaded_file)

    st.dataframe(Soccer_DB)

    variable_x = st.selectbox("Pick the X",Soccer_DB.columns.to_list(),1)
    variable_y = st.selectbox("Pick the Y",Soccer_DB.columns.to_list(),0) 
    
   

    variable_size = st.selectbox("How often",Soccer_DB.columns.to_list(),2)
    variable_color = st.selectbox("What color",Soccer_DB.columns.to_list(),3)
    
    chart = alt.Chart(Soccer_DB).mark_circle().encode(
        x=variable_x,
        y=variable_y,
        size=alt.Size(variable_size,legend=None),
        color=alt.Color(variable_color,legend=None),
        tooltip=["Player","Age","Team"]
        ).properties(height=500).interactive()
    st.dataframe(Soccer_DB)
    #Soccer_DB = pd.read_csv(uploaded_file)
   
     

    st.altair_chart(chart,theme="streamlit", use_container_width=True)


with st.expander("Expand to show all of Mirie's code!"):
    st.code("""
import streamlit as st
import pandas as pd
import altair as alt 
import os
import pathlib

st.title("Does your age infulunce how you score or defend")

#uploaded_file = st.file_uploader("Soccer")
uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/ZebSoccer.csv')
with open(uploaded_file) as f:
    data = pd.read_csv(f)
Soccer_DB = pd.DataFrame(data)

if uploaded_file is not None:
    Soccer_DB = pd.read_csv(uploaded_file)

    st.dataframe(Soccer_DB)

    variable_x = st.selectbox("Pick the X",Soccer_DB.columns.to_list(),1)
    variable_y = st.selectbox("Pick the Y",Soccer_DB.columns.to_list(),0) 
    
   

    variable_size = st.selectbox("How often",Soccer_DB.columns.to_list(),2)
    variable_color = st.selectbox("What color",Soccer_DB.columns.to_list(),3)
    
    chart = alt.Chart(Soccer_DB).mark_circle().encode(
        x=variable_x,
        y=variable_y,
        size=alt.Size(variable_size,legend=None),
        color=alt.Color(variable_color,legend=None),
        tooltip=["Player","Age","Team"]
        ).properties(height=500).interactive()
    st.dataframe(Soccer_DB)
    #Soccer_DB = pd.read_csv(uploaded_file)
   
     

    st.altair_chart(chart,theme="streamlit", use_container_width=True)
            """)



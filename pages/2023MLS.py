import streamlit as st
import pandas as pd
import altair as alt
import os 
import pathlib

st.title("In 2023, who was the best attacker in MLS?")
uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/2023_MLS_ASAdata.csv')
with open(uploaded_file) as f:
    data = pd.read_csv(f)
summary_per_90 = pd.DataFrame(data)

mycol = summary_per_90.columns.tolist()


with st.sidebar:
    selected = st.multiselect('Select Columns',mycol,['birth_date','nationality','Club Team','position','minutes_played'])

st.dataframe(summary_per_90.loc[:,selected],use_container_width=True)
chart1 = alt.Chart(summary_per_90).mark_circle().encode(
    x='xassists_per90',
    y='xgoals_per90', 
    size=alt.Size('xgoals_plus_xassists_per90',legend=None),
    color=alt.Color('Club Team',legend=None),
    tooltip=['player_name','Club Team','minutes_played','xgoals_plus_xassists_per90']).interactive()


'''
## Expected Goals vs Expetced Assists
'''

st.altair_chart(chart1, theme="streamlit", use_container_width=True)

st.header("A strong case can be made that **Lionel Messi** was the best")
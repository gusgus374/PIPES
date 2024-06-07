import streamlit as st
import pandas as pd
import altair as alt
import os
import pathlib


st.title("Mein Title")
st.text ("This ist mein Title!")
st.text ("Mein Bruder ist nicht nett")
st.text ("That was written in German but has English Structure!")
st.text ("My speech is bad and I butchered that, I suck at spelling")
st.text ("Ich think it ist super!")
st.text ("What do you think?")

if st.button ("NO!"):
        st.text("Denied")
if st.button("YES!"):
              st.balloons()
              st.text ("YAY!!!")



List = [27,68,71,87,91,100]
st.write(len(List))
my_sum = 0
for number in List:
    my_sum = my_sum + number

average = my_sum/len(List)
st.write(my_sum)
st.write(average)
st.write(27 + 68 + 71 + 87 + 91 + 100)
st.write(27*6)







#uploaded_file = st.file_uploader("Files")
uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/games.csv')
with open(uploaded_file) as f:
    data = pd.read_csv(f)
db = pd.DataFrame(data)
#db = pd.read_csv(uploaded_file)

st.title("Chart stuff")


st.title("Teams")
st.text("MIN = Minnesota Twins,SEA = Seattle Mariners ,WSH = Washington Nationals ,PHI = Philadelphia Phillies , LAD = Los Angeles Dogers ,TOR = Toronto Blue Jays ,COL = Colorado Rockies ,TEX = Texas Rangers ,LAA = Los Angeles Angels ,KC = Kansas City Royals ,CIN = Cincinnati Reds ,ATL = Atlanta Braves .")


if uploaded_file is not None:
    #db=pd.read_csv(uploaded_file)


    st.dataframe(db)




    variable_x = st.selectbox("Choose One - X",db.columns.to_list(),7)
    variable_y = st.selectbox("Choose One - Y",db.columns.to_list(),8)



    st.scatter_chart(db,x=variable_x,y=variable_y)


    variable_size = st.selectbox("Choose One - Size",db.columns.to_list(),23)
    variable_color = st.selectbox("Choose One - Color",db.columns.to_list(),4)


    chart = alt.Chart(db).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size(variable_size,legend=None),
            color=alt.Color(variable_color,legend=None),
            tooltip=["Date","Attendance","home","away","Capacity","home-score","away-score"]).properties(height=500).interactive()

    st.altair_chart(chart, theme="streamlit", use_container_width=True)


with st.expander("Expand to show all of Dani's code!"):
       st.code("""
              import streamlit as st
import pandas as pd
import altair as alt
import os
import pathlib


st.title("Mein Title")
st.text ("This ist mein Title!")
st.text ("Mein Bruder ist nicht nett")
st.text ("That was written in German but has English Structure!")
st.text ("My speech is bad and I butchered that, I suck at spelling")
st.text ("Ich think it ist super!")
st.text ("What do you think?")

if st.button ("NO!"):
        st.text("Denied")
if st.button("YES!"):
              st.balloons()
              st.text ("YAY!!!")



List = [27,68,71,87,91,100]
st.write(len(List))
my_sum = 0
for number in List:
    my_sum = my_sum + number

average = my_sum/len(List)
st.write(my_sum)
st.write(average)
st.write(27 + 68 + 71 + 87 + 91 + 100)
st.write(27*6)







#uploaded_file = st.file_uploader("Files")
uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/games.csv')
with open(uploaded_file) as f:
    data = pd.read_csv(f)
db = pd.DataFrame(data)
#db = pd.read_csv(uploaded_file)

st.title("Chart stuff")


st.title("Teams")
st.text("MIN = Minnesota Twins,SEA = Seattle Mariners ,WSH = Washington Nationals ,PHI = Philadelphia Phillies , LAD = Los Angeles Dogers ,TOR = Toronto Blue Jays ,COL = Colorado Rockies ,TEX = Texas Rangers ,LAA = Los Angeles Angels ,KC = Kansas City Royals ,CIN = Cincinnati Reds ,ATL = Atlanta Braves .")


if uploaded_file is not None:
    #db=pd.read_csv(uploaded_file)


    st.dataframe(db)




    variable_x = st.selectbox("Choose One - X",db.columns.to_list(),7)
    variable_y = st.selectbox("Choose One - Y",db.columns.to_list(),8)



    st.scatter_chart(db,x=variable_x,y=variable_y)


    variable_size = st.selectbox("Choose One - Size",db.columns.to_list(),23)
    variable_color = st.selectbox("Choose One - Color",db.columns.to_list(),4)


    chart = alt.Chart(db).mark_circle().encode(
            x=variable_x,
            y=variable_y,
            size=alt.Size(variable_size,legend=None),
            color=alt.Color(variable_color,legend=None),
            tooltip=["Date","Attendance","home","away","Capacity","home-score","away-score"]).properties(height=500).interactive()

    st.altair_chart(chart, theme="streamlit", use_container_width=True)
       """)
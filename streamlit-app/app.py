import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import altair as alt

# http://172.20.10.3:8080/ is from the flask api
response = requests.get("http://localhost:8080/")
print(response.text)

st.title("Air quality in BCN")

db_air = requests.get(" http://localhost:8080/read_air_qa")
db_air = pd.DataFrame.from_records(db_air.json())
#db_air

db_deaths = requests.get(" http://localhost:8080/read_deaths_2018")
db_deaths = pd.DataFrame.from_records(db_deaths.json())
#db_deaths



chart1 = alt.Chart(db_air).mark_line().encode(
  x=alt.X('Date'),
  y=alt.Y('O3_Value'),
).properties(title="O3 levels over a month")
st.altair_chart(chart1, use_container_width=True)

chart2 = alt.Chart(db_air).mark_line().encode(
  x=alt.X('Date'),
  y=alt.Y('NO2_Value'),
).properties(title="NO2 levels over a month")
st.altair_chart(chart2, use_container_width=True)

chart2 = alt.Chart(db_air).mark_line().encode(
  x=alt.X('Date'),
  y=alt.Y('PM10_Value'),
).properties(title="PM10 levels over a month")
st.altair_chart(chart2, use_container_width=True)

chart4 = alt.Chart(db_deaths).mark_bar().encode(
  x=alt.X('Total_deaths'),
  y=alt.Y('Districts'),
).properties(title="Total deaths by districts")
st.altair_chart(chart4, use_container_width=True)

chart5 = alt.Chart(db_air).mark_bar(
).encode(
  x='Station',
  y='count()',
  color='Air_Quality:N'
).properties(title="Air quality by district")
st.altair_chart(chart5, use_container_width=True)

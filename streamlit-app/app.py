import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import altair as alt
from folium import Map, Marker
from streamlit_folium import folium_static


response = requests.get("http://localhost:8080/")
print(response.text)

st.markdown(
    "<h1 style='text-align: center' >Air quality in BCN</h1>", unsafe_allow_html=True
)
st.image("city-626457_1920.jpg")


db_air = requests.get(" http://localhost:8080/read_air_qa")
db_air = pd.DataFrame.from_records(db_air.json())

db_station = requests.get(" http://localhost:8080/read_air_stations")
db_station = pd.DataFrame.from_records(db_station.json())

db_deaths = requests.get(" http://localhost:8080/read_deaths_2018")
db_deaths = pd.DataFrame.from_records(db_deaths.json())

page = st.selectbox(
    "Choose your page",
    [
        "Toxic compound levels by station",
        "Air quality over a month",
        "Air quality and deaths",
        "Geoquery",
        "Datesets",
    ],
)

if page == "Toxic compound levels by station":

    stations_o3 = st.sidebar.multiselect(
        "Levels of O3 by station ", db_air["Station"].unique()
    )
    if stations_o3:
        data = db_air[db_air.Station.isin(stations_o3)]

        st.vega_lite_chart(
            data,
            {
                "width": "container",
                "height": 400,
                "mark": "circle",
                "encoding": {
                    "x": {"field": "Station", "type": "nominal"},
                    "y": {"field": "O3_Value", "type": "quantitative"},
                    "size": {"field": "O3_Value", "type": "quantitative"},
                    "color": {"field": "Station", "type": "nominal"},
                },
            },
            use_container_width=True,
        )

    stations_no2 = st.sidebar.multiselect(
        "Levels of NO2 by station ", db_air["Station"].unique()
    )
    if stations_no2:
        data = db_air[db_air.Station.isin(stations_no2)]

        st.vega_lite_chart(
            data,
            {
                "width": "container",
                "height": 400,
                "mark": "circle",
                "encoding": {
                    "x": {"field": "Station", "type": "nominal"},
                    "y": {"field": "NO2_Value", "type": "quantitative"},
                    "size": {"field": "NO2_Value", "type": "quantitative"},
                    "color": {"field": "Station", "type": "nominal"},
                },
            },
            use_container_width=True,
        )

    stations_pm10 = st.sidebar.multiselect(
        "Levels of PM10 by station ", db_air["Station"].unique()
    )
    if stations_pm10:
        data = db_air[db_air.Station.isin(stations_pm10)]

        st.vega_lite_chart(
            data,
            {
                "width": "container",
                "height": 400,
                "mark": "circle",
                "encoding": {
                    "x": {"field": "Station", "type": "nominal"},
                    "y": {"field": "PM10_Value", "type": "quantitative"},
                    "size": {"field": "PM10_Value", "type": "quantitative"},
                    "color": {"field": "Station", "type": "nominal"},
                },
            },
            use_container_width=True,
        )

if page == "Air quality over a month":

    st.caption(
        "This graph shows how O3 concentration in the air at ground level changes over a month (November, 2018). It can cause breathing problems, cause asthma, reduce lung function, and lead to lung disease."
    )
    st.vega_lite_chart(
        db_air,
        {
            "data": db_air,
            "width": 700,
            "height": 400,
            "mark": "line",
            "encoding": {
                "x": {"timeUnit": "day", "field": "Date"},
                "y": {"aggregate": "mean", "field": "O3_Value"},
            },
        },
    )

    st.caption(
        "This graph shows how NO2 concentration in the air changes over a month (November, 2018). Epidemiological studies have shown that the symptoms of bronchitis in asthmatic children have increased in European countries due to prolonged exposure to NO2."
    )
    st.vega_lite_chart(
        db_air,
        {
            "data": db_air,
            "width": 700,
            "height": 400,
            "mark": "line",
            "encoding": {
                "x": {"timeUnit": "day", "field": "Date"},
                "y": {"aggregate": "mean", "field": "NO2_Value"},
            },
        },
    )

    st.caption(
        "This graph shows how PM10 concentration in the air changes over a month (November, 2018). It is estimated that exposure to anthropogenic particles reduces the average life expectancy by 8.6 months."
    )
    st.vega_lite_chart(
        db_air,
        {
            "data": db_air,
            "width": 700,
            "height": 400,
            "mark": "line",
            "encoding": {
                "x": {"timeUnit": "day", "field": "Date"},
                "y": {"aggregate": "mean", "field": "PM10_Value"},
            },
        },
    )

if page == "Air quality and deaths":

    st.caption("Number of deaths during November of 2018")
    chart4 = (
        alt.Chart(db_deaths)
        .mark_bar()
        .encode(x=alt.X("Total_deaths"), y=alt.Y("Districts"),)
        .properties(title="Total deaths by districts")
    )
    st.altair_chart(chart4, use_container_width=True)

    st.caption("Air quality during November of 2018 by distict")
    chart5 = (
        alt.Chart(db_air)
        .mark_bar()
        .encode(x="Station", y="count()", color="Air_Quality:N")
        .properties(title="Air quality by district")
    )
    st.altair_chart(chart5, use_container_width=True)

if page == "Geoquery":

    df = pd.json_normalize(db_station["location"])
    m = Map()
    loc = list(df["coordinates"])
    for l in loc:
        Marker(location=l).add_to(m)
    folium_static(m)

if page == "Datesets":

    if st.checkbox("Show air quality Data"):
        db_air

    if st.checkbox("Show deaths Data"):
        db_deaths

    if st.checkbox("Show stations Data"):
        db_station


import streamlit as st
import requests
import numpy as np
import joblib

model = joblib.load("aqi_model.joblib")
waqi_token = "c489213d910524e8ae3de642298c48948c04e05c"

st.set_page_config(page_title="Global AQI Dashboard", layout="centered")
st.title("Global Real-Time AQI Dashboard")
st.markdown("Use this dashboard to monitor air quality worldwide with live WAQI data and AI prediction.")

city = st.text_input("Enter a city name", "Delhi")

if st.button("Get AQI Report"):
    try:
        url = f"https://api.waqi.info/feed/{city}/?token={waqi_token}"
        response = requests.get(url)
        data = response.json()

        if data['status'] != 'ok':
            st.error(f"No AQI data found for '{city}'. Try another.")
        else:
            station = data['data']['city']['name']
            aqi_live = data['data']['aqi']
            iaqi = data['data']['iaqi']

            so2 = iaqi.get('so2', {}).get('v', 0)
            no2 = iaqi.get('no2', {}).get('v', 0)
            pm25 = iaqi.get('pm25', {}).get('v', 0)
            pm10 = iaqi.get('pm10', {}).get('v', 0)

            X = [[so2, no2, pm25, pm10]]
            predicted_aqi = model.predict(X)[0]

            st.metric("Live AQI (WAQI)", aqi_live)
            st.metric("Predicted AQI (Model)", round(predicted_aqi, 2))

            st.subheader("Pollutants (μg/m³)")
            st.write({"SO2": so2, "NO2": no2, "PM2.5": pm25, "PM10": pm10})
            st.caption(f"Monitoring Station: {station}")

    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

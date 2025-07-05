# 🌍 Global Real-Time AQI Dashboard

An AI-powered Streamlit dashboard that allows users to view and predict **Air Quality Index (AQI)** for any global city in real time. It fetches live air quality data via WAQI API and uses a trained machine learning model to predict AQI based on pollutant levels.

## 🔗 Live Demo

👉 [Use the app](https://7ybjxeiga2ycf8tk7ejdvl.streamlit.app) — No installation needed!

## ✨ Features

- 🌐 Real-time AQI for any city via WAQI API  
- 📈 AI-based AQI prediction using SO₂, NO₂, PM2.5, and PM10  
- 🗺️ Interactive map of the monitoring location  
- 📊 Simulated AQI trend (last 7 days)
- 🎨 Clean and responsive Streamlit interface

## 🧠 Machine Learning

- Model: `LinearRegression`
- Trained on dummy pollutant data
- Stored as `aqi_model.joblib`

### 📌 Inputs:
- SO₂ (µg/m³)
- NO₂ (µg/m³)
- PM2.5 (µg/m³)
- PM10 (µg/m³)

### 📌 Output:
- Predicted AQI score

## 🛠️ Tech Stack

- Streamlit
- scikit-learn
- pandas, numpy
- joblib
- folium + streamlit-folium
- WAQI API (https://aqicn.org/api/)

## 📂 Project Structure


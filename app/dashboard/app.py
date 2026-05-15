import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import os
import json

# Page Config
st.set_page_config(page_title="Fish Feed Prediction AI", layout="wide")

st.title("🐟 Smart Aqua Culture: Fish Feed Prediction")

# Sidebar
st.sidebar.header("Input Parameters")

def user_input_features():
    ph = st.sidebar.slider('pH level', 0.0, 14.0, 7.0)
    temperature = st.sidebar.slider('Temperature (°C)', 0.0, 50.0, 25.0)
    turbidity = st.sidebar.number_input('Turbidity', 0.0, 100.0, 5.0)
    fish = st.sidebar.selectbox('Fish Species', ['katla', 'sing', 'rui', 'koi', 'prawn', 'pangas', 'tilapia', 'magur', 'shrimp', 'silverCup', 'karpio'])
    weight = st.sidebar.number_input('Fish Weight (kg)', 0.01, 10.0, 0.5)
    
    data = {
        'ph': ph,
        'temperature': temperature,
        'turbidity': turbidity,
        'fish': fish,
        'Fish_Weight': weight
    }
    return data

input_dict = user_input_features()

# Main UI
col1, col2 = st.columns(2)

with col1:
    st.subheader("Predict Feed Quantity")
    if st.button("Calculate Feed"):
        try:
            response = requests.post("http://localhost:8000/predict", json=input_dict)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Recommended Feed: **{result['feed_quantity']:.4f} kg**")
                st.info(f"Predicted Feed Ratio: {result['feed_ratio']:.4f}")
            else:
                st.error("API Error. Make sure the backend server is running.")
        except Exception as e:
            st.error(f"Connection Error: {e}")

with col2:
    st.subheader("System Status")
    try:
        health = requests.get("http://localhost:8000/")
        if health.status_code == 200:
            st.write("✅ Backend API: Online")
        else:
            st.write("❌ Backend API: Error")
    except:
        st.write("❌ Backend API: Offline")

# Footer
st.markdown("---")
st.caption("AI-Powered Aquaculture Management System v1.0")

import streamlit as st
import pandas as pd
import pickle

scaler = pickle.load(open('scaler.pkl', 'rb'))
ridge_model = pickle.load(open('ridge.pkl', 'rb'))

st.title("Algerian Forest Fire Prediction")
st.header("Predicting Forest Fires in Algeria")

Temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
RH = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
Ws = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=20.0, value=5.0)  
Rain = st.number_input("Rainfall (mm)", min_value=0.0, max_value=20.0, value=0.0)
FFMC = st.number_input("Fine Fuel Moisture Code", min_value=0.0, max_value=100.0, value=15.0)
DMC = st.number_input("Duff Moisture Code", min_value=0.0, max_value=100.0, value=10.0)
DC = st.number_input("Drought Code", min_value=0.0, max_value=100.0, value=50.0)
ISI = st.number_input("Initial Spread Index", min_value=0.0, max_value=100.0, value=10.0)   
BUI = st.number_input("Buildup Index", min_value=0.0, max_value=100.0, value=20.0)  
Classes = st.selectbox("Select Class", ["Fire", "No Fire"])
Classes = 0 if Classes == "not fire" else 1
region = st.selectbox("Select Region", ["Bejaia", "Sidi-Bel-Abbes"])
region = 0 if region == "Bejaia" else 1

if st.button("Predict"):
    input_data = pd.DataFrame({
        'Temperature': [Temperature],
        'RH': [RH],
        'Ws': [Ws],
        'Rain': [Rain],
        'FFMC': [FFMC],
        'DMC': [DMC],
        'DC': [DC],
        'ISI': [ISI],
        'BUI': [BUI],
        'Classes': [Classes],
        'Region': [region]
    })

    input_data_scaled = scaler.transform(input_data)
    prediction = ridge_model.predict(input_data_scaled)
    st.success(f"The predicted FWI value is: {prediction[0]:.2f}")

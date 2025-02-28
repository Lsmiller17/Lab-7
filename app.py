import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('house_price_model.pkl')

# Prediction function
def predict_price(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]

# Streamlit UI
st.title('Ames Housing Price Predictor')

input_data = {
    'GrLivArea': st.number_input('Above Ground Living Area (sq ft)', min_value=500, max_value=5000, value=1500),
    'GarageCars': st.slider('Number of Garage Spaces', min_value=0, max_value=4, value=1),
    'TotalBsmtSF': st.number_input('Total Basement Area (sq ft)', min_value=0, max_value=3000, value=800),
    'YearBuilt': st.number_input('Year Built', min_value=1800, max_value=2024, value=2000)
}

if st.button('Predict Price'):
    price = predict_price(input_data)
    st.write(f'🏡 **Predicted House Price: ${price:,.2f}**')

import streamlit as st

from model import load_model


@st.cache_resource
def get_model():
    return load_model()

st.set_page_config(page_title="House Price Predictor", page_icon="🏠")
st.title("🏠 House Price Predictor")
st.caption("Estimate a property's market value using the local ML model.")

with st.form("prediction"):
    area = st.number_input("Living area (sq ft)", min_value=100.0, value=1500.0, step=50.0)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=20, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1.0, max_value=20.0, value=2.0, step=0.5)
    age = st.number_input("Property age (years)", min_value=0.0, max_value=200.0, value=10.0)
    distance = st.number_input("Distance to city (km)", min_value=0.0, max_value=500.0, value=10.0)
    submitted = st.form_submit_button("Predict price")

if submitted:
    values = [[area, bedrooms, bathrooms, age, distance]]
    predicted_price = float(get_model().predict(values)[0])
    st.success(f"Estimated price: ${predicted_price:,.2f}")

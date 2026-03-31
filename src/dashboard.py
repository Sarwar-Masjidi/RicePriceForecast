import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

st.title("📊 Rice Price Forecast Dashboard")

# Load data
df = pd.read_csv('data/raw/rice_prices.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Show raw data
st.subheader("Raw Data")
st.write(df.tail())

# Plot original data
st.subheader("Original Price Trend")
fig1, ax1 = plt.subplots()
ax1.plot(df['date'], df['price'])
ax1.set_title("Rice Prices Over Time")
st.pyplot(fig1)

# Cap outliers
cap_value = df['price'].quantile(0.99)
df['price_capped'] = np.where(df['price'] > cap_value, cap_value, df['price'])

# Prepare for Prophet
prophet_df = df[['date','price_capped']].rename(columns={'date':'ds','price_capped':'y'})

# Train model
model = Prophet()
model.fit(prophet_df)

# Forecast
future = model.make_future_dataframe(periods=4, freq='W')
forecast = model.predict(future)

# Plot forecast
st.subheader("Forecast (Next 4 Weeks)")
fig2 = model.plot(forecast)
st.pyplot(fig2)

# Show forecast values
st.subheader("Forecast Values")
st.write(forecast[['ds','yhat']].tail(4))
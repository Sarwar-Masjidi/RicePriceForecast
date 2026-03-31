RicePriceForecast – Rice Price Prediction and Anomaly Detection

Project Overview
RicePriceForecast is a Python project designed to predict rice prices and detect anomalies in Central Asia.
It uses time series models ARIMA and Prophet, and includes an interactive dashboard built with Streamlit.
The dataset simulates rice prices with seasonal trends, noise, and occasional outliers.

The project includes:

Dataset generation (src/main.py)
Exploratory Data Analysis (notebooks/01_eda.ipynb)
Streamlit dashboard (src/dashboard.py)
Clean CSV dataset (data/raw/rice_prices.csv)

Features

Simulated rice price data with seasonality, trend, and outliers
Predictions using ARIMA and Prophet
Handling extreme spikes and improving model accuracy
Interactive Streamlit dashboard to visualize predictions and anomalies

How to Run

Clone the repository:
git clone https://github.com/
<Sarwar-Masjidi>/RicePriceForecast.git
Create a virtual environment (recommended):
python -m venv venv

Activate the environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
Install required libraries:
pip install -r requirements.txt
Generate dataset:
python src/main.py
Run the Streamlit dashboard:
python -m streamlit run src/dashboard.py --server.headless true
Open the EDA notebook:
notebooks/01_eda.ipynb to explore rice prices and anomalies

Documentation in Multiple Languages

Dari (فارسی)
RicePriceForecast 
پروژه‌ای است که قیمت برنج در آسیای مرکزی را پیش‌بینی کرده و ناهنجاری‌ها را شناسایی می‌کند.
این پروژه شامل داده‌های شبیه‌سازی شده قیمت برنج با روند فصلی، نویز و اسپایک‌های نادر است.

Pashto (پښتو)
RicePriceForecast
یوه پروژه ده چې د منځنۍ آسیا په وریجو بیې وړاندوینه کوي او ناسمې بیې کشفوي.
پروژې کې د وریجو د بیو شبیه شوې ډاټا شامل ده چې موسمي تمایلات، شور، او ناڅاپي لوړوالی لري.

Next Steps

Improve prediction models and reduce error metrics
Add rolling median filter to handle extreme spikes
Extend to other commodities for a full Nerkhnama-style system

Steps after pasting

Save the file
Open terminal and run:
git add README.md
git commit -m "Add full README in English, Dari, and Pashto"
git push origin main

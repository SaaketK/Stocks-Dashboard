# Stock Market Analysis Dashboard

A Python-based web application built with Dash and Plotly for visualizing stock market trends. This dashboard provides interactive data exploration of stock prices across different companies and months.

## Features

* Dynamic Filtering: Select specific months to update all visualizations
* Metric Selection: Toggle between Open, Close, High, and Low stock price metrics
* Comparative Bar Chart: View the average stock price for each company in a selected month
* Distribution Box Plot: Analyze price changes and distributions across different companies

### Installation & Usage

Required: Python 3.x installed

1. Clone the repo or download the source code.
2. Install the required dependencies:
pip install pandas plotly dash

3. Use either the sample stockdata provided (StockData.csv) or use a custom file in the form: Date,Open,High,Low,Close,AdjClose,Volume,Company,Month
4. Run the app:
python app.py

## How it Works

The application uses Dash callbacks to listen for user input from the dropdown and radio buttons. When a change is detected, the underlying Pandas dataframe is filtered, and the Plotly Express library updates the bar and box plots

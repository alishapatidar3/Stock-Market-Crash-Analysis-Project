import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Streamlit config
st.set_page_config(page_title="Stock Crash Analyzer", layout="wide")

st.title("📉 Stock Market Crash Analyzer")

# User Inputs
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

# When user clicks "Analyze"
if st.button("Analyze") and ticker:
    # Fetch data from yfinance
    df = yf.download(ticker, start=start_date, end=end_date)

    if df.empty:
        st.error("No data found for this ticker. Please try another one.")
    else:
        # Reset index to make 'Date' a column
        df.reset_index(inplace=True)

        # Calculate daily returns and identify crash days
        df['Daily_Return'] = df['Close'].pct_change() * 100
        crash_threshold = -5
        df['Crash_Daily'] = df['Daily_Return'] <= crash_threshold

        # Format Volume and Date for display
        df['Volume'] = df['Volume'].astype('int64')
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

        # Display the latest stock data
        st.subheader(f"📊 {ticker.upper()} Stock Data (Latest)")
        columns_to_show = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume', 'Daily_Return', 'Crash_Daily']
        st.dataframe(df[columns_to_show].tail().astype(str), use_container_width=True)

        # Plot: Closing Price
        st.subheader("📈 Closing Price Over Time")
        fig, ax = plt.subplots()
        df.set_index(pd.to_datetime(df['Date']))['Close'].plot(ax=ax, title=f"{ticker.upper()} Closing Price")
        ax.set_ylabel("Price (USD)")
        st.pyplot(fig)

        # Plot: Daily Returns with Crash Highlights
        st.subheader("📉 Daily Returns with Crash Highlights")
        fig2, ax2 = plt.subplots()

        # Line plot of daily returns
        df.set_index(pd.to_datetime(df['Date']))['Daily_Return'].plot(ax=ax2, color='gray', alpha=0.6, label='Daily Return')

        # Scatter plot for crash days
        crash_days = df[df['Crash_Daily']]
        ax2.scatter(pd.to_datetime(crash_days['Date']), crash_days['Daily_Return'], color='red', label='Crash Days')

        # Crash threshold line
        ax2.axhline(crash_threshold, color='red', linestyle='--', label='Crash Threshold')

        ax2.set_title("Daily Returns with Crashes")
        ax2.set_ylabel("Daily Return (%)")
        ax2.legend()
        st.pyplot(fig2)


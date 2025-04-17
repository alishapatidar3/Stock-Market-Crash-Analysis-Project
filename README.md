# Stock-Market-Crash-Analysis-Project

This project focuses on identifying and analyzing stock market crashes using historical stock data. Leveraging Python and data visualization tools, the analysis uncovers significant dips in daily returns and highlights their impact on stock performance. The tool allows users to input custom stock tickers and dates for dynamic analysis.

---

## 📌 Features

- **Crash Detection**: Identify daily crashes based on -5% thresholds.
- **Drawdown Analysis**: Quantify dips from historical peaks to detect bear markets.
- **Crash Clustering**: Segment consecutive crash days into clusters.
- **Historical Crash Visualization**: Focus on events from 1997, 2008–09, and 2020.
- **Early Warning System**: Simulate predictive signals using rolling returns and volatility.
- **Interactive Dashboard**: Visualize crashes and returns for any stock via Streamlit.

---

## ⚙️ Technologies & Tools Used
🐍 Python – Core programming language for data analysis and visualization

📊 Pandas – Efficient data cleaning, transformation, and manipulation

📈 Matplotlib & Seaborn – Visualization of stock trends and crash indicators

📉 yFinance – Real-time stock data collection for interactive exploration

🌐 Streamlit – Web application framework for an interactive analysis experience

📁 Jupyter Notebook – Exploratory data analysis and model testing environment

---

## 💡 Business Insights
- Helps investors identify high-risk periods and patterns leading up to market crashes
- Useful for financial analysts and traders to improve risk management strategies

---

## 📸 Streamlit App Screenshot
<img width="1225" alt="Screenshot 2025-04-18 at 12 33 53 AM" src="https://github.com/user-attachments/assets/49d9dc59-3906-4b26-a8cd-6b55b0f627a5" />

### 📈 Closing Price Over Time
<img width="957" alt="Screenshot 2025-04-18 at 12 34 38 AM" src="https://github.com/user-attachments/assets/66d6908d-5a35-4159-8f8b-4cd11b1ea572" />

## 📉 Daily Returns with Crash Highlights
<img width="957" alt="Screenshot 2025-04-18 at 12 37 32 AM" src="https://github.com/user-attachments/assets/9dd39271-c00b-40ef-ac41-d8d131b7f3b0" />

---

## 🛠️ Requirements

### Install the dependencies using pip:

- pip install pandas numpy matplotlib plotly streamlit yfinance

### website using Streamlit
### 🚀 How to Run It:
Save the code above to a file named stock_crash_analysis_app.py.

Open a terminal in that folder.
Run:
1. pip install streamlit
2. streamlit run stock_crash_analysis_app.py
3. Open the browser (Streamlit will launch it for you).
4. Type any ticker like AAPL, TSLA, MSFT, etc., choose your date range, and hit Analyze.









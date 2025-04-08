import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import yfinance as yf

st.set_page_config(page_title="Smart Portfolio Risk Analyzer", layout="centered")
st.title("📊 Smart Portfolio Risk Analyzer")

st.markdown("Enter your portfolio below. Example: `AAPL 40%, TQQQ 30%, TSLA 30%`")

# --- Helper: Parse user input ---
def parse_portfolio(input_str):
    tickers = []
    allocations = []
    pattern = re.compile(r'(\b[A-Z]+\b)[\s:=]*([0-9]+\.?[0-9]*)%?')
    matches = pattern.findall(input_str.upper())
    for match in matches:
        tickers.append(match[0])
        allocations.append(float(match[1]))
    return tickers, allocations

# --- Helper: Get sector info ---
def get_sector_info(tickers):
    sectors = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            sector = info.get("sector", "Unknown")
        except:
            sector = "Unknown"
        sectors[ticker] = sector
    return sectors

# --- Inputs ---
portfolio_input = st.text_input("Your Portfolio:", "AAPL 40%, TQQQ 30%, TSLA 30%")
strategy = st.selectbox("Your Strategy Focus:", ["Growth", "Stable", "Mixed"])

if st.button("Analyze Portfolio"):
    # --- Parse input ---
    assets, allocations = parse_portfolio(portfolio_input)

    if not assets or sum(allocations) != 100:
        st.error("Please make sure you enter valid tickers and the total adds up to 100%.")
    else:
        df = pd.DataFrame({"Asset": assets, "Allocation (%)": allocations})

        # --- Get and display sector info ---
        sector_map = get_sector_info(assets)
        df["Sector"] = df["Asset"].map(sector_map)
        st.subheader("🔎 Portfolio Breakdown by Sector")
        st.dataframe(df)

        # --- Pie Chart ---
        fig, ax = plt.subplots()
        ax.pie(allocations, labels=assets, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # --- Risk Warnings (Mock) ---
        st.subheader("⚠️ Risk Warnings")
        st.markdown("- Over 50% exposure to high-volatility assets")
        st.markdown("- Leverage detected (TQQQ)")

        # --- Suggestions (Mock) ---
        st.subheader("💡 Suggestions")
        st.markdown("- Consider reducing TQQQ to 20% to improve balance")
        st.markdown("- Add more diversification into other sectors or asset classes")

        # --- Diversification Score ---
        st.subheader("📈 Diversification Rating")
        st.markdown("★★★☆☆ (3/5)")

        # --- Placeholder for PDF Download ---
        st.button("Download Report (Coming Soon)")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Portfolio Risk Analyzer", layout="centered")
st.title("📊 Smart Portfolio Risk Analyzer")

st.markdown("Enter your portfolio below. Example: `AAPL 40%, TQQQ 30%, TSLA 30%`")

# --- Inputs ---
portfolio_input = st.text_input("Your Portfolio:", "AAPL 40%, TQQQ 30%, TSLA 30%")
strategy = st.selectbox("Your Strategy Focus:", ["Growth", "Stable", "Mixed"])

if st.button("Analyze Portfolio"):
    # --- Fake Parsed Data ---
    assets = ["AAPL", "TQQQ", "TSLA"]
    allocations = [40, 30, 30]

    df = pd.DataFrame({"Asset": assets, "Allocation (%)": allocations})

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

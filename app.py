
import streamlit as st
from analyze import analyze_data
from fetch_data import fetch_sports_news
from datetime import datetime

st.set_page_config(page_title="Real-Time Sports Market AI", layout="wide")

st.title("Real-Time Sports Market Research Tool (India Focused)")
st.markdown("Track real-time trends, sentiment, and topics in Indian sports using AI.")

# Sidebar
st.sidebar.title("Control Panel")
keyword = st.sidebar.text_input("Track Keyword", value="Indian sports")
if st.sidebar.button("Fetch & Analyze"):
    with st.spinner("Fetching and analyzing data..."):
        data = fetch_sports_news(keyword)
        result = analyze_data(data)
        st.session_state["data"] = result

# Main Area
if "data" in st.session_state:
    st.subheader(f"Sentiment Summary for '{keyword}'")
    st.write(st.session_state["data"]["summary"])
    
    st.subheader("Top Topics")
    st.write(", ".join(st.session_state["data"]["top_topics"]))

    st.subheader("Recent Headlines")
    for item in st.session_state["data"]["raw"]:
        st.markdown(f"- [{item['title']}]({item['link']})")

st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

import streamlit as st
from src.services import get_trends

st.title("Twitter Trends Dashboard")

trends = get_trends()

for trend in trends:
    st.write(f"[{trend['name']}]({trend['url']})")

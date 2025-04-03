import json
import streamlit as st
@st.cache_data
def load_json(file_path='faq.json'):
    try:
        with open(file_path,"r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        st.error(f"failing to load the data from json:{e}")
        return []
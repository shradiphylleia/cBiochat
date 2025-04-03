import streamlit as st
import time
import re
import string
from json_loader import load_json

json_data = load_json()

def get_response_json(user_query):
    user_query = user_query.lower().translate(str.maketrans('', '', string.punctuation))

    if "faqs" not in json_data or not isinstance(json_data["faqs"], list):
        return "json problem"
    
    for faq in json_data["faqs"]:
        if "question" in faq and "answer" in faq:
            normalized_question=faq["question"].lower().translate(str.maketrans('', '', string.punctuation))
            pattern=re.compile(re.escape(normalized_question), re.IGNORECASE)

            if pattern.search(user_query):
                return faq["answer"]

    return "a relevant answer matching the query was not found"



def rsp(response):
    if response:
        for word in response.split():
            yield word + " "
            time.sleep(0.2)

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt:=st.chat_input("Ask your query..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.msgs.append({"role": "user", "content": prompt})

    bot_response=get_response_json(prompt)

    with st.chat_message('ai'):
        st.write_stream(rsp(bot_response))

    st.session_state.msgs.append({'role': 'ai', 'content': bot_response})

import streamlit as st

st.title('cBioPotal: chatbot')
pages={
    "General":[st.Page("about.py",title="about chatbot")],
    "chatbot":[st.Page("chat.py",title="cBio documentation chatbot")]
}

pg=st.navigation(pages)
pg.run()
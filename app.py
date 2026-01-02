import streamlit as st
from langchain_community.llms import Ollama


st.set_page_config(page_title="AI Chatbot Sederhana", page_icon="p")

st.title("Chatbot AI Lokal")
st.caption("Ditenagai oleh Ollama (Llama 3 / DeepSeek)")

llm = Ollama(model="llama3")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Apa yang ingin kamu tanyakan?"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
 
    with st.chat_message("assistant"):
        with st.spinner("Sedang berpikir..."):
            response = llm.invoke(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

st.title("💬 Simple LangChain Chatbot")

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

system_msg = SystemMessage(content="You are a helpful assistant.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.text)

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    response = llm.invoke([system_msg] + st.session_state.messages)

    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append(AIMessage(content=response.text))

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

conver_his = []

while True:
    user_input = input("YOU: ")
    if user_input.lower() == "exit":
        break
    conver_his.append(HumanMessage(content=user_input))
    response = model.invoke(conver_his)
    # conver_his.append(AIMessage(content=response.content))
    
    print(f"AI: {response.text}\n")


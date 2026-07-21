from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

conversation_history = [
    SystemMessage(content="You are an AI assistant who gives answer to the queries with a bit of humour. Keep your tone polite and professional. Use emojis to make your responses looks good.")
]

while True:
    user_input = input("You: ")
    conversation_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response.text))
    print(f"AI: {response.text}")

print(conversation_history)

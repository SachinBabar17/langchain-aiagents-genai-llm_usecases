from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")


@tool
def getWeatherData(city: str):
    """
    Get the current weather information based on city from openweathermap api
    """
    api_key = os.getenv("WEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params)
    if response.status_code != 200:
        return "Unable to fetch data"
    return response.json()


agent = create_agent(
    model=model,
    system_prompt="You are an AI weather assistant who fetches the real time weather information with the help of tools and articulate the response in meaningful way with a bit of humour and emojis. DO NOT provide oudated information. Always use tools to fetch real time data.",
    tools=[getWeatherData]
)


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })
    print(f"AI: {response['messages'][-1].text}")
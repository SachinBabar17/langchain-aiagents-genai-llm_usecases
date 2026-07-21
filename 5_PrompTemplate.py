from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

template = PromptTemplate(
    template="Write an article in 500 words on the topic of {topic}", input_variables=["topic"])

template2 = PromptTemplate(
    template="Create 5 mulitple choice questions based on the article below \n {article}")

# prompt = template.invoke({'topic': 'AI'})
# article = model.invoke(prompt)
# prompt2 = template2.invoke({'article': article.text})
# quiz = model.invoke(prompt2)

chain = template | model | StrOutputParser() | template2 | model | StrOutputParser()

print(chain.invoke({'topic': 'AI'}))
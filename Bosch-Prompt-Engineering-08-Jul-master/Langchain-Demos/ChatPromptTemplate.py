from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate(
    [
        ("system", "You rewrite emails in a {tone} tone for a {audience} audience. Keep the core meaning intact. Respond with ONLY the rewritten email text — no options, no headers, no explanations, no markdown."),

        ("human", "hey can u send me the report by tmrw, kinda urgent"),
        ("ai", "Hi, could you please send over the report by tomorrow? It's fairly urgent — thanks in advance."),

        ("human", "not gonna make the call today, smth came up"),
        ("ai", "I won't be able to make today's call — something has come up. Apologies for the short notice."),

        ("human", "{email}")
    ]
)

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

chain = prompt | model

response = chain.invoke({
    "tone": "professional",
    "audience": "external client",
    "email": "yo buddy, we need to push the meeting. my bad."
})

print(response.text)

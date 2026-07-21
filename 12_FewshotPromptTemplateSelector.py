from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

examples = [
    {"ticket": "My invoice shows a charge I don't recognize.",
        "output": "CATEGORY: billing\nPRIORITY: P2\nTEAM: finance-ops"},
    {"ticket": "App crashes on photo upload.",
        "output": "CATEGORY: bug\nPRIORITY: P1\nTEAM: mobile-eng"},
    {"ticket": "Please add dark mode.",
        "output": "CATEGORY: feature-request\nPRIORITY: P4\nTEAM: product"},
    {"ticket": "I was charged twice this month.",
        "output": "CATEGORY: billing\nPRIORITY: P2\nTEAM: finance-ops"},
    {"ticket": "Login page throws a 500 error.",
        "output": "CATEGORY: bug\nPRIORITY: P1\nTEAM: backend-eng"},
    {"ticket": "Can we get CSV export?",
        "output": "CATEGORY: feature-request\nPRIORITY: P4\nTEAM: product"},
]

example_prompt = PromptTemplate(
    template="Ticket: {ticket}\n{output}",
    input_variables=["ticket", "output"]
)

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"),
    Chroma,
    k=2
)

fewshot_template = FewShotPromptTemplate(
    example_prompt=example_prompt,
    example_selector=example_selector,
    prefix="You are a ticket triage assistant for our internal system. Classify each ticket using our exact schema: CATEGORY, PRIORITY (P1-P4), TEAM, SUMMARY. TEAM must be one of: finance-ops, mobile-eng, backend-eng, product, security.",
    suffix="Ticket: {ticket}",
    input_variables=["ticket"]
)

chain = fewshot_template | model | StrOutputParser()

response = chain.invoke(
    {'ticket': "Users are seeing other people's account data on login."})
print(response)
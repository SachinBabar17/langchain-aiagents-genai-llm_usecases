from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")


class Feedback(BaseModel):
    name: str = Field(description="Name of the participant")
    summary: str = Field(description="Summary of the overall feedback")
    sentiment: Literal['positive', 'negative'] = Field(
        description="Sentiment fo the feedback. It can be either positive or negative")
    highlights: list[str] = Field(
        description="List of Highlights of the feedback")
    lowlights: list[str] = Field(
        description="List of Lowlights of the feedback")
    rating: int = Field(
        description="Rating of the feedback provided by participant")


pyparser = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="Analyze the sentiment of the following feedback and classify it inot positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback", "format_instructions"],
    partial_variables={
        'format_instructions': pyparser.get_format_instructions()}
)

chain = prompt | model | pyparser

positive_email_template = PromptTemplate(
    template=" Write a thank you mail to the participant for giving a positive feedback about the recent training program the participant attended\n {feedback}", input_variables=["feedback"]
)

negative_email_template = PromptTemplate(
    template=" Write an apology mail to the participant for giving a negative feedback about the recent training program the participant attended\n {feedback}", input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive',
     positive_email_template | model | StrOutputParser()),
    (lambda x: x.sentiment == 'negative',
     negative_email_template | model | StrOutputParser()),
    (lambda x: "Not able to analyze the sentiment")
)

main = chain | branch_chain

print(main.invoke({"feedback": "The Java Fullstack training program did not fully meet my expectations. Although the program covered important technologies such as Core Java, Spring Boot, Hibernate, and Angular, the overall delivery lacked sufficient depth and practical implementation. Several topics, particularly Spring Boot and Angular, were covered too quickly, making it difficult to understand and apply the concepts effectively. The hands-on exercises and live coding sessions were limited and did not provide enough opportunities to work on realistic, end-to-end application scenarios. The program also lacked adequate coverage of important areas such as debugging, code optimization, troubleshooting, testing, and industry best practices. More structured practical assignments, real-world examples, and dedicated time for resolving participant queries would have significantly improved the learning experience. Overall, the training needs considerable improvement in terms of pacing, practical exposure, topic depth, and alignment with real-world development practices. Rating: 2 out of 5 Feedback given by Dhiraj Kumar"}))
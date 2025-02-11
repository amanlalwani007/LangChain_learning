from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


messages = [
    SystemMessage("You are an expert in social media marketing."),
    HumanMessage("Give a short tip to create  engaging posts on Instagram."),
]
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result = model.invoke(messages)
print(f"Answers from Google: {result.content}")

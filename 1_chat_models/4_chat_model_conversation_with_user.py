from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

chat_history = []
system_message = SystemMessage(content="You are a helpful AI Assistant")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exist":
        break

    chat_history.append(HumanMessage(content=query))
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI: {response}")


print("--- Message History ---")
print(chat_history)

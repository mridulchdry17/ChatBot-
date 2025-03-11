from langchain_deepseek import ChatDeepSeek
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
# api_key = os.getenv("DEEPSEEK_API_KEY")

# Initialize model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"]  # Pass token explicitly
)

model = ChatHuggingFace(llm=llm)

chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history.append(user_input)

    # Invoke model with latest input, not entire history
    result = model.invoke(chat_history)

    chat_history.append(result.content)
    print("AI:", result.content)

print("\nChat History:", chat_history)



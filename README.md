# LangChain Chatbot using Zephyr-7B-Beta

This repository contains a chatbot built using **LangChain** and **HuggingFaceH4/zephyr-7b-beta**. The chatbot can handle general conversations, answer questions, and assist with various NLP tasks.

## Features

- Uses **Zephyr-7B-Beta**, a fine-tuned open-source LLM for chat-based applications.
- Integrated with **LangChain** to efficiently manage interactions.
- Supports **context-aware** responses.
- Easily extensible for different use cases.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot**
   ```bash
   python chatbot.py
   ```

## Usage

1. **Ensure you have a Hugging Face API token** stored in a `.env` file:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_api_key_here
   ```

2. **Run the chatbot script**:
   ```bash
   python chatbot.py
   ```

3. **Interact with the chatbot**:
   - Type a message and press enter.
   - Type `exit` to stop the conversation.

## Code Overview

```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_key:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is missing. Please check your .env file.")

# Initialize the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=api_key  # Explicitly pass API key
)

model = ChatHuggingFace(llm=llm)

chat_history = []

print("🤖 Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Invoke model
    result = model.invoke(user_input)

    # Store history (optional)
    chat_history.append({"user": user_input, "AI": result.content})

    print("AI:", result.content)

# Print entire chat history
print("\n📝 Chat History:")
for exchange in chat_history:
    print(f"You: {exchange['user']}\nAI: {exchange['AI']}\n")
```

## Difference Between LLM and Chatbot

| Feature | LLM (Large Language Model) | Chatbot |
|---------|---------------------------|---------|
| Purpose | General-purpose language understanding and generation | Application built on top of an LLM for specific tasks |
| Training | Trained on diverse datasets to learn language patterns | Uses an LLM but may have additional tuning for specific use cases |
| Flexibility | Can generate text, summarize, translate, and more | Usually designed for conversational interfaces |
| Example | Zephyr-7B-Beta, GPT-4, LLaMA-2 | ChatGPT, Your LangChain chatbot |

## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute!

## License

This project is licensed under the MIT License.

---

### 🚀 Happy Coding!


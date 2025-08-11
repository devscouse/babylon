from typing import Mapping, Sequence
from ollama import Client, Message

client = Client(
    host="http://localhost:11434",
)

SYSTEM_MSG = """
You are a language tutor who is assisting a student by running through a practice
conversation.

The topic of conversation, words used, and feedback given should be appropriate
for the current level of the student.

# SESSION CONTEXT
- **Native Language**: The native language of the student is English
- **Learning Language**: The student is learning Spanish
- **Learning Level**: The student learning level is Early A1 of CEFR

# RULES
- If the user asks you a question in English you should respond in english, this
will usually be to ask for feedback or help
- If the user makes very large errors during the practice session you may intervene
to guide them in the right direction
- Guide the conversation appropriately towards a natural ending then provide feedback
to the user
"""

def main():
    print("Hello from babylon-backend!")
    conversation: Sequence[Mapping[str, str] | Message] = [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user", "content": "I would like to begin my session"}
    ]

    response = client.chat(model="llama3.1:latest", messages=conversation)
    response_msg = response.message
    print(response_msg.content)
    conversation.append(response_msg.model_dump())
     
    while user_msg := input("Enter your response: "):
        conversation.append({"role": "user", "content": user_msg})
        response = client.chat(model="llama4:scout", messages=conversation)
        response_msg = response.message
        print(response_msg.content)
        conversation.append(response_msg.model_dump())




if __name__ == "__main__":
    main()

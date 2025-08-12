
from typing import List

from ollama import Client, Message
from src.settings import settings


client = Client(
    host=settings.ollama_host,
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

class BabylonAgent:
    model: str
    messages: List[Message]

    def __init__(self):
        self.messages = [
            Message(role="system", content=SYSTEM_MSG)
        ]
        self.model = "llama3.1:latest"

    def chat(self, msg: str) -> Message:
        self.messages.append(Message(role="user", content=msg))
        response = client.chat(model=self.model, messages=self.messages)
        self.messages.append(response.message)
        return response.message


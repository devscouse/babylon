from typing import List
from fastapi import FastAPI
from ollama import Message
from pydantic import BaseModel
from src.agent import BabylonAgent

app = FastAPI(
    title="Babylon-Backend",
)

agent = BabylonAgent()

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    messages: List[Message]

@app.post("/chat")
def chat(req: ChatRequest) -> ChatResponse:
    agent.chat(req.user_message)
    return ChatResponse(messages=agent.messages)
    


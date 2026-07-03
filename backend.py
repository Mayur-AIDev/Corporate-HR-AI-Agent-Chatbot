import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from fastapi.middleware.cors import CORSMiddleware

from graph import app_agent 

app = FastAPI(title="HR Agent Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/agent/chat")
async def chat_witn_agent(payload:ChatRequest):
    input_data = {"messages": [HumanMessage(content=payload.message)]}
    config = {"configurable": {"thread_id": payload.session_id}}

    final_state = app_agent.invoke(input_data, config=config)

    ai_response_text = final_state["messages"][-1].content

    return {"response": ai_response_text}


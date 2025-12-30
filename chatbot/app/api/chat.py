# app/api/chat.py

from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.memory.short_term import ShortTermMemory
from app.memory.long_term import LongTermMemory
from app.memory.retriever import retrieve_relevant_memories
from app.core.prompt import build_prompt
from app.core.llm import generate_response

router = APIRouter()

short_memory = ShortTermMemory()
long_memory = LongTermMemory()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    user_input = request.message

    short_memory.add_user(user_input)

    memories = retrieve_relevant_memories(long_memory, user_input)
    history = short_memory.get()

    prompt = build_prompt(memories, history, user_input)
    response = generate_response(prompt)

    short_memory.add_assistant(response)

    # Store only meaningful user info (simple v1 rule)
    if len(user_input.split()) > 4:
        long_memory.add(user_input)

    return ChatResponse(response=response)

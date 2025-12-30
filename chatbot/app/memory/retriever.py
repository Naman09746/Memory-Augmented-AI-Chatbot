# app/memory/retriever.py

from app.core.config import TOP_K_MEMORY
def retrieve_relevant_memories(memory, query):
    try:
        return memory.search(query, TOP_K_MEMORY)
    except Exception as e:
        print("Memory retrieval failed:", e)
        return []

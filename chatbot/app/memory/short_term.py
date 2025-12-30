# app/memory/short_term.py

from collections import deque
from app.core.config import SHORT_TERM_LIMIT

class ShortTermMemory:
    def __init__(self):
        self.buffer = deque(maxlen=SHORT_TERM_LIMIT)

    def add_user(self, message: str):
        self.buffer.append(f"User: {message}")

    def add_assistant(self, message: str):
        self.buffer.append(f"Assistant: {message}")

    def get(self) -> list[str]:
        return list(self.buffer)

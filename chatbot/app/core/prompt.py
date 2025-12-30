# app/core/prompt.py

def build_prompt(memories: list[str], history: list[str], user_input: str) -> str:
    memory_section = "\n".join(memories) if memories else "No relevant memories."
    history_section = "\n".join(history)

    return f"""
You are a professional, intelligent assistant with long-term memory.

Relevant past memories:
{memory_section}

Recent conversation:
{history_section}

User message:
{user_input}

Respond clearly, correctly, and concisely.
""".strip()

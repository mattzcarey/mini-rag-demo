import random

messages = ["Hello there! I'm Mini RAG, your AI personal assistant",
"Hey, how can I help you today?",
"What can I do for you?",
]

def build_welcome_message() -> str:
    return random.choice(messages)
    


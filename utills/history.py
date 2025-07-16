def format_chat_history(chat_history):
    return "\n".join([f"User: {q}\nAssistant: {a}" for q, a in chat_history])

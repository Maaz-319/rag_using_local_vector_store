import os

from config import GOOGLE_API_KEY
os.environ["GOOGLE_API_KEY"] = str(GOOGLE_API_KEY)


from retreival.retreiver import get_retriever
from chains.qa_chain import answer_question


chat_history = []

def main():
    print("Milky Way Assistant — Ask a question (type 'exit' to quit)")
    retriever = get_retriever()

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = answer_question(query, retriever, chat_history)
        print(f"Assistant: {response}")
        chat_history.append((query, response))

if __name__ == "__main__":
    main()

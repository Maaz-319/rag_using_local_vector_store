from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.prompt import concise_prompt
from utills.history import format_chat_history

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
qa_chain = LLMChain(llm=llm, prompt=concise_prompt)

def answer_question(question, retriever, chat_history):
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    formatted_history = format_chat_history(chat_history)

    response = qa_chain.run({
        "context": context,
        "chat_history": formatted_history,
        "question": question
    })

    return response

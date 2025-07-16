import os
import threading
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from config import GOOGLE_API_KEY

os.environ["GOOGLE_API_KEY"] = str(GOOGLE_API_KEY)

chat_history = []
retriever = None
answer_question = None
model_ready = False

class ChatApp(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("RAG Assistant - By Maaz")
        self.state('zoomed')
        self.resizable(True, True)

        self.chat_display = ScrolledText(self, wrap=tk.WORD, font=("Segoe UI", 12),
                                         bg="#23272b", fg="#f8f9fa", insertbackground="#f8f9fa",
                                         state=tk.DISABLED)
        self.chat_display.pack(fill=BOTH, expand=True, padx=20, pady=(20, 0))

        self.entry_frame = tb.Frame(self)
        self.entry_frame.pack(fill=X, padx=20, pady=20)

        self.user_entry = tb.Entry(self.entry_frame, font=("Segoe UI", 12))
        self.user_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
        self.user_entry.bind("<Return>", self.on_send)

        self.send_btn = tb.Button(self.entry_frame, text="Send", bootstyle=PRIMARY, command=self.on_send)
        self.send_btn.pack(side=RIGHT)

        self.user_entry.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.user_entry.focus()

        self.display_message("Assistant", "Loading Model...Please Wait....")

        threading.Thread(target=self.initialize_model, daemon=True).start()

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}:\n", "sender")
        self.chat_display.insert(tk.END, f"{message}\n\n", "message")
        self.chat_display.tag_config("sender", foreground="#6c757d", font=("Segoe UI", 10, "bold"))
        self.chat_display.tag_config("message", foreground="#f8f9fa", font=("Segoe UI", 12))
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def on_send(self, event=None):
        if not model_ready:
            self.display_message("Assistant", "Please wait, the assistant is still loading.")
            return

        query = self.user_entry.get().strip()
        if not query:
            return

        self.display_message("You", query)
        self.user_entry.delete(0, tk.END)

        threading.Thread(target=self.get_response, args=(query,), daemon=True).start()

    def get_response(self, query):
        global chat_history, answer_question, retriever
        # self.display_message("Assistant", "Thinking...")
        response = answer_question(query, retriever, chat_history)
        self.display_message("Assistant", response)
        chat_history.append((query, response))

    def initialize_model(self):
        global retriever, answer_question, model_ready

        from retreival.retreiver import get_retriever
        from chains.qa_chain import answer_question as aq

        retriever = get_retriever()
        answer_question = aq
        model_ready = True
        
        self.chat_display.delete("1.0", tk.END)
        self.display_message("Assistant", "Assistant is ready! Ask me anything about the Milky Way.")
        self.user_entry.config(state=tk.NORMAL)
        self.send_btn.config(state=tk.NORMAL)

    def on_close(self):
        self.destroy()

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import ttk
from stock_data import fetch_stock_data, plot_stock_data, metrics
from ai_interactions import stock_predict, chat_with_stock

app = tk.Tk()
app.title("Stock Advisor App")
app.geometry("1440x900")

canvas_widget = None  # Global variable to keep track of the current graph canvas widget


def display_stock_info(event=None):
    global canvas_widget

    ticker_symbol = stock_entry.get()

    # Check if ticker_symbol is empty
    if not ticker_symbol:
        messagebox.showerror("Error", "Please enter a stock ticker.")
        return

    try:
        stock_info = fetch_stock_data(ticker_symbol)
        if not stock_info or 'shortName' not in stock_info:
            messagebox.showerror("Error", f"Couldn't fetch data for ticker: {ticker_symbol}")
            return

        sidebar_content = "\n".join(
            [f"{description}: {stock_info.get(key, 'N/A')}" for key, description in metrics.items()])
        sidebar_label.config(text=sidebar_content)
        advice = stock_predict(stock_info)
        openai_response_label.config(text=advice)
        canvas_widget = plot_stock_data(ticker_symbol, app, canvas_widget)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def ask_openai_question():
    ticker_symbol = stock_entry.get()

    # Check if ticker_symbol is empty
    if not ticker_symbol:
        messagebox.showerror("Error", "Please select a stock first.")
        return

    user_question = question_entry.get()

    # Check if user_question is empty
    if not user_question:
        messagebox.showerror("Error", "Please enter a question to ask OpenAI.")
        return

    try:
        stock_info = fetch_stock_data(ticker_symbol)
        if not stock_info or 'shortName' not in stock_info:
            messagebox.showerror("Error", f"Couldn't fetch data for ticker: {ticker_symbol}")
            return

        response = chat_with_stock(stock_info, user_question)
        openai_response_label.config(text=response)
    except Exception as e:
        messagebox.showerror("Error", str(e))


frame = ttk.Frame(app)
frame.pack(side="top", fill="x", padx=20, pady=20)

stock_label = ttk.Label(frame, text="Enter Stock Ticker:")
stock_label.pack(side="left", padx=5)
stock_entry = ttk.Entry(frame)
stock_entry.pack(side="left", padx=5)

fetch_button = ttk.Button(frame, text="Fetch Stock Info", command=display_stock_info)
fetch_button.pack(side="left", padx=5)

# Sidebar for metrics
sidebar_label = ttk.Label(app, text="", wraplength=250, justify="left",
                          font=('Arial', 12), background='#F0F0F0')
sidebar_label.pack(side="left", fill="y", padx=10, pady=20)

# Label for AI responses
openai_response_label = ttk.Label(app, text="", wraplength=1000, justify="left")
openai_response_label.pack(side="top", fill="x", padx=10, pady=20)

# Entry field for asking questions
question_label = ttk.Label(app, text="Ask OpenAI about the stock:")
question_label.pack(side="top", padx=10, pady=5)

question_entry = ttk.Entry(app, width=100)
question_entry.pack(side="top", padx=10, pady=5)

ask_button = ttk.Button(app, text="Ask OpenAI", command=ask_openai_question)
ask_button.pack(side="top", padx=10, pady=10)
app.configure(bg='#F0F0F0')

app.mainloop()

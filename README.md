# Stock Advisor App

A user-friendly GUI application that leverages OpenAI to provide insights and recommendations on stocks.

## 🌟 Features

- **Fetch Key Metrics from yFinance:** Enter any stock ticker to retrieve and display its vital statistics.
- **Visualize Price History:** See the stock's price trajectory over the past year with an integrated graph.
- **Interact with OpenAI:** Pose questions about the stock and receive insights powered by OpenAI.

## 🚀 Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the Repository:**


git clone https://github.com/vedant-varma/stock-advisor-app.git
cd stock-advisor-app


2. **Install Dependencies:**


pip install -r requirements.txt


3. **API Key Configuration:** Set up your OpenAI API key. Make sure to replace `YOUR_API_KEY` with your actual OpenAI API key:


export OPENAI_API_KEY=YOUR_API_KEY


## 🔍 Usage

To launch the app, simply run:

python main.py


## 📦 Turning the App into an Executable

If you wish to convert the app into a standalone executable:

1. Install `pyinstaller`:

pip install pyinstaller


2. Generate the executable:

pyinstaller --onefile main.py

Once done, find your standalone executable in the `dist` directory.

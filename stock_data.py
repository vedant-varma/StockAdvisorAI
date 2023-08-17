import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

metrics = {
    'shortName': 'Stock Name',
    'sector': 'Sector',
    'marketCap': 'Market Capitalization',
    'forwardPE': 'Forward Price-to-Earnings Ratio',
    'dividendYield': 'Dividend Yield',
    'beta': 'Beta',
    'trailingPE': 'Trailing Price-to-Earnings Ratio',
    'fiftyTwoWeekHigh': '52 Week High',
    'fiftyTwoWeekLow': '52 Week Low',
    'regularMarketPrice': 'Current Stock Price'
}


def fetch_stock_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    stock_info = stock.info
    # Fetching the stock's most recent closing price
    try:
        stock_info['regularMarketPrice'] = stock.history(period="1d").iloc[-1]['Close']
    except:
        stock_info['regularMarketPrice'] = 'N/A'
    return stock_info


def plot_stock_data(ticker_symbol, app, canvas_widget):
    # Remove old graph if present
    if canvas_widget:
        canvas_widget.destroy()

    stock = yf.Ticker(ticker_symbol)
    stock_data = stock.history(period="1y")

    fig, ax = plt.subplots(figsize=(8, 6))
    stock_data['Close'].plot(ax=ax)

    # Adding dot for the current closing price
    current_close = stock_data['Close'].iloc[-1]
    ax.scatter(stock_data.index[-1], current_close, color='red', s=50, label='Current Close Price')
    ax.legend(loc='upper left')

    ax.set_title(f"Stock Price History: {ticker_symbol}")
    ax.set_ylabel("Price ($)")
    ax.set_xlabel("Date")

    # Embedding the plot in tkinter
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side="bottom", fill="both", expand=True)
    canvas.draw()

    return canvas_widget

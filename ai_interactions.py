import openai

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

# Set up your OpenAI API key
openai.api_key = "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"

def stock_predict(stock_info):
    stock_context = "\n".join([f"{description}: {stock_info.get(key, 'N/A')}" for key, description in metrics.items()])
    messages = [
        {"role": "system",
         "content": "You are an assistant that provides insights on stocks."},
        {"role": "user",
         "content": f"Based on the following stock details:\n{stock_context}\n\nCan you provide insights or a recommendation for this stock?"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    return response.choices[0].message['content']

def chat_with_stock(stock_info, text):
    stock_context = "\n".join([f"{description}: {stock_info.get(key, 'N/A')}" for key, description in metrics.items()])
    messages = [
        {"role": "system",
         "content": "You are an assistant that provides insights on stocks."},
        {"role": "user",
         "content": f"Based on the following stock details:\n{stock_context}\n\nUser asks: {text}"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    return response.choices[0].message['content']

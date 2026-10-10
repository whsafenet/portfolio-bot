import yfinance as yf
import requests

# ---- YOUR PORTFOLIO ----
tickers = ["AAPL", "MSFT", "O", "SCHD", "JEPI"]  # We will customize this later

def get_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        return data["Close"][0]
    return None

def get_news(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey=1dec4693b4d04e2abae20cae7fd870e5"
    try:
        r = requests.get(url)
        articles = r.json().get("articles", [])
        headlines = [a["title"] for a in articles[:5]]
        return headlines
    except:
        return []

def main():
    print("=== Daily Summary ===")
    for t in tickers:
        price = get_price(t)
        print(f"{t}: {price}")

        news = get_news(t)
        print("News:")
        for n in news:
            print(f" - {n}")
        print()

if __name__ == "__main__":
    main()


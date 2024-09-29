import yfinance as yf

# tickers from yahoo finance
data = yf.download("MSFT", period="6mo")
import pandas as pd
import yfinance as yf
from datetime import date

'''
video [en]: https://youtu.be/yrNH9JkjSr0
video [fr]: https://youtu.be/YhhVzxdXgkM
'''

# --- 1) Download and save historical data of Apple
def basic_download():
    aapl = yf.download("AAPL", period="", interval="", progress=False)
    aapl.to_csv("AAPL.csv", index=True)
    return aapl

#apple = basic_download()


# --- 2) Download multiple tickers
def download_2assets():
    symbols = ["AAPL", "MSFT"]
    multi = yf.download(symbols, period="", interval="", progress=False)
    multi.to_csv("AAPL_MSFT.csv", index=True)
    return multi

#stocks = download_2assets()


# --- 3) Download by specific date range
def download_from_date():
    start_date = "2024-01-01"
    end_date = "2025-01-01"
    range_df = yf.download("QQQ", start=start_date, end=end_date, progress=False)
    range_df.to_csv("NASDAQ.csv")
    return range_df

#from_date = download_from_date()



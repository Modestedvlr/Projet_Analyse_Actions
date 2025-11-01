import yfinance as yf
import os

def download_stock_data(tickers, start="2019-01-01", end="2025-01-01", output_dir="../data/raw/"):
    os.makedirs(output_dir, exist_ok=True)
    for ticker in tickers:
        print(f"Downloading {ticker}...")
        data = yf.download(ticker, start=start, end=end, auto_adjust=True)
        file_path = os.path.join(output_dir, f"{ticker}.csv")
        data.to_csv(file_path)
        print(f"Saved to {file_path}")

if __name__ == "__main__":
    tickers = ["BNP.PA", "MC.PA", "TTE.PA"]
    download_stock_data(tickers)

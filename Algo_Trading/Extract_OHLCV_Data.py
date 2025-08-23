import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

mt5.initialize()

# --- Config (edit as needed) ---
SYMBOL = "EURUSD"
TIMEFRAME = mt5.TIMEFRAME_M15
COUNT = 5000
CSV_FILE = f"{SYMBOL}_ohlc.csv"

if not mt5.symbol_select(SYMBOL, True):
    raise RuntimeError(f"symbol_select failed for {symbol}")
        
# --- Convert the Numpy Array to a DataFrame ---
def to_df(rates):
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.set_index('time', inplace=True)
    return df[["open", "high", "low", "close", "tick_volume"]]


# --------------- METHOD 1: copy_rates_from (backwards logic) ---------------
NOW = datetime.now()    # Start download from now and go backward
data1 = mt5.copy_rates_from(SYMBOL, TIMEFRAME, NOW, COUNT)
df1 = to_df(data1)
df1.to_csv(CSV_FILE.replace(".csv", "_from.csv"), index=True)


# --------------- METHOD 2: copy_rates_from_pos (backwards logic) ---------------
# Start 100 candles before the most recent one,
# then take `count` older bars from there
START_POS = 100
data2 = mt5.copy_rates_from_pos(SYMBOL, TIMEFRAME, START_POS, COUNT)
df2 = to_df(data2)
df2.to_csv(CSV_FILE.replace(".csv", "_from_pos.csv"), index=True)


# --------------- METHOD 3: copy_rates_range (NO backwards logic - explicit time window) ---------------
END = datetime.now()                    # Stop download at now
START = END - timedelta(hours=10)       # Start download from 10 hours ago and go forward
data3 = mt5.copy_rates_range(SYMBOL, TIMEFRAME, START, END)
df3 = to_df(data3)
df3.to_csv(CSV_FILE.replace(".csv", "_range.csv"), index=True)

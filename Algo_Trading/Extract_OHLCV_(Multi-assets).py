'''
video [en]: https://youtu.be/_HdrjqHIj_o?si=mVpS83L4ksl13AcB
video [fr]: https://youtu.be/lYZ3gSxqSMk?si=8iqVDgb1OXPKVYX2
'''


import MetaTrader5 as mt5
import pandas as pd
from tqdm import tqdm

# --- Config ---
SYMBOLS = ["EURUSD", "EURGBP", "NZDUSD", "AUDNZD", "US500", "USTEC"]
TIMEFRAME = mt5.TIMEFRAME_M15
START_POS = 0
COUNT = 20000

mt5.initialize()  # or full fonction as seen in the 1st video if it is disconnected 

def to_df(rates):  # Convert into readable date & time
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df.set_index("time")

data = {}
for sym in tqdm(SYMBOLS, desc='Extraction', bar_format={l_bar}{bar} | {remaining}):
    if not mt5.symbol_select(sym, True):
        raise RuntimeError(f"symbol_select failed for {sym}")
    rates = mt5.copy_rates_from_pos(sym, TIMEFRAME, START_POS, COUNT)
    data[sym] = to_df(rates)

mt5.shutdown()

# Example: access the EURUSD DataFrame
print(data["EURUSD"].head())

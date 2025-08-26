# ============================================
# MT5 - Open avec SL/TP (simple)
# ============================================
import MetaTrader5 as mt5
import os
from dotenv import load_dotenv

# --- Config ---
load_dotenv()
ACCOUNT_LOGIN    = int(os.getenv("MT5_LOGIN"))
ACCOUNT_PASSWORD = os.getenv("MT5_PASSWORD")
ACCOUNT_SERVER   = os.getenv("MT5_SERVER")

SYMBOL    = "EURGBP"
VOLUME    = 0.10
DEVIATION = 20
COMMENT   = "SL/TP demo"
MAGIC_A   = 101

# SL/TP
SL_POINTS = 200   # Remember to check the digits given by your broker (3,5 or 2,4)
TP_POINTS = 400   

# --- Init ---
if not mt5.initialize(login=ACCOUNT_LOGIN, server=ACCOUNT_SERVER, password=ACCOUNT_PASSWORD):
    raise RuntimeError(f"MT5 init failed: {mt5.last_error()}")
if not mt5.symbol_select(SYMBOL, True):
    raise RuntimeError(f"Failed to select {SYMBOL}")

info = mt5.symbol_info(SYMBOL)
tick = mt5.symbol_info_tick(SYMBOL)

# --- Open avec SL/TP ---
def open_long(magic, comment):
    price = tick.ask 
    sl = price - SL_POINTS * info.point
    tp = price + TP_POINTS * info.point

    req = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": VOLUME,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": round(sl, info.digits),
        "tp": round(tp, info.digits),
        "deviation": DEVIATION,
        "magic": magic,
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    r = mt5.order_send(req)
    print("OPEN:", r)
    return r

open_long(MAGIC_A, COMMENT)

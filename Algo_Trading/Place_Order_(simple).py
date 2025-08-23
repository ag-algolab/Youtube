# ============================================
# MT5 - Open and Close a Market Order (Simple)
# ============================================

import MetaTrader5 as mt5
from datetime import datetime
import os
from dotenv import load_dotenv

# --- Config ---
load_dotenv()
ACCOUNT_LOGIN    = int(os.getenv("MT5_LOGIN")) 
ACCOUNT_PASSWORD = os.getenv("MT5_PASSWORD")
ACCOUNT_SERVER   = os.getenv("MT5_SERVER") 

SYMBOL = "BTCUSD"
VOLUME = 0.10
DEVIATION = 20
COMMENT = "Basic order"

# --- Init ---
if not mt5.initialize(login=ACCOUNT_LOGIN, server=ACCOUNT_SERVER, password=ACCOUNT_PASSWORD):
    raise RuntimeError(f"MT5 init failed: {mt5.last_error()}")

if not mt5.symbol_select(SYMBOL, True):
    raise RuntimeError(f"Failed to select {SYMBOL}")

# --- Open a BUY order ---
buy_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": SYMBOL,
    "volume": VOLUME,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(SYMBOL).ask,
    "deviation": DEVIATION,
    "comment": COMMENT,
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK,
}


# --- Close the order (send SELL of same volume) ---
close_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": SYMBOL,
    "volume": VOLUME,
    "type": mt5.ORDER_TYPE_SELL,
    "position": buy_result.order,   # close the opened position
    "price": mt5.symbol_info_tick(SYMBOL).bid,
    "deviation": DEVIATION,
    "comment": "Close order",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK,
}


# ===== Execution =====

buy_result = mt5.order_send(buy_request)
print("BUY result:", buy_result)

close_result = mt5.order_send(close_request)
print("CLOSE result:", close_result)

mt5.shutdown()

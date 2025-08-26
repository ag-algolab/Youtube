# ============================================
# MT5 - Magic demo: open 2, close only MAGIC_A
# ============================================
import time
import MetaTrader5 as mt5
import os
from dotenv import load_dotenv

# --- Config ---
load_dotenv()
ACCOUNT_LOGIN    = int(os.getenv("MT5_LOGIN"))
ACCOUNT_PASSWORD = os.getenv("MT5_PASSWORD")
ACCOUNT_SERVER   = os.getenv("MT5_SERVER")

SYMBOL   = "EURGBP"
VOLUME   = 0.10
DEVIATION = 20
COMMENT  = "Magic demo"
MAGIC_A  = 101   # bot A
MAGIC_B  = 102   # bot B

# --- Init ---
if not mt5.initialize(login=ACCOUNT_LOGIN, server=ACCOUNT_SERVER, password=ACCOUNT_PASSWORD):
    raise RuntimeError(f"MT5 init failed: {mt5.last_error()}")
if not mt5.symbol_select(SYMBOL, True):
    raise RuntimeError(f"Failed to select {SYMBOL}")

# --- Helper: open market order ---
def open_order(order_type, magic, comment):
    tick = mt5.symbol_info_tick(SYMBOL)
    price = tick.ask if order_type == mt5.ORDER_TYPE_BUY else tick.bid
    req = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": VOLUME,
        "type": order_type,
        "price": price,
        "deviation": DEVIATION,
        "magic": magic,
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    return mt5.order_send(req)

# --- Open two orders (different MAGIC) ---
r1 = open_order(mt5.ORDER_TYPE_BUY,  MAGIC_A, f"{COMMENT} A")
r2 = open_order(mt5.ORDER_TYPE_BUY,  MAGIC_B, f"{COMMENT} B")
print("OPEN A:", r1)
print("OPEN B:", r2)

time.sleep(0.5)  # laisse MT5 créer la/les positions

# --- Close only positions belonging to MAGIC_A ---
def close_order(magic):
  positions = mt5.positions_get(symbol=SYMBOL) or []
  for p in positions:
      if p.magic != magic:
          continue
      tick = mt5.symbol_info_tick(p.symbol)
      close_req = {
          "action": mt5.TRADE_ACTION_DEAL,
          "symbol": p.symbol,
          "volume": p.volume,            
          "type": mt5.ORDER_TYPE_SELL,
          "price": tick.bid,
          "position": p.ticket,          
          "deviation": DEVIATION,
          "comment": f"Close magic{magic}",
          "type_time": mt5.ORDER_TIME_GTC,
          "type_filling": mt5.ORDER_FILLING_IOC,
      }
      r_close = mt5.order_send(close_req)
      print("CLOSE:", r_close)

close_order(MAGIC_B)

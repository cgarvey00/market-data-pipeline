from datetime import datetime, timezone
import json
import random
import time
import uuid

SYMBOLS = ["AAPL", "MSFT", "NVDA", "TSLA", "GOOG", "JPM", "BAC"]


def generate_market_event():
    symbol = random.choice(SYMBOLS)

    bid_price = round(random.uniform(100, 500), 2)
    ask_price = round(bid_price + random.uniform(0.01, 0.10), 2)
    trade_price = round(random.uniform(bid_price, ask_price), 2)

    bid_size = random.randint(100, 5000)
    ask_size = random.randint(100, 5000)
    trade_volume = random.randint(1, 10000)

    now = datetime.now(timezone.utc)

    return {
        "tradeId": f"TRD-{uuid.uuid4()}",
        "symbol": symbol,
        "exchange": "NASDAQ",
        "currency": "USD",
        "tradePrice": trade_price,
        "tradeVolume": trade_volume,
        "bidPrice": bid_price,
        "askPrice": ask_price,
        "bidSize": bid_size,
        "askSize": ask_size,
        "spread": round(ask_price - bid_price, 2),
        "midPrice": round((bid_price + ask_price) / 2, 2),
        "windowStart": now.isoformat(),
        "windowEnd": now.isoformat(),
        "tradeTimestamp": now.isoformat(),
        "ingestionTimestamp": now.isoformat(),
        "quoteCondition": "REGULAR",
        "tradeCondition": "AT_LAST",
        "totalVolume": random.randint(1_000_000, 50_000_000),
        "sessionVolume": random.randint(100_000, 5_000_000),
        "totalOTCVolume": random.randint(1_000, 500_000),
        "totalLitVolume": random.randint(100_000, 5_000_000),
        "vwap": round(random.uniform(100, 500), 2),
        "openPrice": round(random.uniform(100, 500), 2),
        "highPrice": round(random.uniform(100, 500), 2),
        "lowPrice": round(random.uniform(100, 500), 2),
        "closePricePrevious": round(random.uniform(100, 500), 2),
        "source": "market-feed-simulator",
        "sequenceNumber": random.randint(1_000_000, 9_999_999),
    }


if __name__ == "__main__":
    while True:
        event = generate_market_event()
        print(json.dumps(event, indent=4))
        time.sleep(1)

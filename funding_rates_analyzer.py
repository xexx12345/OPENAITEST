import argparse
from typing import List
import ccxt


def get_top_symbols(limit: int = 5) -> List[str]:
    """Return a list of top crypto perpetual symbols."""
    # Simple predefined list for demonstration
    universe = [
        "BTC/USDT",
        "ETH/USDT",
        "BNB/USDT",
        "XRP/USDT",
        "SOL/USDT",
    ]
    return universe[:limit]


def fetch_funding_rates(exchange: ccxt.Exchange, symbols: List[str]):
    rates = {}
    for symbol in symbols:
        try:
            info = exchange.fetch_funding_rate(symbol)
            rates[symbol] = info["fundingRate"]
        except Exception as err:
            print(f"Failed to fetch {symbol}: {err}")
    return rates


def main():
    parser = argparse.ArgumentParser(description="Funding rates analyzer")
    parser.add_argument("--exchange", default="binance", help="Exchange id (default: binance)")
    parser.add_argument("--limit", type=int, default=5, help="Number of top symbols to fetch")
    args = parser.parse_args()

    exchange_class = getattr(ccxt, args.exchange)
    exchange = exchange_class({"enableRateLimit": True})
    symbols = get_top_symbols(args.limit)
    rates = fetch_funding_rates(exchange, symbols)

    if not rates:
        print("No funding rates fetched")
        return

    print("\nFunding Rates:")
    for symbol, rate in rates.items():
        direction = "longs pay shorts" if rate > 0 else "shorts pay longs"
        print(f"{symbol}: {rate:.6%} ({direction})")


if __name__ == "__main__":
    main()

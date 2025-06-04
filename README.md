# OPENAITEST

This repository contains examples for using various Python tools.

## Funding Rates Analyzer

`funding_rates_analyzer.py` fetches recent funding rates for popular crypto perpetual pairs using the [ccxt](https://github.com/ccxt/ccxt) library. The top symbols are predefined (BTC/USDT, ETH/USDT, BNB/USDT, XRP/USDT, SOL/USDT).

### Usage

```bash
pip install ccxt
python funding_rates_analyzer.py --exchange binance --limit 5
```

By default the script fetches data from Binance and prints the funding rate for each symbol with an indicator of whether longs or shorts pay.

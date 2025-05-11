# Launch Pad Trading Strategy Backtest

This repository demonstrates a proprietary trading strategy backtest implemented in Python, applied to daily DOGE (Dogecoin) price data. The strategy employs technical indicators to generate trading signals and manages positions to maintain a single trade (long or short) at a time. The specific trading logic is proprietary and has been masked to protect intellectual property. This project serves to showcase my expertise in quantitative finance, data analysis, and visualization.

## Backtest Results

The backtest was conducted on daily DOGE price data with an initial capital of $100,000. The results are as follows:

- Total Trades: 271
- Buy Trades (Long): 84
- Sell Trades (Short): 187
- Win Rate: 70.11%
- Initial Capital: $100,000.00
- Final Portfolio Value: $763,508.47
- Total Profit/Loss: $663,508.47 (663.51%)
- Maximum Drawdown: -29.91%
- Sharpe Ratio: 2.13
## The strategy was also validated on TradingView using Pine Script on the DOGE daily timeframe, covering the entire historical data from the initial period, yielding:

- Total Profit: 1007.59%
- Profitable Trades: 29%
- Profit Factor: 15.23
- Total Trades: 55
<img width="1317" alt="Screenshot 2025-05-11 at 11 56 28" src="https://github.com/user-attachments/assets/f4feb475-e863-42b9-92f2-f7e4e01d74dc" />

## Visualizations

The script generates four high-quality plots to evaluate the strategy's performance:

### Equity Curve: Displays portfolio value over time with drawdown periods shaded and a secondary axis for percentage returns.
![equity_curve](https://github.com/user-attachments/assets/035a6c04-578a-4e1e-b826-9d08f5be3d00)

### Monthly Returns: Bar chart of monthly returns, with positive returns in green and negative in red.
![monthly_returns](https://github.com/user-attachments/assets/15e4590d-e6e0-495f-b185-98abfbf2840d)

### Drawdown: Plot of drawdown percentage over time, highlighting the maximum drawdown.
![drawdown](https://github.com/user-attachments/assets/b152289f-ecdb-424f-83e5-0d924d561f10)

### Live Trades: Step plot showing the number of active trades (0 or 1) over time.
![live_trades](https://github.com/user-attachments/assets/c9504b00-06f3-4b13-8d8a-5c80b4f6e6a8)

## License

This project is protected by an "All rights reserved" license (see LICENSE). The code, strategy, and associated materials are proprietary and may not be used, reproduced, modified, or distributed for any purpose (personal, commercial, or educational) without explicit permission.

## Disclaimer

This repository is for showcasing my work and is not intended for use in live trading or investment decisions. The results are from a backtest and do not guarantee future performance.

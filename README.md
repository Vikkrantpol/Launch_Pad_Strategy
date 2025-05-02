SMA Crossover Strategy Backtest

This project implements a Simple Moving Average (SMA) Crossover Strategy for backtesting on historical financial data. It generates buy and sell signals based on the crossover of three SMAs (21, 50, and 65 periods), incorporates position sizing and trade limits, and calculates performance metrics. The code processes daily data from a CSV file (e.g., newdata1d.csv), computes portfolio performance, and generates visualizations.

The purpose is to assess the profitability and risk of the SMA crossover strategy through metrics like total profit/loss, win rate, maximum drawdown, and Sharpe ratio.

Features

SMA Calculations: Calculates 21, 50, and 65-period Simple Moving Averages on closing prices to detect trends.
Signal Generation: Triggers buy signals when 21 SMA > 50 SMA > 65 SMA (bullish trend) and sell signals when 65 SMA > 50 SMA > 21 SMA (bearish trend).
Position Sizing: Allocates 4% of the initial $100,000 capital per trade to manage risk.
Trade Limits: Restricts concurrent trades to 25, ensuring full capital utilization without over-leveraging.

Backtesting Metrics:
Total Trades: Tracks the number of buy and sell trades.
Win Rate: Computes the percentage of trades with positive returns.
Total Profit/Loss: Calculates the final portfolio value and percentage return.
Maximum Drawdown: Measures the largest peak-to-trough portfolio decline to evaluate risk.
Sharpe Ratio: Assesses risk-adjusted returns using annualized daily returns (risk-free rate = 0).

Visualizations:

Portfolio Value Plot: Shows portfolio value over time with buy/sell signals.
Drawdown Plot: Displays percentage drawdown to highlight risk periods.
Live Trades Plot: Tracks the number of active trades over time.
Data Processing: Converts UNIX timestamps to datetime and sorts data chronologically.

Output: Prints metrics to the console and saves plots as portfolio_value.png, drawdown.png, and live_trades.png.

Results:

Backtest results on newdata1d.csv:

Total Trades: 287
Buy Trades: 171
Sell Trades: 116
Win Rate: 59.23%
Initial Capital: $100,000
Final Portfolio Value: $150,315.46
Total Profit/Loss: $50,315.46 (50.32%)
Maximum Drawdown: -22.02%
Sharpe Ratio: 0.89

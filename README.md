# SMA Crossover Strategy Backtest

This project implements a Simple Moving Average (SMA) Crossover Strategy for backtesting on historical financial data. It generates buy and sell signals based on the crossover of three SMAs (21, 50, and 65 periods), incorporates position sizing and trade limits, and calculates performance metrics. The code processes daily data from a CSV file (e.g., newdata1d.csv), computes portfolio performance, and generates visualizations.

The purpose is to assess the profitability and risk of the SMA crossover strategy through metrics like total profit/loss, win rate, maximum drawdown, and Sharpe ratio.

## Results:

### Python Script Results
Backtest results on newdata1d.csv: (Tested for daily timeframe) (Date since 29-Dec-2023)

- **Total Trades**: 287
- **Buy Trades**: 171
- **Sell Trades**: 116
- **Win Rate**: 59.23%
- **Initial Capital**: $100,000
- **Final Portfolio Value**: $150,315.46
- **Total Profit/Loss**: $50,315.46 (50.32%)
- **Maximum Drawdown**: -22.02%
- **Sharpe Ratio**: 0.89

### TradingView Results (Daily Timeframe)
The same SMA Crossover Strategy (21, 50, 65 periods) was tested on TradingView using a daily timeframe, yielding the following results:
- **Total Trades**: 58
- **Profitable Trades**: 39.66% (23/58 trades)
- **Total Profit/Loss**: $5,418,338.48 (541.84%)
- **Maximum Drawdown**: $138,830.32 (4.13%)
- **Profit Factor**: 9.505
  
## Output Plots

The script generates three visualization plots to analyze the strategy's performance. These plots are saved as PNG files in the project directory and are included below for reference.

1. **Portfolio Value Plot**  
   Displays the portfolio value over time, with green triangles marking buy signals and red triangles marking sell signals.  
   ![portfolio_value](https://github.com/user-attachments/assets/8ec75894-bf76-4828-a5b8-b29309482824)

2. **Drawdown Plot**  
   Shows the percentage drawdown over time, highlighting periods of portfolio decline to assess risk.  
   ![drawdown](https://github.com/user-attachments/assets/811550f1-4976-4167-a286-3d3a0631839c)

3. **Live Trades Plot**  
   Tracks the number of concurrent trades over time, illustrating capital utilization.  
   ![live_trades](https://github.com/user-attachments/assets/f54a083b-2419-4f8b-83e1-2dd272618f0b)
   
5. **TradingView Equity and Drawdown Plot**  
   Shows the equity curve (cyan line) and drawdown (shaded area) for the SMA Crossover Strategy on a daily timeframe, with key metrics like Total P&L, Max Drawdown, and Profit        Factor displayed above the plot.
   ![TradingView Results](<img width="1323" alt="Screenshot 2025-05-02 at 13 24 49" src="https://github.com/user-attachments/assets/9d0c94e3-25df-464d-91d4-7e76582f1c1c" />)

## Features

SMA Calculations: Calculates 21, 50, and 65-period Simple Moving Averages on closing prices to detect trends.
Signal Generation: Triggers buy signals when 21 SMA > 50 SMA > 65 SMA (bullish trend) and sell signals when 65 SMA > 50 SMA > 21 SMA (bearish trend).
Position Sizing: Allocates 4% of the initial $100,000 capital per trade to manage risk.
Trade Limits: Restricts concurrent trades to 25, ensuring full capital utilization without over-leveraging.

## Backtesting Metrics:
Total Trades: Tracks the number of buy and sell trades.
Win Rate: Computes the percentage of trades with positive returns.
Total Profit/Loss: Calculates the final portfolio value and percentage return.
Maximum Drawdown: Measures the largest peak-to-trough portfolio decline to evaluate risk.
Sharpe Ratio: Assesses risk-adjusted returns using annualized daily returns (risk-free rate = 0).

## Visualizations:

Portfolio Value Plot: Shows portfolio value over time with buy/sell signals.
Drawdown Plot: Displays percentage drawdown to highlight risk periods.
Live Trades Plot: Tracks the number of active trades over time.
Data Processing: Converts UNIX timestamps to datetime and sorts data chronologically.

## Output: Prints metrics to the console and saves plots as portfolio_value.png, drawdown.png, and live_trades.png.





## File Structure:

sma-crossover-strategy/
├── sma_crossover.py          # Backtesting script
├── newdata1d.csv            # User-provided input data
├── portfolio_value.png       # Portfolio value plot
├── drawdown.png             # Drawdown plot
├── live_trades.png          # Live trades plot
├── README.md                # Documentation

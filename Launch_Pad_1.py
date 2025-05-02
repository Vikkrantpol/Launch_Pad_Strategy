import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file (replace 'btc_data.csv' with your actual file path)
df = pd.read_csv('newdata1d.csv')

# Ensure the 'time' column is in datetime format (assuming 'time' is in UNIX timestamp)
df['time'] = pd.to_datetime(df['time'], unit='s')

# Sort the data by time to ensure chronological order
df = df.sort_values('time')

# Calculate SMAs
df['SMA_21'] = df['close'].rolling(window=21).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()
df['SMA_65'] = df['close'].rolling(window=65).mean()

# Initialize columns for signals and positions
df['Signal'] = 0  # 1 for Buy, -1 for Sell, 0 for Hold
df['Position'] = 0  # 1 for holding a position, 0 for no position

# Generate signals based on SMA crossover conditions
for i in range(1, len(df)):
    # Buy signal: 21 SMA > 50 SMA > 65 SMA
    if (df['SMA_21'].iloc[i] > df['SMA_50'].iloc[i] > df['SMA_65'].iloc[i]):
        df.loc[i, 'Signal'] = 1
    # Sell signal: 65 SMA > 50 SMA > 21 SMA
    elif (df['SMA_65'].iloc[i] > df['SMA_50'].iloc[i] > df['SMA_21'].iloc[i]):
        df.loc[i, 'Signal'] = -1

# Calculate positions (holding or not)
position = 0
for i in range(len(df)):
    if df['Signal'].iloc[i] == 1:  # Buy signal
        position = 1
    elif df['Signal'].iloc[i] == -1:  # Sell signal
        position = 0
    df.loc[i, 'Position'] = position

# Calculate returns
df['Returns'] = df['close'].pct_change()
df['Strategy_Returns'] = df['Position'].shift(1) * df['Returns']

# Backtesting metrics
initial_capital = 100000  # Starting capital in USD
df['Portfolio_Value'] = initial_capital * (1 + df['Strategy_Returns']).cumprod()

# Total trades
buy_trades = len(df[df['Signal'] == 1])
sell_trades = len(df[df['Signal'] == -1])
total_trades = buy_trades + sell_trades

# Win rate
winning_trades = len(df[df['Strategy_Returns'] > 0])
losing_trades = len(df[df['Strategy_Returns'] < 0])
win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0

# Total profit/loss
final_portfolio_value = df['Portfolio_Value'].iloc[-1]
total_profit_loss = final_portfolio_value - initial_capital
total_profit_loss_percent = (total_profit_loss / initial_capital) * 100

# Maximum drawdown
rolling_max = df['Portfolio_Value'].cummax()
drawdown = (df['Portfolio_Value'] - rolling_max) / rolling_max
df['Drawdown'] = drawdown * 100  # Store drawdown percentage for plotting
max_drawdown = df['Drawdown'].min()

# Sharpe ratio (assuming risk-free rate = 0 for simplicity)
strategy_returns = df['Strategy_Returns'].dropna()
sharpe_ratio = (strategy_returns.mean() / strategy_returns.std()) * np.sqrt(252) if strategy_returns.std() != 0 else 0

# Plot 1: Portfolio Value over Time with Buy/Sell Signals
plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['Portfolio_Value'], label='Portfolio Value', color='blue')
plt.scatter(df[df['Signal'] == 1]['time'], df[df['Signal'] == 1]['Portfolio_Value'], 
            label='Buy Signal', color='green', marker='^', s=100)
plt.scatter(df[df['Signal'] == -1]['time'], df[df['Signal'] == -1]['Portfolio_Value'], 
            label='Sell Signal', color='red', marker='v', s=100)
plt.title('Portfolio Value Over Time with Buy/Sell Signals')
plt.xlabel('Time')
plt.ylabel('Portfolio Value (USD)')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('portfolio_value.png')

# Plot 2: Drawdown Over Time
plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['Drawdown'], label='Drawdown (%)', color='red')
plt.fill_between(df['time'], df['Drawdown'], 0, alpha=0.2, color='red')
plt.title('Drawdown Over Time')
plt.xlabel('Time')
plt.ylabel('Drawdown (%)')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('drawdown.png')

# Print backtesting results
print("=== SMA Crossover Strategy Backtest Results ===")
print(f"Total Trades: {total_trades}")
print(f"Buy Trades: {buy_trades}")
print(f"Sell Trades: {sell_trades}")
print(f"Win Rate: {win_rate:.2f}%")
print(f"Initial Capital: ${initial_capital:,.2f}")
print(f"Final Portfolio Value: ${final_portfolio_value:,.2f}")
print(f"Total Profit/Loss: ${total_profit_loss:,.2f} ({total_profit_loss_percent:.2f}%)")
print(f"Maximum Drawdown: {max_drawdown:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print("Plots saved as 'portfolio_value.png' and 'drawdown.png'")

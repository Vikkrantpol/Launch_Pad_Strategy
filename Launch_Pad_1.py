import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for improved aesthetics
sns.set_style("whitegrid")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.dpi': 300
})

# Load the CSV file (replace 'DOGEdata1d.csv' with your actual file path)
df = pd.read_csv('DOGEdata1d.csv')

# Ensure the 'time' column is in datetime format (assuming 'time' is in UNIX timestamp)
df['time'] = pd.to_datetime(df['time'], unit='s')

# Sort the data by time to ensure chronological order
df = df.sort_values('time')

# Calculate technical indicators (masked for proprietary reasons)
# Original strategy used specific moving averages; placeholders used here
df['Indicator_1'] = df['close'].rolling(window=20).mean()  # Placeholder
df['Indicator_2'] = df['close'].rolling(window=40).mean()  # Placeholder
df['Indicator_3'] = df['close'].rolling(window=60).mean()  # Placeholder

# Initialize columns for signals and positions
df['Signal'] = 0  # 1 for Buy (Go Long), -1 for Sell (Go Short), 0 for Hold
df['Position'] = 0  # 1 for Long, -1 for Short, 0 for Neutral

# Proprietary signal generation and position logic (masked)
# Original strategy used specific indicator conditions and ensured single trade
for i in range(1, len(df)):
    # Placeholder: Proprietary signal generation logic
    # Original logic used custom conditions to set Signal = 1, -1, or 0
    df.loc[i, 'Signal'] = np.random.choice([0, 1, -1], p=[0.7, 0.15, 0.15])  # Dummy random signals
    
    # Placeholder: Proprietary position management logic
    # Original logic ensured only one trade (long or short) at a time
    if df.loc[i, 'Signal'] == 1:
        df.loc[i, 'Position'] = 1
    elif df.loc[i, 'Signal'] == -1:
        df.loc[i, 'Position'] = -1
    else:
        df.loc[i, 'Position'] = df.loc[i-1, 'Position'] if i > 0 else 0

# Calculate number of live trades (0 or 1, since only one trade at a time)
df['Live_Trades'] = (df['Position'] != 0).astype(int)

# Calculate returns with position sizing
initial_capital = 100000  # Starting capital in USD
position_size_percentage = 1.0  # 100% of capital per trade (single trade)
df['Returns'] = df['close'].pct_change()
df['Strategy_Returns'] = position_size_percentage * df['Position'].shift(1) * df['Returns']

# Backtesting metrics
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
df['Drawdown'] = drawdown * 100
max_drawdown = df['Drawdown'].min()

# Sharpe ratio (risk-free rate = 0)
strategy_returns = df['Strategy_Returns'].dropna()
sharpe_ratio = (strategy_returns.mean() / strategy_returns.std()) * np.sqrt(252) if strategy_returns.std() != 0 else 0

# Calculate monthly returns
df['YearMonth'] = df['time'].dt.to_period('M')
monthly_returns = df.groupby('YearMonth')['Strategy_Returns'].sum() * 100
monthly_returns.index = monthly_returns.index.to_timestamp()

# Plot 1: Enhanced Equity Curve (No Buy/Sell Signals)
plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['Portfolio_Value'], label='Equity Curve', color='royalblue', linewidth=3, zorder=2)
plt.plot(df['time'], df['Portfolio_Value'], color='lightblue', linewidth=5, alpha=0.5, zorder=1)
plt.fill_between(df['time'], initial_capital, df['Portfolio_Value'], 
                 where=(df['Portfolio_Value'] < rolling_max), 
                 facecolor='salmon', alpha=0.15, label='Drawdown Periods')
plt.axhline(initial_capital, color='gray', linestyle='--', linewidth=1.5, label='Initial Capital')
ax1 = plt.gca()
ax2 = ax1.twinx()
ax2.set_ylabel('Percentage Return (%)', color='green')
ax2.plot(df['time'], (df['Portfolio_Value'] / initial_capital - 1) * 100, color='green', alpha=0.5, linewidth=1)
ax2.tick_params(axis='y', labelcolor='green')
plt.title('Equity Curve with Drawdown Periods', fontsize=18, fontweight='bold')
ax1.set_xlabel('Time', fontsize=14)
ax1.set_ylabel('Portfolio Value (USD)', fontsize=14)
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('equity_curve.png')
plt.close()

# Plot 2: Monthly Returns
plt.figure(figsize=(14, 7))
colors = ['green' if x >= 0 else 'red' for x in monthly_returns]
bars = plt.bar(monthly_returns.index, monthly_returns, color=colors, width=20)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.1f}%', 
             ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10)
plt.axhline(0, color='black', linestyle='-', linewidth=1)
plt.title('Monthly Returns')
plt.xlabel('Month')
plt.ylabel('Return (%)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_returns.png')
plt.close()

# Plot 3: Enhanced Drawdown Plot
plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['Drawdown'], label='Drawdown (%)', color='red', linewidth=2)
plt.fill_between(df['time'], df['Drawdown'], 0, alpha=0.3, color='red')
plt.axhline(max_drawdown, color='black', linestyle='--', alpha=0.7, 
            label=f'Max Drawdown: {max_drawdown:.2f}%')
plt.title('Drawdown Over Time')
plt.xlabel('Time')
plt.ylabel('Drawdown (%)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('drawdown.png')
plt.close()

# Plot 4: Live Trades Over Time (Step Plot)
plt.figure(figsize=(14, 7))
plt.step(df['time'], df['Live_Trades'], label='Live Trades', color='purple', linewidth=2, where='post')
trade_changes = df[df['Live_Trades'].diff() != 0][['time', 'Live_Trades']].iloc[:3]
for idx, row in trade_changes.iterrows():
    label = 'Enter Trade' if row['Live_Trades'] == 1 else 'Exit Trade'
    plt.annotate(label, (row['time'], row['Live_Trades']), 
                 xytext=(0, 15), textcoords='offset points', color='purple', fontsize=10)
plt.title('Number of Live Trades Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Live Trades')
plt.ylim(-0.1, 1.1)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('live_trades.png')
plt.close()

# Print backtesting results
print("=== Trading Strategy Backtest Results ===")
print(f"Total Trades: {total_trades}")
print(f"Buy Trades (Long): {buy_trades}")
print(f"Sell Trades (Short): {sell_trades}")
print(f"Win Rate: {win_rate:.2f}%")
print(f"Initial Capital: ${initial_capital:,.2f}")
print(f"Final Portfolio Value: ${final_portfolio_value:,.2f}")
print(f"Total Profit/Loss: ${total_profit_loss:,.2f} ({total_profit_loss_percent:.2f}%)")
print(f"Maximum Drawdown: {max_drawdown:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print("Plots saved as 'equity_curve.png', 'monthly_returns.png', 'drawdown.png', and 'live_trades.png'")

import pandas as pd
from strategies.rsi import execute_rsi_strategy

def run_backtest(strategy, data):
    results = []
    for _, row in data.iterrows():
        decision = strategy({"price": row["price"]})
        results.append({"date": row["date"], "price": row["price"], "decision": decision})
    return pd.DataFrame(results)

if __name__ == "__main__":
    # Simulated test data
    test_data = pd.DataFrame({
        "date": pd.date_range(start="2022-01-01", periods=100),
        "price": pd.Series(range(100)) + 100
    })
    df_results = run_backtest(execute_rsi_strategy, test_data)
    print(df_results.tail())
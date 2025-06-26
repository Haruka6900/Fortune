import os
import os
import json
import random
from datetime import datetime
from strategies.rsi import execute_rsi_strategy
from strategies.macd import execute_macd_strategy
from strategies.grid import execute_grid_strategy
from strategies.dca import execute_dca_strategy
from strategies.scalping import execute_scalping_strategy
from strategies.trend import execute_trend_strategy
from strategies.breakout import execute_breakout_strategy
from strategies.ai_sentiment import execute_ai_sentiment_strategy

STRATEGIES = [
    execute_rsi_strategy,
    execute_macd_strategy,
    execute_grid_strategy,
    execute_dca_strategy,
    execute_scalping_strategy,
    execute_trend_strategy,
    execute_breakout_strategy,
    execute_ai_sentiment_strategy
]

def load_memory(path=os.path.join(os.path.dirname(__file__), '../memory/trading_memory.json')):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory, path=os.path.join(os.path.dirname(__file__), '../memory/trading_memory.json')):
    with open(path, 'w') as f:
        json.dump(memory, f, indent=2)

def get_market_data():
    # Dummy data for now
    return {"price": random.uniform(100, 200)}

def main():
    memory = load_memory()
    data = get_market_data()

    votes = {"buy": 0, "sell": 0, "hold": 0}

    for strategy in STRATEGIES:
        decision = strategy(data)
        votes[decision] += 1

    final_decision = max(votes, key=votes.get)

    now = datetime.now().isoformat()
    memory[now] = {
        "data": data,
        "decision": final_decision,
        "votes": votes
    }

    save_memory(memory)
    print(f"Time: {now}, Decision: {final_decision}, Votes: {votes}")

if __name__ == "__main__":
    main()
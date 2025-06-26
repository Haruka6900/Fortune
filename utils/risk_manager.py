def calculate_position_size(balance, risk_per_trade, stop_loss_distance):
    if stop_loss_distance == 0:
        return 0
    return (balance * risk_per_trade) / stop_loss_distance

def should_enter_trade(current_drawdown, max_drawdown=0.2):
    return current_drawdown < max_drawdown

def enforce_trade_limits(trade_history, max_trades_per_day=10):
    from datetime import datetime
    today = datetime.now().date()
    today_trades = [t for t in trade_history if t.get("date") == str(today)]
    return len(today_trades) < max_trades_per_day
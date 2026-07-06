import plotly.express as px
import pandas as pd

valuations = pd.read_csv('../data/raw/player_valuations.csv')

def plot_valuation_history(player_id):
    player_valuations = valuations[valuations["player_id"] == player_id][["date", "market_value_in_eur"]].sort_values(by="date", ascending=True) 
    fig = px.line(player_valuations, x="date", y="market_value_in_eur", title="Player Valuation History")
    return fig

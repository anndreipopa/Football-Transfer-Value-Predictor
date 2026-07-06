import pandas as pd

players = pd.read_csv('../data/processed/players_clean.csv')
valuations = pd.read_csv('../data/raw/player_valuations.csv')

def build_player_profile(player_id):
    selected_player = players[players["player_id"] == player_id].iloc[0]
    player_valuations = valuations[valuations["player_id"] == player_id].sort_values(by="date", ascending=False)
    latest_valuation = player_valuations.iloc[0]

    profile = {
        "name" : selected_player["name"],
        "country" : selected_player["country_of_citizenship"],
        "position" : selected_player["sub_position"],
        "club" : selected_player["current_club_name"],
        "date_of_birth" : selected_player["date_of_birth"],
        "latest_market_value" : latest_valuation["market_value_in_eur"]
    }
    return profile

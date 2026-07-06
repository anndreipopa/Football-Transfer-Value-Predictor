import pandas as pd
from datetime import date

players = pd.read_csv('./data/raw/players.csv')
valuations = pd.read_csv('./data/raw/player_valuations.csv')

players_clean = players.copy()

valid_players_ids = valuations["player_id"].unique()

players_clean = players_clean[players_clean["player_id"].isin(valid_players_ids)]

players_clean["date_of_birth"] = pd.to_datetime(players_clean["date_of_birth"])

def validation_checks():
    print(players_clean["player_id"].isin(valid_players_ids).all())
    print(players_clean["player_id"].is_unique)
    print(players_clean["player_code"].str.contains("Messi", na=False, case=False).any())
    print(players_clean["date_of_birth"].dtype)

validation_checks()

players_clean.to_csv('./data/processed/players_clean.csv')





#print(f"Original players: {len(players)}")
#print(f"Clean players: {len(players_clean)}")
#print(f"Removed players: {len(players) - len(players_clean)}")

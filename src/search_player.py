import pandas as pd

player_data = pd.read_csv("../data/processed/players_clean.csv")


def search_players(search_term):
    matching_mask = player_data["player_code"].str.contains(
        search_term,
        case=False,
        na=False
    )

    return player_data[matching_mask].reset_index(drop=True)
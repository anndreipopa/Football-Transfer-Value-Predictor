import streamlit as st

import search_player as sp
import build_profile as bp
import plot_history as ph

st.set_page_config(
    page_title="Football Market Value Explorer",
    layout="wide"
)

st.title("Football Market Value Explorer")

search_term = st.text_input("Search player")

if search_term:

    matching_players = sp.search_players(search_term)

    if matching_players.empty:
        st.warning("No players found.")
        st.stop()

    player_options = (
        matching_players["name"]
    )

    selected_name = st.selectbox(
        "Select player",
        player_options
    )

    selected_player = matching_players[
        player_options == selected_name
    ].iloc[0]

    player_id = selected_player["player_id"]

    profile = bp.build_player_profile(player_id)

    st.subheader(profile["name"])

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Country:** {profile['country']}")
        st.write(f"**Club:** {profile['club']}")
        st.write(f"**Position:** {profile['position']}")

    with col2:
        st.write(f"**Date of Birth:** {profile['date_of_birth']}")
        st.write(f"**Latest Market Value:** €{profile['latest_market_value']:,}")

    fig = ph.plot_valuation_history(player_id)
    st.plotly_chart(fig, use_container_width=True)
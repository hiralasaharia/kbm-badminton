
# badminton_score_tracker.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Badminton Match Tracker", layout="wide")

st.title("🏸 Badminton Match Tracker - 6 Teams")

# Initialize team names
teams = [f"Team {i}" for i in range(1, 7)]

# Initialize team scores
if "scores" not in st.session_state:
    st.session_state.scores = {team: 0 for team in teams}

# Match tracking (8 total matches)
matches = [f"Match {i}" for i in range(1, 9)]

if "match_results" not in st.session_state:
    st.session_state.match_results = {match: None for match in matches}

st.header("Match Results Entry")

for match in matches:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown(f"### {match}")
    with col2:
        team_a = st.selectbox(f"{match} - Team A", teams, key=f"{match}_a")
    with col3:
        team_b = st.selectbox(f"{match} - Team B", teams, key=f"{match}_b")

    winner = st.radio(f"{match} - Who won?", [team_a, team_b, "Not Played"], horizontal=True, key=f"{match}_win")

    if winner != "Not Played":
        if st.session_state.match_results[match] != winner:
            previous = st.session_state.match_results[match]
            if previous and previous in st.session_state.scores:
                st.session_state.scores[previous] -= 1
            st.session_state.match_results[match] = winner
            st.session_state.scores[winner] += 1

st.header("Team Scores")
score_df = pd.DataFrame.from_dict(st.session_state.scores, orient="index", columns=["Points"])
score_df = score_df.sort_values(by="Points", ascending=False)
st.dataframe(score_df)

if st.button("Reset All Data"):
    st.session_state.scores = {team: 0 for team in teams}
    st.session_state.match_results = {match: None for match in matches}
    st.success("Data has been reset!")

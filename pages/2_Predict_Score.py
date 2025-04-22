import streamlit as st
import numpy as np
from function_epl import *

st.header("Let's See the Score!")

roll_df = rolling_home(df)
roll_df = rolling_home_away(roll_df)
roll_df = sort_data(roll_df)
roll_df = encode_data(roll_df)
roll_df_normal = normalization_data(roll_df)

left, right = st.columns(2)
with left:
  home_team = st.selectbox("Choose Home Team",
                         ('Manchester Utd', 'Ipswich Town', 'Newcastle Utd', "Nott'ham Forest",
                          'Everton', 'Arsenal', 'West Ham', 'Brentford', 'Chelsea', 'Leicester City',
                          'Brighton', 'Tottenham', 'Fulham', 'Crystal Palace', 'Manchester City',
                          'Southampton', 'Aston Villa', 'Bournemouth', 'Wolves', 'Liverpool', 'Watford',
                          'West Brom', 'Swansea City', 'Burnley', 'Stoke City', 'Huddersfield',
                          'Cardiff City', 'Norwich City', 'Sheffield Utd', 'Leeds United', 'Luton Town'),
                        )
  st.write("You selected:", home_team)
with right:
  away_team = st.selectbox("Choose Away Team", 
                         ('Manchester Utd', 'Ipswich Town', 'Newcastle Utd', "Nott'ham Forest", 
                          'Everton', 'Arsenal', 'West Ham', 'Brentford', 'Chelsea', 'Leicester City',
                          'Brighton', 'Tottenham', 'Fulham', 'Crystal Palace', 'Manchester City',
                          'Southampton', 'Aston Villa', 'Bournemouth', 'Wolves', 'Liverpool', 'Watford',
                          'West Brom', 'Swansea City', 'Burnley', 'Stoke City', 'Huddersfield',
                          'Cardiff City', 'Norwich City', 'Sheffield Utd', 'Leeds United', 'Luton Town'),
                        )
  st.write("You selected:", away_team)

col1, col2, col3 = st.columns(3)
with col2:
  button = st.button('Start Prediction', use_container_width=True, type='primary')

if button == True:
    model = rf_regressor(roll_df_normal)
    predict_data(roll_df_normal, home_team, away_team)
    plot_timeline(roll_df, home_team, away_team)
    
else:
  st.write('Prediction Not Started')

st.caption("Last Update: 20-03-2025")

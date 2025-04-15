import streamlit as st
import numpy as np
from function_epl import *

st.header("Let's See the Score!")

df = rolling_home(df)
df = rolling_home_away(df)
roll_df = sort_data(df)
roll_df = encode_data(roll_df)
roll_df_normal = normalization_data(roll_df)

home_team = st.selectbox("Choose Home Team",
                         ('Manchester Utd', 'Ipswich Town', 'Newcastle Utd', "Nott'ham Forest",
                          'Everton', 'Arsenal', 'West Ham', 'Brentford', 'Chelsea', 'Leicester City',
                          'Brighton', 'Tottenham', 'Fulham', 'Crystal Palace', 'Manchester City',
                          'Southampton', 'Aston Villa', 'Bournemouth', 'Wolves', 'Liverpool', 'Watford',
                          'West Brom', 'Swansea City', 'Burnley', 'Stoke City', 'Huddersfield',
                          'Cardiff City', 'Norwich City', 'Sheffield Utd', 'Leeds United', 'Luton Town'),
                        )
st.write("You selected:", home_team)
away_team = st.selectbox("Choose Away Team", 
                         ('Manchester Utd', 'Ipswich Town', 'Newcastle Utd', "Nott'ham Forest", 
                          'Everton', 'Arsenal', 'West Ham', 'Brentford', 'Chelsea', 'Leicester City',
                          'Brighton', 'Tottenham', 'Fulham', 'Crystal Palace', 'Manchester City',
                          'Southampton', 'Aston Villa', 'Bournemouth', 'Wolves', 'Liverpool', 'Watford',
                          'West Brom', 'Swansea City', 'Burnley', 'Stoke City', 'Huddersfield',
                          'Cardiff City', 'Norwich City', 'Sheffield Utd', 'Leeds United', 'Luton Town'),
                        )
button = st.button('Start Prediction')
st.write("You selected:", away_team)

if button == True:
    st.write('Prediction Starting')
    model = rf_regressor(roll_df_normal)
    predict_data(roll_df_normal, home_team, away_team)
    
else:
  st.write('Prediction Not Started')

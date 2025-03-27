# -*- coding: utf-8 -*-
"""EPL - Streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cEz7NWkbTosCjo69zoSLL5elBKtgH0x1
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from function_epl import *

st.header('Can Your Team Win?')
st.write('English Premier League Version')
st.write('This is for FUN only. I made this because I need a portfolio for my data science job (LOL).')
df = read_data('epl-2017-2025-03-20.csv')
df = rolling_home(df)
df = rolling_home_away(df)
roll_df = sort_data(df)
roll_df = encode_data(roll_df)
roll_df_normal = normalization_data(roll_df)
model = rf_regressor(roll_df_normal)


home_team = st.selectbox("Choose Home Team",
                         ('Manchester Utd', 'Ipswich Town', 'Newcastle Utd', "Nott'ham Forest",
                          'Everton', 'Arsenal', 'West Ham', 'Brentford', 'Chelsea', 'Leicester City',
                          'Brighton', 'Tottenham', 'Fulham', 'Crystal Palace', 'Manchester City',
                          'Southampton', 'Aston Villa', 'Bournemouth', 'Wolves', 'Liverpool', 'Watford',
                          'West Brom', 'Swansea City', 'Burnley', 'Stoke City', 'Huddersfield',
                          'Cardiff City', 'Norwich City', 'Sheffield Utd', 'Leeds United', 'Luton Town'),
                        )
away_team = st.selectbox("Choose Away Team", 
                         ('Manchester Utd', 'Ipswich Town', 'Newcastle Utd', "Nott'ham Forest", 
                          'Everton', 'Arsenal', 'West Ham', 'Brentford', 'Chelsea', 'Leicester City',
                          'Brighton', 'Tottenham', 'Fulham', 'Crystal Palace', 'Manchester City',
                          'Southampton', 'Aston Villa', 'Bournemouth', 'Wolves', 'Liverpool', 'Watford',
                          'West Brom', 'Swansea City', 'Burnley', 'Stoke City', 'Huddersfield',
                          'Cardiff City', 'Norwich City', 'Sheffield Utd', 'Leeds United', 'Luton Town'),
                        )
button = st.button('Start Prediction')

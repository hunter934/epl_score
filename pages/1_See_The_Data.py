import streamlit as st
import numpy as np
from function_epl import *

st.set_page_config(page_title="EPL Data", page_icon="⚽")

st.header('See The Data')
st.dataframe(df)
st.caption('Last update: 20-03-2025')

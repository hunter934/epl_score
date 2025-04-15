import streamlit as st
import numpy as np
from function_epl import *

st.header('EPL Database')
st.dataframe(df)
st.caption('Last update: 20-03-2025')

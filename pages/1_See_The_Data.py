import streamlit as st
import numpy as np
from function_epl import *

st.set_page_config(page_title='EPL Database', page_icon='⚽')

st.markdown('EPL Database')
st.sidebar.header('EPL Database')
st.dataframe(df)
st.caption('Last update: 20-03-2025')

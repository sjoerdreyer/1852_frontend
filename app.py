import streamlit as st

import numpy as np
import pandas as pd

# st.slider("select a value", 1, 10, 5, 1)

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
pass_count = st.slider('Select passanger count', 0, 10, 1, 1)

# and used to select the displayed lines
head_df = df.head(pass_count)

head_df

# url = 'API/predict'
# params_df = {}
# pred = requets.get().json()

# final_pred = pred['fare']
final_pred = 15.5

st.markdown(f'taxifare ride will cost you {final_pred} $')

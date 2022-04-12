import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.header('Streamlit Cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(10000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return st.write(df)

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(10000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return st.write(df)

# Using cache
a0 = time()

st.subheader('Using st.cache')
load_data_a()

a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()

st.subheader('Not using st.cache')
load_data_b()

b1 = time()
st.info(b1-b0)

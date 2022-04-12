import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.header('Streamlit Cache')

@st.cache()
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(10000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(10000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

a0 = time()
load_data_a()
a1 = time()
st.info(a1-a0)


b0 = time()
load_data_b()
b1 = time()
st.info(b1-b0)

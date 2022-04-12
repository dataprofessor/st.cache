import streamlit as st
import pandas as pd
import pandas_profiling

from streamlit_pandas_profiling import st_profile_report

@st.cache(suppress_st_warning=True)
def pp_report(input_data):
  df = pd.read_csv(input_data)
  pr = df.profile_report()
  return st_profile_report(pr)

pp_report('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

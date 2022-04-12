import streamlit as st
import pandas as pd
import pandas_profiling

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

@st.cache(suppress_st_warning=True)
def pp_report(input_data):
  pr = input_data.profile_report()
  return st_profile_report(pr)

pp_report(df)

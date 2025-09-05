import streamlit as st
import pandas as pd
import numpy as np

##Adding a title
st.title("Hello Streamlit")

##Display simple text
st.write("This is a sample text")

##create a simple dataframe

df = pd.DataFrame({
    'first': [1, 2, 3, 4],
    'second': [5, 6, 7, 8]
})

##Display DF
st.write("Here is the dataframe")
st.write(df)

##Display a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["a", "b", "c"]
)
st.line_chart()
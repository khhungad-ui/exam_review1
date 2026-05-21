import pandas as pd
import streamlit as st


data = {
    'Product': ['A', 'B', 'C'],
    'Sales': [1200, 850, 950],
    'Customers': [300, 400, 350]
}
df = pd.DataFrame(data)

st.write("This is dataframe!")
st.dataframe(df)

st.write("This is data_editor!")
st.data_editor(df)

st.write("This is table")
st.table(df)

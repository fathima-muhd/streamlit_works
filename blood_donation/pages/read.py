import streamlit as st
from Blood import BloodAddReadRetrieveUpdateDelete
st.title("READ")
b=BloodAddReadRetrieveUpdateDelete()
records=b.read()
if records:
    st.table(records)
else:
    st.error("Not Found")
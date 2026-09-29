import streamlit as st
from library_stream import BooklistCreateRetrieveUpdateDelete
st.title("READ RECORDS")

b=BooklistCreateRetrieveUpdateDelete()
records=b.list()
if records:
    st.table(records)
else:
    st.error("No Records Found")





    
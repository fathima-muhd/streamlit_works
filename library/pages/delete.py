import streamlit as st
from library_stream import BooklistCreateRetrieveUpdateDelete
st.title("DELETE")
id=st.number_input('enter id',min_value=0)
btn=st.button("Delete")
if btn:
    b=BooklistCreateRetrieveUpdateDelete()
    records=b.delete(id)
    if records:
        st.success("Record deleted successfully")
    else:
        st.error("No Records Found")

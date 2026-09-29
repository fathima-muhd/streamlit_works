import streamlit as st
from library_stream import BooklistCreateRetrieveUpdateDelete
st.title("RETRIEVE")
id=st.number_input("ID",min_value=0)
btn=st.button("Click")
if btn:
    b=BooklistCreateRetrieveUpdateDelete()
    records=b.retrieve(id)

    if records:
        # st.table(records)
        st.write("Title:",records[1])
        st.write("Author:",records[2])
        st.write("Language:",records[3])
        st.write("Price:",records[4])
        st.write("Pages:",records[5])

    else:
        st.error("No Records Found")


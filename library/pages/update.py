import streamlit as st
from library_stream import BooklistCreateRetrieveUpdateDelete
st.title("UPDATE")
st.write(" ")
id=st.number_input("Enter id",min_value=0)
title=st.text_input("Title")
author=st.text_input("Author")
language=st.selectbox("Language",["Malayalam","Hindi","English"])
price=st.number_input("price",min_value=0)
pages=st.number_input("pages",min_value=0)
btn=st.button("update")
if btn:
    b=BooklistCreateRetrieveUpdateDelete()
    records=b.update(id,title,author,price,pages,language)
    if records:    
        st.write("updated Successfully")
    else:
        st.error("No Records Found")
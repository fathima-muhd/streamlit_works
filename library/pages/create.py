import streamlit as st
from library_stream import BooklistCreateRetrieveUpdateDelete
st.title("CREATE")
title=st.text_input("Title")
author=st.text_input("Author")
language=st.selectbox("Language",["Malayalam","English","Hindi"])
price=st.number_input("Price",min_value=0)
pages=st.number_input("Pages",min_value=0)
btn=st.button("Submit")
if btn:
    b=BooklistCreateRetrieveUpdateDelete()
    b.create(title,author,price,pages,language)
    st.success("Created Successfully")
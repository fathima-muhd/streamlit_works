import streamlit as st
from library_stream import BooklistCreateRetrieveUpdateDelete

st.title('Welcome to library')
b=BooklistCreateRetrieveUpdateDelete()

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])

with tab1:
    st.write('ADD')
    title=st.text_input("Title")
    author=st.text_input("Author")
    language=st.selectbox("Language",["Malayalam","English","Hindi"])
    price=st.number_input("Price",min_value=0)
    pages=st.number_input("Pages",min_value=0)
    btn=st.button("Submit")
    if btn:
        b.create(title,author,price,pages,language)
        st.success("Created Successfully")

with tab2:
    st.write('READ')

with tab3:
    st.write('RETRIEVE')

with tab4:
    st.write('UPDATE')

with tab5:
    st.write('DELETE')
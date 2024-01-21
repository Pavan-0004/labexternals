import streamlit as st

st.header("Lab externals")
st.subheader("AT CD Pdf's")
with open("atcd.pdf", "rb") as file:
    btn = st.download_button(
    label="ATCD pdf",
    data=file,
    file_name="atcd.pdf",
    mime="pdf"
    )
st.subheader("DWDM")
with open("dwdm.pdf", "rb") as file:
    btn = st.download_button(
    label="DWDM",
    data=docx,
    file_name="dwdm.pdf",
    mime="pdf"
    )

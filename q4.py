import streamlit as st
from PyPDF2 import PdfReader
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")
if uploaded_pdf:
    reader = PdfReader(uploaded_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    sentences = nltk.sent_tokenize(text)
    
    st.write("Extracted text")
    for i in range(58, 69):
        if i < len(sentences):
            st.write(f"[{i}]: {sentences[i]}")
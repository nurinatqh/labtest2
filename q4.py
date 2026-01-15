import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize
from PyPDF2 import PdfReader

@st.cache_resource
def download_nltk_resources():
    nltk.download("punkt")
    nltk.download("punkt_tab")

download_nltk_resources()

st.set_page_config(page_title="PDF Semantic Chunking", layout="wide")

st.title("Question 4: PDF Text Chunking")
st.write("Extract text from PDF and perform semantic sentence tokenization.")

uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

if uploaded_file is not None:
    
    try:
        reader = PdfReader(uploaded_file)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + " "
        
        if full_text.strip():
            
            st.subheader("Text Sample Index 58-68")
            
            sample = full_text[58:69]
            st.code(sample if sample.strip() else "[Whitespace/Empty at these indices]")

            
            st.subheader("Semantic Sentence Chunks")
            chunks = sent_tokenize(full_text)
            
            st.write(f"**Total Sentences Found:** {len(chunks)}")
            
            
            st.write(chunks)
            
        else:
            st.error("The PDF appears to be empty or contains no extractable text.")
            
    except Exception as e:
        st.error(f"An error occurred while processing the PDF: {e}")
else:
    st.info("Please upload a PDF file to see the results.")
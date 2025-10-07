"""
PDF Document Parsing and Processing Module

This module provides utilities for loading, parsing, and processing PDF documents
using various LangChain loaders with enhanced text cleaning and chunking capabilities.
"""


from langchain_community.document_loaders import (PyPDFLoader,PyMuPDFLoader,UnstructuredPDFLoader)

# PypdfLoader
print("PyPdfloader")

try:
    pdf_loader = PyPDFLoader("data/pdf/th.pdf")
    pdf_docs = pdf_loader.load()
    
    print(f"📄 Loaded {len(pdf_docs)} pages")
    print(f"📄 Page 1 content : {pdf_docs[0].page_content[:100]}...")
    print(f"📄 Metadata : {pdf_docs[0].metadata}")

    print(pdf_docs)
except Exception as e:
    print(f"❌ Error loading PDF: {e}")


# Method 2 : PyMuPDFLoader (Fast and accurate)
print("\n PyMuPDFLoader")

try:
    pymupdf_loader = PyMuPDFLoader("data/pdf/th.pdf")
    pymupdf_docs = pymupdf_loader.load()

    print(f"📄 Loaded {len(pymupdf_docs)} pages")
    print(f"📄 Page 1 content : {pymupdf_docs[0].page_content[:200]}...")
    print(f"📄 Metadata : {pymupdf_docs[0].metadata}")

    print(pymupdf_docs)
except Exception as e:
    print(f"❌ Error loading PDF: {e}")

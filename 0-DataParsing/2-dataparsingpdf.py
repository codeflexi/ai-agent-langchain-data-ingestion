"""
PDF Document Parsing and Processing Module

This module provides utilities for loading, parsing, and processing PDF documents
using various LangChain loaders with enhanced text cleaning and chunking capabilities.
"""

from typing import List, Dict, Any
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class SmartPDFProcessor:
    """
    Advanced PDF processing with error handling and smart chunking.
    
    Features:
    - Intelligent text cleaning
    - Configurable chunking
    - Enhanced metadata preservation
    - Error handling for malformed PDFs
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        """
        Initialize the PDF processor.
        
        Args:
            chunk_size: Maximum size of each text chunk
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def process_pdf(self, pdf_path: str) -> List[Document]:
        """
        Process PDF with smart chunking and metadata enhancement.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            List of processed Document chunks with enhanced metadata
        """
        # Load PDF
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        
        # Process each page
        processed_chunks = []
        
        for page_num, page in enumerate(pages):
            # Clean text
            cleaned_text = self._clean_text(page.page_content)
            
            # Skip nearly empty pages
            if len(cleaned_text.strip()) < 50:
                continue
            
            # Create chunks with enhanced metadata
            chunks = self.text_splitter.create_documents(
                texts=[cleaned_text],
                metadatas=[{
                    **page.metadata,
                    "page": page_num + 1,
                    "total_pages": len(pages),
                    "chunk_method": "smart_pdf_processor",
                    "char_count": len(cleaned_text)
                }]
            )
            
            processed_chunks.extend(chunks)
        
        return processed_chunks
    
    def _clean_text(self, text: str) -> str:
        """
        Clean extracted text from PDF.
        
        Args:
            text: Raw text extracted from PDF
            
        Returns:
            Cleaned text with fixed formatting issues
        """
        # Remove excessive whitespace
        text = " ".join(text.split())
        
        # Fix common PDF ligature issues
        text = text.replace("ï¬", "fi")
        text = text.replace("ï¬‚", "fl")
        
        return text


def compare_pdf_loaders(pdf_path: str) -> Dict[str, Any]:
    """
    Compare different PDF loading methods.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Dictionary containing comparison results
    """
    results = {}
    
    # PyPDFLoader
    print("Testing PyPDFLoader...")
    try:
        pypdf_loader = PyPDFLoader(pdf_path)
        pypdf_docs = pypdf_loader.load()
        results['pypdf'] = {
            'success': True,
            'pages': len(pypdf_docs),
            'first_page_length': len(pypdf_docs[0].page_content) if pypdf_docs else 0,
            'metadata_keys': list(pypdf_docs[0].metadata.keys()) if pypdf_docs else []
        }
        print(f"  ✅ Loaded {len(pypdf_docs)} pages")
    except Exception as e:
        results['pypdf'] = {'success': False, 'error': str(e)}
        print(f"  ❌ Error: {e}")
    
    # PyMuPDFLoader
    print("\nTesting PyMuPDFLoader...")
    try:
        pymupdf_loader = PyMuPDFLoader(pdf_path)
        pymupdf_docs = pymupdf_loader.load()
        results['pymupdf'] = {
            'success': True,
            'pages': len(pymupdf_docs),
            'first_page_length': len(pymupdf_docs[0].page_content) if pymupdf_docs else 0,
            'metadata_keys': list(pymupdf_docs[0].metadata.keys()) if pymupdf_docs else []
        }
        print(f"  ✅ Loaded {len(pymupdf_docs)} pages")
    except Exception as e:
        results['pymupdf'] = {'success': False, 'error': str(e)}
        print(f"  ❌ Error: {e}")
    
    return results


def clean_text(text: str) -> str:
    """
    Standalone function to clean PDF text.
    
    Args:
        text: Raw text from PDF
        
    Returns:
        Cleaned text
    """
    # Remove excessive whitespace
    text = " ".join(text.split())
    
    # Fix ligatures
    text = text.replace("ï¬", "fi")
    text = text.replace("ï¬‚", "fl")
    
    return text


def main():
    """
    Main function demonstrating PDF processing capabilities.
    """
    pdf_path = "data/pdf/th.pdf"
    
    print("=" * 70)
    print("PDF Document Parsing and Processing Demo")
    print("=" * 70)
    
    # Compare loaders
    print("\n1. Comparing PDF Loaders:")
    print("-" * 70)
    comparison = compare_pdf_loaders(pdf_path)
    
    # Process with SmartPDFProcessor
    print("\n2. Processing with SmartPDFProcessor:")
    print("-" * 70)
    try:
        processor = SmartPDFProcessor(chunk_size=1000, chunk_overlap=100)
        smart_chunks = processor.process_pdf(pdf_path)
        
        print(f"✅ Processed into {len(smart_chunks)} smart chunks")
        
        if smart_chunks:
            print("\nSample chunk metadata:")
            for key, value in smart_chunks[0].metadata.items():
                print(f"  {key}: {value}")
            
            print(f"\nFirst chunk preview (200 chars):")
            print(f"  {smart_chunks[0].page_content[:200]}...")
    
    except Exception as e:
        print(f"❌ Processing error: {e}")
    
    # Text cleaning demo
    print("\n3. Text Cleaning Demo:")
    print("-" * 70)
    raw_text = """Company Financial Report


    The ï¬nancial performance for ï¬scal year 2024
    shows signiï¬cant growth in proï¬tability.
    
    
    
    Revenue increased by 25%.
    
The company's efï¬ciency improved due to workï¬‚ow
optimization.


Page 1 of 10
"""
    
    cleaned = clean_text(raw_text)
    print("BEFORE:")
    print(repr(raw_text[:100]))
    print("\nAFTER:")
    print(repr(cleaned[:100]))
    
    print("\n" + "=" * 70)
    print("PDF Loader Comparison Summary:")
    print("=" * 70)
    print("\nPyPDFLoader:")
    print("  ✅ Simple and reliable")
    print("  ✅ Good for most PDFs")
    print("  ✅ Preserves page numbers")
    print("  ⚠️  Basic text extraction")
    print("  Use when: Standard text PDFs")
    
    print("\nPyMuPDFLoader:")
    print("  ✅ Fast processing")
    print("  ✅ Good text extraction")
    print("  ✅ Image extraction support")
    print("  ✅ More detailed metadata")
    print("  Use when: Speed is important")
    
    print("\nSmartPDFProcessor:")
    print("  ✅ Enhanced text cleaning")
    print("  ✅ Smart chunking with overlap")
    print("  ✅ Enhanced metadata")
    print("  ✅ Error handling")
    print("  Use when: Production RAG systems")


if __name__ == "__main__":
    main()
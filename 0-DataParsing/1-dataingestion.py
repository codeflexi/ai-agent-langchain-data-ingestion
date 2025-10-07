"""
Data Ingestion Module for RAG Systems
This module covers parsing and ingesting data for RAG systems, from basic text files 
to complex PDFs and databases using LangChain v0.3

Topics covered:
- Introduction to Data Ingestion
- Text Files (.txt)
- PDF Documents
- Microsoft Word Documents
- CSV and Excel Files
- JSON and Structured Data
- Web Scraping
- Databases (SQL)
- Audio and Video Transcripts
- Advanced Techniques
- Best Practices
"""

import os
from typing import List, Dict, Any
import pandas as pd
from langchain_core.documents import Document
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter
)
from langchain_community.document_loaders import TextLoader, DirectoryLoader

print("Setup Completed!")

# ============================================================================
# SECTION 1: Understanding Document Structure in LangChain
# ============================================================================

def demonstrate_document_structure():
    """Show the structure of a LangChain Document object"""
    print("\n" + "="*70)
    print("SECTION 1: Understanding Document Structure")
    print("="*70)
    
    # Create a simple document
    doc = Document(
        page_content="This is the main text content that will be embedded and searched.",
        metadata={
            "source": "example.txt",
            "page": 1,
            "author": "Nattapong Mahamart",
            "date_created": "2025-10-01",
            "custom_field": "any_value"
        }
    )
    
    print("\nDocument Structure")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
    print(f"Type: {type(doc)}")
    
    # Why metadata matters
    print("\n📋 Metadata is crucial for:")
    print("- Filtering search results")
    print("- Tracking document sources")
    print("- Providing context in responses")
    print("- Debugging and auditing")



# ============================================================================
# SECTION 2: Creating Sample Text Files
# ============================================================================

def create_sample_text_files():
    """Create sample text files for demonstration"""
    print("\n" + "="*70)
    print("SECTION 2: Creating Sample Text Files")
    print("="*70)
    
    # Create directory
    os.makedirs("data/txt_files", exist_ok=True)

    sample_texts = {
        "data/txt_files/python_intro.txt": """Python Programming Introduction

Python is a high-level, interpreted programming language known for its simplicity and readability.
Created by Guido van Rossum and first released in 1991, Python has become one of the most popular
programming languages in the world.

Key Features:
- Easy to learn and use
- Extensive standard library
- Cross-platform compatibility
- Strong community support 123

Python is widely used in web development, data science, artificial intelligence, and automation.""",
        
        "data/txt_files/machine_learning.txt": """Machine Learning Basics

Machine learning is a subset of artificial intelligence that enables systems to learn and improve
from experience without being explicitly programmed. It focuses on developing computer programs
that can access data and use it to learn for themselves.

Types of Machine Learning:
1. Supervised Learning: Learning with labeled data
2. Unsupervised Learning: Finding patterns in unlabeled data
3. Reinforcement Learning: Learning through rewards and penalties 345

Applications include image recognition, speech processing, and recommendation systems"""
    }
    
    # Loops to Write sample text files
    for filepath, content in sample_texts.items():
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(content)
    
    print("✅ Sample text files created!")



# ============================================================================
# SECTION 3: TextLoader - Reading Single Files
# ============================================================================

def load_single_text_file():
    """Demonstrate loading a single text file"""
    print("\n" + "="*70)
    print("SECTION 3: TextLoader - Reading Single File")
    print("="*70)
    
    # Loading a single text file
    loader = TextLoader("data/txt_files/python_intro.txt", encoding="utf-8")
    documents = loader.load()
    
    print(f"\n📄 Loaded {len(documents)} document")
    print(f"Content preview: {documents[0].page_content[:400]}...")
    print(f"Metadata: {documents[0].metadata}")
   
    
    return documents

# ============================================================================
# SECTION 4: DirectoryLoader - Loading Multiple Text Files
# ============================================================================

def load_directory_text_files():
    """Demonstrate loading multiple text files from a directory"""
    print("\n" + "="*70)
    print("SECTION 4: DirectoryLoader - Loading Multiple Files")
    print("="*70)
    
    # Load all text files from directory
    dir_loader = DirectoryLoader(
        "data/txt_files",
        glob="**/*.txt",  # Pattern to match files
        loader_cls=TextLoader,  # Loader class to use
        loader_kwargs={'encoding': 'utf-8'},
        show_progress=True
    )
    
    documents = dir_loader.load()
    
    print(f"\n📁 Loaded {len(documents)} documents")
    for i, doc in enumerate(documents):
        print(f"\nDocument {i+1}:")
        print(f"  Source: {doc.metadata['source']}")
        print(f"  Length: {len(doc.page_content)} characters")
    
    # Analysis
    print("\n📊 DirectoryLoader Characteristics:")
    print("✅ Advantages:")
    print("  - Loads multiple files at once")
    print("  - Supports glob patterns")
    print("  - Progress tracking")
    print("  - Recursive directory scanning")
    
    print("\n❌ Disadvantages:")
    print("  - All files must be same type")
    print("  - Limited error handling per file")
    print("  - Can be memory intensive for large directories")
    
    return documents

# ============================================================================
# SECTION 5: Text Splitting Strategies
# ============================================================================

def demonstrate_character_text_splitter(text):
    """Demonstrate CharacterTextSplitter with different separators"""
    print("\n" + "="*70)
    print("SECTION 5a: Character Text Splitter")
    print("="*70)
    
    # Method 1: Split on spaces
    print("\n1️⃣ CHARACTER TEXT SPLITTER (separator=' ')")
    char_splitter = CharacterTextSplitter(
        separator=" ",
        chunk_size=200,
        chunk_overlap=20,
        length_function=len
    )
    
    char_chunks = char_splitter.split_text(text)
    print(f"Created {len(char_chunks)} chunks")
    print(f"First chunk: {char_chunks[0][:100]}...")
    
    print("\nFirst two chunks:")
    print(char_chunks[0])
    print("-" * 50)
    print(char_chunks[1])
    
  
    
    # Method 2: Split on newlines
    print("\n\n1️⃣ CHARACTER TEXT SPLITTER (separator='\\n')")
    char_splitter_newline = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=20,
        length_function=len
    )
    
    char_chunks_newline = char_splitter_newline.split_text(text)
    print(f"Created {len(char_chunks_newline)} chunks")
    
    print("\nFirst three chunks:")
    for i in range(min(3, len(char_chunks_newline))):
        print(char_chunks_newline[i])
        if i < 2:
            print("-" * 50)
def demonstrate_recursive_text_splitter(text):
    """Demonstrate RecursiveCharacterTextSplitter"""
    print("\n" + "="*70)
    print("SECTION 5b: Recursive Character Text Splitter")
    print("="*70)
    
    print("\n2️⃣ RECURSIVE CHARACTER TEXT SPLITTER")
    recursive_splitter = RecursiveCharacterTextSplitter(
        separators=[" "],
        chunk_size=200,
        chunk_overlap=20,
        length_function=len
    )
    
    recursive_chunks = recursive_splitter.split_text(text)
    print(f"Created {len(recursive_chunks)} chunks")
    print(f"First chunk: {recursive_chunks[0][:100]}...")
    
    print("\nFirst three chunks:")
    for i in range(min(3, len(recursive_chunks))):
        print(recursive_chunks[i])
        if i < 2:
            print("-" * 50)
    
    # Demonstrate overlap with simple example
    print("\n\nSimple overlap example:")
    simple_text = "This is sentence one and it is quite long. This is sentence two and it is also quite long. This is sentence three which is even longer than the others. This is sentence four. This is sentence five. This is sentence six."
    
    splitter = RecursiveCharacterTextSplitter(
        separators=[" ", "\n","","\n\n"],
        chunk_size=80,
        chunk_overlap=20,
        length_function=len
    )
    
    chunks = splitter.split_text(simple_text)
    print(f"\nSimple text example - {len(chunks)} chunks:\n")
    
    for i in range(len(chunks) - 1):
        print(f"Chunk {i+1}: '{chunks[i]}'")
        print(f"Chunk {i+2}: '{chunks[i+1]}'")
        print()

def demonstrate_token_text_splitter(text):
    """Demonstrate TokenTextSplitter"""
    print("\n" + "="*70)
    print("SECTION 5c: Token Text Splitter")
    print("="*70)
    
    print("\n3️⃣ TOKEN TEXT SPLITTER")
    token_splitter = TokenTextSplitter(
        chunk_size=50,
        chunk_overlap=10
    )
    
    token_chunks = token_splitter.split_text(text)
    print(f"Created {len(token_chunks)} chunks")
    print(f"First chunk: {token_chunks[0][:100]}...")

    for i in range(len(token_chunks)):
        print(f"Chunk {i}: '{token_chunks[i]}'")
        print()


def compare_splitting_methods():
    """Print comparison of text splitting methods"""
    print("\n" + "="*70)
    print("TEXT SPLITTING METHODS COMPARISON")
    print("="*70)
    
    print("\n📊 Text Splitting Methods Comparison:")
    
    print("\nCharacterTextSplitter:")
    print("  ✅ Simple and predictable")
    print("  ✅ Good for structured text")
    print("  ❌ May break mid-sentence")
    print("  Use when: Text has clear delimiters")
    
    print("\nRecursiveCharacterTextSplitter:")
    print("  ✅ Respects text structure")
    print("  ✅ Tries multiple separators")
    print("  ✅ Best general-purpose splitter")
    print("  ❌ Slightly more complex")
    print("  Use when: Default choice for most texts")
    
    print("\nTokenTextSplitter:")
    print("  ✅ Respects model token limits")
    print("  ✅ More accurate for embeddings")
    print("  ❌ Slower than character-based")
    print("  Use when: Working with token-limited models")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run all demonstrations"""
    print("\n" + "="*70)
    print("DATA INGESTION FOR RAG SYSTEMS")
    print("="*70)
    
    # Section 1: Document structure
    demonstrate_document_structure()
    
    # Section 2: Create sample files
    create_sample_text_files()

    # Section 3: Load single file
    load_single_text_file()

    # Section 4: Load directory
    documents = load_directory_text_files()
    
    # Section 5: Text splitting strategies
    if documents:
        text = documents[0].page_content
        demonstrate_character_text_splitter(text)
        demonstrate_recursive_text_splitter(text)
        demonstrate_token_text_splitter(text)
        compare_splitting_methods()
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETED!")
    print("="*70)

if __name__ == "__main__":
    main()
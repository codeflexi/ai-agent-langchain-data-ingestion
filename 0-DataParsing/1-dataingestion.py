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
            "author": "Krish Naik",
            "date_created": "2024-01-01",
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

demonstrate_document_structure()

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
    
    for filepath, content in sample_texts.items():
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(content)
    
    print("✅ Sample text files created!")

create_sample_text_files()

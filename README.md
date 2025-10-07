# Data Ingestion for RAG Systems

A comprehensive guide to parsing and ingesting data for Retrieval-Augmented Generation (RAG) systems using LangChain v0.3. This module covers everything from basic text files to complex document processing with practical, runnable examples.

## 🎯 Overview

This project demonstrates data ingestion techniques essential for building RAG applications. Learn how to load, parse, and split documents efficiently for use with vector databases and language models.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Module Structure](#module-structure)
- [Usage Examples](#usage-examples)
- [PDF Processing](#pdf-processing)
- [Text Splitting Strategies](#text-splitting-strategies)
- [Best Practices](#best-practices)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Document Loading**: Load single files or entire directories
- **Multiple File Formats**: Support for .txt, .pdf, Word, CSV, and more
- **PDF Processing**: Advanced PDF parsing with PyMuPDF and PyPDF
- **Smart Text Splitting**: Multiple strategies for chunking text
- **Metadata Management**: Track document sources and properties
- **LangChain Integration**: Built on LangChain v0.3 framework
- **Production-Ready**: Clean, documented, and reusable code

## 🚀 Installation

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer (recommended)

### Why uv?

`uv` is a modern, extremely fast Python package installer and resolver written in Rust. It's 10-100x faster than pip!

```bash
# Install uv (if not already installed)
# On macOS and Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip:
pip install uv
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/codeflexi/ai-agent-langchain-data-ingestion.git
cd ai-agent-langchain-data-ingestion
```

2. Create a virtual environment with uv:
```bash
# uv automatically creates and manages virtual environments
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

3. Install dependencies with uv:
```bash
# Install all dependencies at once (much faster than pip!)
uv pip install -r requirements.txt

# Or install individually:
uv pip install langchain langchain-core langchain-community
uv pip install pymupdf pypdf pandas tiktoken
```

### Requirements

Create a `requirements.txt` file with:
```
langchain>=0.3.0
langchain-core>=0.3.0
langchain-community>=0.3.0
pymupdf>=1.23.0
pypdf>=3.17.0
pandas>=2.0.0
tiktoken>=0.5.0
```

### Alternative: One-Line Installation

```bash
# Using uv (recommended - very fast!)
uv pip install langchain langchain-core langchain-community pymupdf pypdf pandas tiktoken

# Or using traditional pip:
pip install langchain langchain-core langchain-community pymupdf pypdf pandas tiktoken
```

## 🏃 Quick Start

Run the complete demonstration:

```bash
# Text file ingestion demo
python data_ingestion.py

# PDF processing demo
python pdf_parser.py
```

This will:
1. Create sample text files
2. Demonstrate document structure
3. Load single and multiple files
4. Show different text splitting strategies
5. Process PDF documents with multiple loaders
6. Compare splitting methods

## 📁 Module Structure

```
data-ingestion-rag/
├── data_ingestion.py       # Main text ingestion module
├── pdf_parser.py           # PDF processing module
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── data/
│   ├── text_files/        # Sample text files
│   │   ├── python_intro.txt
│   │   └── machine_learning.txt
│   └── pdf/               # Sample PDF files
│       └── th.pdf
└── notebooks/
    ├── 1-dataingestion.ipynb      # Text ingestion notebook
    └── 2-dataparsingpdf.ipynb     # PDF parsing notebook
```

## 💡 Usage Examples

### Loading a Single File

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/text_files/python_intro.txt", encoding="utf-8")
documents = loader.load()

print(f"Loaded {len(documents)} document")
print(f"Content: {documents[0].page_content[:100]}...")
```

### Loading Multiple Files from Directory

```python
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

dir_loader = DirectoryLoader(
    "data/text_files",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={'encoding': 'utf-8'},
    show_progress=True
)

documents = dir_loader.load()
```

### Working with Document Metadata

```python
from langchain_core.documents import Document

doc = Document(
    page_content="Your text content here",
    metadata={
        "source": "example.txt",
        "page": 1,
        "author": "Your Name",
        "date_created": "2024-01-01"
    }
)
```

## 📄 PDF Processing

### PDF Loader Comparison

This project includes two powerful PDF loaders:

#### 1. PyPDFLoader

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/pdf/th.pdf")
pages = loader.load()

print(f"Loaded {len(pages)} pages")
```

**Pros:**
- ✅ Simple and reliable
- ✅ Good for most PDFs
- ✅ Preserves page numbers
- ✅ Pure Python implementation

**Cons:**
- ⚠️ Basic text extraction
- ⚠️ May struggle with complex layouts

**Use when:** Standard text PDFs with simple layouts

#### 2. PyMuPDFLoader (Recommended for Speed)

```python
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("data/pdf/attention.pdf")
pages = loader.load()

print(f"Loaded {len(pages)} pages")
```

**Pros:**
- ✅ Fast processing (10-100x faster)
- ✅ Excellent text extraction
- ✅ Image extraction support
- ✅ More detailed metadata
- ✅ Better handling of complex PDFs

**Cons:**
- ⚠️ Requires native dependencies (PyMuPDF)

**Use when:** Speed is important or dealing with complex PDFs

### Smart PDF Processing

```python
from pdf_parser import SmartPDFProcessor

# Initialize processor with custom settings
processor = SmartPDFProcessor(
    chunk_size=1000,
    chunk_overlap=100
)

# Process PDF with enhanced features
chunks = processor.process_pdf("data/pdf/attention.pdf")

print(f"Processed into {len(chunks)} smart chunks")

# Access enhanced metadata
for chunk in chunks[:3]:
    print(f"Page {chunk.metadata['page']}: {chunk.page_content[:100]}...")
```

**Features:**
- ✅ Automatic text cleaning (fixes ligatures, whitespace)
- ✅ Smart chunking with configurable overlap
- ✅ Enhanced metadata preservation
- ✅ Skips empty or near-empty pages
- ✅ Error handling for malformed PDFs

### PDF Text Cleaning

PDFs often have extraction artifacts. The smart processor handles:

```python
# Before: "The ï¬nancial performance for ï¬scal year 2024"
# After:  "The financial performance for fiscal year 2024"

from pdf_parser import clean_text

raw_text = "The company's efï¬ciency improved due to workï¬‚ow optimization."
cleaned = clean_text(raw_text)
print(cleaned)
# Output: "The company's efficiency improved due to workflow optimization."
```

## 📊 Text Splitting Strategies

### 1. CharacterTextSplitter

Simple splitting based on a single separator (spaces, newlines, etc.)

```python
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=20,
    length_function=len
)

chunks = splitter.split_text(text)
```

**Pros:**
- ✅ Simple and predictable
- ✅ Good for structured text
- ✅ Fast processing

**Cons:**
- ❌ May break mid-sentence
- ❌ Less intelligent splitting

**Use when:** Text has clear, consistent delimiters

### 2. RecursiveCharacterTextSplitter (Recommended)

Tries multiple separators hierarchically to preserve text structure

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=200,
    chunk_overlap=20,
    length_function=len
)

chunks = splitter.split_text(text)
```

**Pros:**
- ✅ Respects text structure
- ✅ Tries multiple separators
- ✅ Best general-purpose splitter
- ✅ Maintains semantic coherence

**Cons:**
- ❌ Slightly more complex
- ❌ Minimal overhead

**Use when:** Default choice for most text processing tasks

### 3. TokenTextSplitter

Splits based on token count (important for LLM token limits)

```python
from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)
```

**Pros:**
- ✅ Respects model token limits
- ✅ More accurate for embeddings
- ✅ Prevents token overflow

**Cons:**
- ❌ Slower than character-based
- ❌ Requires tokenizer

**Use when:** Working with token-limited models or need precise token counts

## 🎓 Best Practices

### 1. Chunk Size Selection

- **Small chunks (100-300 chars)**: Better for precise retrieval, more chunks to manage
- **Medium chunks (300-800 chars)**: Balanced approach, works for most cases
- **Large chunks (800-1500 chars)**: More context, but less precise retrieval

### 2. Chunk Overlap

- Recommended: 10-20% of chunk size
- Prevents losing information at boundaries
- Helps maintain context across chunks

### 3. Metadata Management

Always include:
- `source`: Original file path
- `page`: Page number (if applicable)
- `created_date`: When document was processed
- Custom fields as needed

### 4. Error Handling

```python
try:
    documents = loader.load()
except Exception as e:
    print(f"Error loading documents: {e}")
    # Handle error appropriately
```

### 5. Memory Management

For large directories:
- Process files in batches
- Use generators where possible
- Monitor memory usage

### 6. PDF Processing Tips

- Use PyMuPDFLoader for better performance
- Always clean extracted text (ligatures, whitespace)
- Skip empty pages to reduce noise
- Preserve metadata for traceability
- Use smart chunking for better retrieval

## 🔧 Advanced Usage

### Custom Document Processing

```python
def process_documents(documents):
    """Custom processing pipeline"""
    processed = []
    for doc in documents:
        # Add custom metadata
        doc.metadata['processed_date'] = '2024-01-01'
        doc.metadata['word_count'] = len(doc.page_content.split())
        
        # Clean content
        doc.page_content = doc.page_content.strip()
        
        processed.append(doc)
    
    return processed
```

### Filtering Documents

```python
def filter_by_metadata(documents, key, value):
    """Filter documents by metadata"""
    return [
        doc for doc in documents 
        if doc.metadata.get(key) == value
    ]
```

### Batch Processing PDFs

```python
import os
from pdf_parser import SmartPDFProcessor

processor = SmartPDFProcessor(chunk_size=1000, chunk_overlap=100)
pdf_dir = "data/pdf"

all_chunks = []
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        chunks = processor.process_pdf(pdf_path)
        all_chunks.extend(chunks)

print(f"Processed {len(all_chunks)} total chunks from {len(os.listdir(pdf_dir))} PDFs")
```

## 📚 Topics Covered

- ✅ Introduction to Data Ingestion
- ✅ Text Files (.txt)
- ✅ PDF Documents (PyPDF & PyMuPDF)
- ✅ Smart PDF Processing with Text Cleaning
- ✅ Text Splitting Strategies
- 🚧 Microsoft Word Documents (coming soon)
- 🚧 CSV and Excel Files (coming soon)
- 🚧 JSON and Structured Data (coming soon)
- 🚧 Web Scraping (coming soon)
- 🚧 Databases (SQL) (coming soon)
- 🚧 Audio and Video Transcripts (coming soon)

## ⚡ Performance Tips

### Using uv for Faster Development

```bash
# Install packages lightning fast
uv pip install package-name

# Sync dependencies from requirements.txt
uv pip sync requirements.txt

# Upgrade all packages
uv pip install --upgrade -r requirements.txt

# Create isolated environment
uv venv --python 3.11
```

### PDF Processing Performance

```python
# PyMuPDF is significantly faster
import time

# PyPDF (slower but pure Python)
start = time.time()
loader1 = PyPDFLoader("large.pdf")
docs1 = loader1.load()
print(f"PyPDF: {time.time() - start:.2f}s")

# PyMuPDF (faster, native code)
start = time.time()
loader2 = PyMuPDFLoader("large.pdf")
docs2 = loader2.load()
print(f"PyMuPDF: {time.time() - start:.2f}s")
# Typically 10-100x faster!
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nattapong Mahamart**

- Documentation and examples for educational purposes

## 🙏 Acknowledgments

- LangChain team for the excellent framework
- PyMuPDF developers for the fast PDF library
- Astral team for creating uv
- Community contributors and learners

## 📞 Support

If you have any questions or run into issues:

- Open an issue in the GitHub repository
- Check the [LangChain documentation](https://python.langchain.com/)
- Review the example notebooks
- Check [uv documentation](https://github.com/astral-sh/uv)

## 🔄 Updates

### Version 1.1.0 (Current)
- Added PDF processing with PyMuPDF and PyPDF
- Implemented SmartPDFProcessor with text cleaning
- Migrated to uv package manager
- Enhanced documentation with performance tips

### Version 1.0.0
- Initial release
- Text file loading and processing
- Three text splitting strategies
- Comprehensive documentation

---

**⭐ If you find this useful, please star the repository!**

## 🚀 Quick Commands Reference

```bash
# Setup with uv (fast!)
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r requirements.txt

# Run demos
python data_ingestion.py    # Text file demo
python pdf_parser.py         # PDF processing demo

# Update dependencies
uv pip install --upgrade langchain langchain-community pymupdf

# Check what's installed
uv pip list
```

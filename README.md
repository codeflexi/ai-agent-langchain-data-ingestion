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
- [Text Splitting Strategies](#text-splitting-strategies)
- [Best Practices](#best-practices)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Document Loading**: Load single files or entire directories
- **Multiple File Formats**: Support for .txt files (expandable to PDF, Word, CSV, etc.)
- **Smart Text Splitting**: Multiple strategies for chunking text
- **Metadata Management**: Track document sources and properties
- **LangChain Integration**: Built on LangChain v0.3 framework
- **Production-Ready**: Clean, documented, and reusable code

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip or conda package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/codeflexi/ai-agent-langchain-data-ingestion.git
cd ai-agent-langchain-data-ingestion
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Requirements

Create a `requirements.txt` file with:
```
langchain>=0.3.0
langchain-core>=0.3.0
langchain-community>=0.3.0
pandas>=2.0.0
tiktoken>=0.5.0
```

## 🏃 Quick Start

Run the complete demonstration:

```bash
python data_ingestion.py
```

This will:
1. Create sample text files
2. Demonstrate document structure
3. Load single and multiple files
4. Show different text splitting strategies
5. Compare splitting methods

## 📁 Module Structure

```
data-ingestion-rag/
├── data_ingestion.py       # Main module
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── data/
│   └── text_files/        # Sample data directory
│       ├── python_intro.txt
│       └── machine_learning.txt
└── notebooks/
    └── 1-dataingestion.ipynb  # Original Jupyter notebook
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

## 📚 Topics Covered

- ✅ Introduction to Data Ingestion
- ✅ Text Files (.txt)
- 🚧 PDF Documents (coming soon)
- 🚧 Microsoft Word Documents (coming soon)
- 🚧 CSV and Excel Files (coming soon)
- 🚧 JSON and Structured Data (coming soon)
- 🚧 Web Scraping (coming soon)
- 🚧 Databases (SQL) (coming soon)
- 🚧 Audio and Video Transcripts (coming soon)

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
- Community contributors and learners

## 📞 Support

If you have any questions or run into issues:

- Open an issue in the GitHub repository
- Check the [LangChain documentation](https://python.langchain.com/)
- Review the example notebooks

## 🔄 Updates

### Version 1.0.0 (Current)
- Initial release
- Text file loading and processing
- Three text splitting strategies
- Comprehensive documentation

---

**⭐ If you find this useful, please star the repository!**

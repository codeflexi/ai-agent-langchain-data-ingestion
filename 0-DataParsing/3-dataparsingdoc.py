"""
Word Document Processing
"""

from langchain_community.document_loaders import Docx2txtLoader, UnstructuredWordDocumentLoader

# Method 1: Using Docx2txtLoader
print("1️⃣ Using Docx2txtLoader")
try:
    docx_loader = Docx2txtLoader("data/word_files/proposal.docx")
    docs = docx_loader.load()
    print(f"✅ Loaded {len(docs)} document(s)")
    print(f"Content preview: {docs[0].page_content[:200]}...")
    print(f"Metadata: {docs[0].metadata}")
except Exception as e:
    print(f"Error: {e}")

# Method 2: Using UnstructuredWordDocumentLoader
print("\n2️⃣ Using UnstructuredWordDocumentLoader")
try:
    unstructured_loader = UnstructuredWordDocumentLoader(
        "data/word_files/proposal.docx", 
        mode="elements"
    )
    unstructured_docs = unstructured_loader.load()
    
    print(f"✅ Loaded {len(unstructured_docs)} elements")
    for i, doc in enumerate(unstructured_docs[:10]):
        print(f"\nElement {i+1}:")
        print(f"Type: {doc.metadata.get('category', 'unknown')}")
        print(f"Content: {doc.page_content[:100]}...")
    print("METADATA of 4th element:")
    print(f"Metadata: {unstructured_docs[3].metadata}")  # Display metadata of the 4th element
    print(f"\n Data: {unstructured_docs[8].page_content}")  # Display metadata of the 4th element

except Exception as e:
    print(e)

# Display all unstructured documents (optional)
# Uncomment the line below if you want to see all documents
# print("\nAll unstructured documents:")
# print(unstructured_docs)
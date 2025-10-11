"""
CSV And Excel files - Structured Data Processing
"""

import pandas as pd
import os
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import CSVLoader, UnstructuredExcelLoader


# ============================================================================
# PART 1: CREATE SAMPLE DATA
# ============================================================================

# Create directory for structured files
os.makedirs("data/structured_files", exist_ok=True)

# Create sample data
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'Price': [999.99, 29.99, 79.99, 299.99, 89.99],
    'Stock': [50, 200, 150, 75, 100],
    'Description': [
        'High-performance laptop with 16GB RAM and 512GB SSD',
        'Wireless optical mouse with ergonomic design',
        'Mechanical keyboard with RGB backlighting',
        '27-inch 4K monitor with HDR support',
        '1080p webcam with noise cancellation'
    ]
}

# Save as CSV
df = pd.DataFrame(data)
df.to_csv('data/structured_files/products.csv', index=False)
print("✅ Created products.csv")

# Save as Excel with multiple sheets
with pd.ExcelWriter('data/structured_files/inventory.xlsx') as writer:
    df.to_excel(writer, sheet_name='Products', index=False)
    
    # Add another sheet
    summary_data = {
        'Category': ['Electronics', 'Accessories'],
        'Total_Items': [3, 2],
        'Total_Value': [1389.97, 109.98]
    }
    pd.DataFrame(summary_data).to_excel(writer, sheet_name='Summary', index=False)

print("✅ Created inventory.xlsx with multiple sheets\n")

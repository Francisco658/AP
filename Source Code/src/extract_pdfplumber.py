# Import the pdfplumber library
import pdfplumber
import regex as re

# Function to extract text from each page of a PDF file
def text_from_pdf_with_pdfplumber1(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[5:-1]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'^o.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    return full_text

def text_from_pdf_with_pdfplumber2(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[3:-1]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                page_text = re.sub(r'\b\d+\b', '', page_text)
                page_text = ''.join(char for char in page_text if ord(char) < 128)
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    return full_text

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
  
pdf_path1 = '../PDF Files/Treinar_Musculos.pdf'
pdf_path2 = '../PDF Files/Guia_Treino.pdf'
output_file1 = '../TXT Files/treinar_musculos.txt'
output_file2 = '../TXT Files/guia_treino.txt'
extracted_text1 = text_from_pdf_with_pdfplumber1(pdf_path1)
extracted_text2 = text_from_pdf_with_pdfplumber2(pdf_path2)
write_to_file(extracted_text1, output_file1)
write_to_file(extracted_text2, output_file2)

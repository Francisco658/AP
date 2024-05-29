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
        for page in pdf.pages:
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

def text_from_pdf_with_pdfplumber3(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[9:-14]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                page_text = re.sub(r'\b\d+\b', '', page_text)
                page_text = ''.join(char for char in page_text if ord(char) < 128)
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    return full_text

def text_from_pdf_with_pdfplumber4(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[16:-5]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                page_text = re.sub(r'\b\d+\b', '', page_text)
                page_text = ''.join(char for char in page_text if ord(char) < 128)
                page_text = re.sub(r'^\.', '', page_text, flags=re.MULTILINE)
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    return full_text

def text_from_pdf_with_pdfplumber5(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[47:-8]:
            # Extract text from the current page
            page_text = page.extract_text()

            if page_text:
                lines = page_text.split("\n")
                if len(lines) > 3:  # Adjust the number based on the number of lines in your header
                    # Remove the first three lines assuming they are the header
                    page_text = "\n".join(lines[1:])

            # Append the text of the current page to the full text
            if page_text:
                page_text = re.sub(r'\b\d+\b', '', page_text)
                page_text = ''.join(char for char in page_text if ord(char) < 128)
                page_text = re.sub(r'^\.', '', page_text, flags=re.MULTILINE)
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    return full_text

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
  
pdf_path = '../PDF Files/Muscle_Growth.pdf'
output_file = '../TXT Files/Muscle_Growth.txt'
extracted_text = text_from_pdf_with_pdfplumber1(pdf_path)
write_to_file(extracted_text,output_file)
# Import the required module
import PyPDF2

# Function to extract text from a PDF file
def text_from_pdf(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize a variable to hold all 
        # the extracted text
        full_text = ""
        
        # Iterate over each page in the PDF
        for page in pdf_reader.pages[17]:
            # Extract text from the page and 
            # add it to the full_text variable
            full_text += page.extract_text() + "\n"
        
        return full_text.lower()

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
pdf_path = 'src/Research/Código Penal.pdf'  # Path to your PDF file
output_file = 'extracted_text_py2pdf.txt'  # Path to the output text file
extracted_text = text_from_pdf(pdf_path)
write_to_file(extracted_text, output_file)
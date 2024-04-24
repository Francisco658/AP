# Import necessary libraries
import pdf2image
from PIL import Image
import pytesseract

# Function to convert PDF to images and then extract
# text using Tesseract OCR
def text_from_pdf(pdf_path):
    # Convert PDF to a list of images
    images = pdf2image.convert_from_path(pdf_path)

    # Initialize an empty string to store all 
    # extracted text
    full_text = ""

    # Loop through the images
    for image in images:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        # Append the extracted text to the full 
        # text string
        full_text += text + '\n'

    # Return the full text extracted from the PDF
    return full_text

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
pdf_path = 'src\Leis\Código Penal.pdf'  # Path to your PDF file
output_file = 'extracted_text_tesseract.txt'  # Path to the output text file
extracted_text = text_from_pdf(pdf_path)
write_to_file(extracted_text, output_file)

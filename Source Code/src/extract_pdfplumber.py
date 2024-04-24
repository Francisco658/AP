# Import the pdfplumber library
import pdfplumber
import regex as re


text = """nessa conformidade, o crime sexual praticado contra menor é objecto de uma dupla agravação: por um lado a que resulta de
elevação geral das molduras penais dos crimes de violação e coacção sexual, quer no limite mínimo, quer no máximo; e, por
outro, a agravação estabelecida para os casos em que tais crimes sejam praticados contra menor de 14 anos. donde resulta
que o crime praticado contra menor de 14 anos é sempre punido mais severamente que o crime praticado contra um adulto,
atenta a especial vulnerabilidade da vítima.
uma outra nota que acentua a protecção do menor é a possibilidade de o ministério público, sempre que especiais razões de
interesse público o justifiquem, poder desencadear a acção penal quando a vítima for menor de 12 anos.
ainda numa perspectiva de reforço da tutela dos bens jurídicos pessoais, alteraram-se os pressupostos de concessão da
liberdade condicional. com efeito, nos casos de condenação em pena superior a 5 anos, por crimes contra as pessoas ou
crimes de perigo comum, a liberdade condicional só poderá ser concedida após o cumprimento de dois terços da pena. a
gravidade dos crimes e o alarme social que provocam justificam um maior rigor em sede de execução da pena de prisão.
finalmente, de entre a legislação revogada destaca-se o n.º 1 do artigo 28.º do decreto-lei n.º 85-c/75, de 26 de fevereiro.
no uso da autorização legislativa concedida pelo artigo 1.º da lei n.º 35/94, de 15 de setembro, rectificada pela declaração de
rectificação n.º 17/94, de 13 de dezembro, e nos termos da alínea b) do n.º 1 do artigo 201.º da constituição, o governo
decreta o seguinte:"""



# Function to extract text from each page of a PDF file
def text_from_pdf_with_pdfplumber1(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[16:]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'^alterações.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^alterado.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'pág.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'versão à data.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^rectificado.*$', '', full_text, flags=re.MULTILINE | re.IGNORECASE)
                full_text = re.sub(r'^código penal - cp|legislação consolidada$', '', full_text, flags=re.MULTILINE)

                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    return full_text

def text_from_pdf_with_pdfplumber2(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[16:]:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'^alterações.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^alterado.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'pág.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'versão à data.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^rectificado.*$', '', full_text, flags=re.MULTILINE | re.IGNORECASE)
                full_text = re.sub(r'^código de processo penal - cpp|legislação consolidada$', '', full_text, flags=re.MULTILINE)
                # full_text = re.sub(r'diploma.*?seguinte:', '', full_text, flags=re.MULTILINE)

                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    full_text = re.sub(r'nessa conformidade, o crime sexual praticado contra menor', '', full_text)
    return full_text

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage  
# pdf_path1 = 'src/Research/Codigo_Penal.pdf'  # Path to your PDF file
pdf_path2 = 'src/Research/Codigo_Processo_Penal.pdf'  # Path to your PDF file
# output_file1 = 'pdfplumber_codigo_penal.txt'  # Path to the output text file
output_file2 = 'pdfplumber_codigo_processual_penal.txt'  # Path to the output text file
# extracted_text1 = text_from_pdf_with_pdfplumber1(pdf_path1)  # Correct function name
extracted_text2 = text_from_pdf_with_pdfplumber2(pdf_path2)  # Correct function name
# write_to_file(extracted_text1, output_file1)
write_to_file(extracted_text2, output_file2)
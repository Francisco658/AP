def convert_to_lowercase(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            lowercase_content = content.lower()
        
        with open(file_path, 'w') as file:
            file.write(lowercase_content)
        
        return f"File '{file_path}' successfully converted to lowercase."
    
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

file_path = "../TXT Files/"
result = convert_to_lowercase(file_path)
print(result)
import os

def convert_file_to_lowercase(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
    
    # Convert content to lowercase
    content_lower = content.lower()
    
    # Open the file for writing (overwrite mode)
    with open(file_path, 'w') as file:
        # Write the lowercase content back to the file
        file.write(content_lower)
    

# Example usage: Convert a specific file to lowercase
file_path = "WarmUp.txt"  # Replace this with the path to your file
convert_file_to_lowercase(file_path)

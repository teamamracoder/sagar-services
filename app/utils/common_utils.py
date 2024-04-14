import re

class CommonUtils:
     
     @staticmethod
     def replace_special_characters_with_underscore(text):
        # Define a regular expression pattern to match special characters and spaces
        pattern = r'[^a-zA-Z0-9_.]+'
    
        # Replace matches with underscores
        return re.sub(pattern, '_', text)
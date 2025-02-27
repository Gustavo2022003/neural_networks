import os
import re
from datetime import datetime

def get_file_size(path):
    try:
        file_size = os.path.getsize(path)
        
        size_in_mb = file_size / (1024 * 1024)
        
        return f"{size_in_mb:.2f} MB"
    except FileNotFoundError:
        return "Arquivo não encontrado."

def find_and_replace_pattern_in_md(path, pattern, replacement):
    try:
        if pattern == "X.XX MB":
            regex_pattern = r'(\d+\.\d+ MB)'
        elif pattern == "MM/DD/YYYY":
            regex_pattern = r'(\d{2}/\d{2}/\d{4})'

        with open(path, 'r') as file:
            content = file.read()

        updated_content = re.sub(regex_pattern, replacement, content)

        with open(path, 'w') as file:
            file.write(updated_content)
        
        return f"Padrão '{pattern}' substituído por '{replacement}' no arquivo."

    except FileNotFoundError:
        return "Arquivo não encontrado."
    except Exception as e:
        return f"Erro ao processar o arquivo: {e}"

if __name__ == "__main__":
    current_date = datetime.now()
    path_to_pdf = './docs/Articles/pt-br/Redes Neurais Artificiais - ptBR.pdf'
    path_to_readme = "./README.md"

    pattern_to_find = "X.XX MB"
    replacement_value = str(get_file_size(path_to_pdf))

    pattern_to_find = "MM/DD/YYYY"
    replacement_value = current_date.strftime("%m/%d/%Y")

    print(find_and_replace_pattern_in_md(path_to_readme, pattern_to_find, replacement_value))

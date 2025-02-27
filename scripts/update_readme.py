import os
import re
from datetime import datetime

# Path of the file that will be monitored
file_path = "../docs/Articles/pt-br/Redes Neurais Artificiais - ptBR.pdf"

# README path
readme_path = "../README.md"

def get_file_size(file_path):
    """Returns the file size in MB"""
    if os.path.exists(file_path):
        size = os.path.getsize(file_path) / (1024 * 1024)
        return round(size, 2)
    return 0

def get_current_date():
    """Returna the current date"""
    return datetime.now().strftime("%m/%d/%y")

def update_readme(file_size, last_update):
    """Update the file size and the last update on the README's table"""
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Update the file size on the table
    content = re.sub(
        r"(\|\s*\[Redes Neurais Artificiais - PTBR.*?\|\s*pdf\s*\|\s*)([\d\.]+)(\s*MB\s*\|)",
        r"\1" + str(file_size) + r"\3",
        content
    )

    # Updates the last update date on the table
    content = re.sub(
        r"(\|\s*\[Redes Neurais Artificiais - PTBR.*?\|\s*pdf\s*\|.*?\|\s*Portguese 🇧🇷\s*\|\s*)(\d{2}/\d{2}/\d{2})(\s*\|)",
        r"\1" + last_update + r"\3",
        content
    )

    # Save the new content on the README
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    tamanho = get_file_size(file_path)
    data_atual = get_current_date()
    update_readme(tamanho, data_atual)
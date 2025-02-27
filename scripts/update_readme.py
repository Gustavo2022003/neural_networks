from jinja2 import Template
import os
import datetime

def update_readme(file_size, last_update):
    with open("README_template.md", "r", encoding="utf-8") as file:
        template_content = file.read()

    template = Template(template_content)

    content = template.render(
        file_size=file_size,
        last_update=last_update
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(content)

def get_file_info():
    file_path = "docs/Articles/pt-br/Redes Neurais Artificiais - PTBR.pdf"
    
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    file_size = round(file_size, 2)
    
    last_modified_time = os.path.getmtime(file_path)
    last_update = datetime.datetime.fromtimestamp(last_modified_time).strftime('%m/%d/%y')
    
    return file_size, last_update

file_size, last_update = get_file_info()
update_readme(file_size, last_update)
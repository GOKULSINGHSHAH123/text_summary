import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "text_summary"

list_of_files = [
    "text_summary/github/workflows/.gitkeep",
    f"text_summary/src/{project_name}/__init__.py",
    f"text_summary/src/{project_name}/conponents/__init__.py",
    f"text_summary/src/{project_name}/utils/__init__.py",
    f"text_summary/src/{project_name}/utils/common.py",
    f"text_summary/src/{project_name}/logging/__init__.py",
    f"text_summary/src/{project_name}/config/__init__.py",
    f"text_summary/src/{project_name}/config/configuration.py",
    f"text_summary/src/{project_name}/pipeline/__init__.py",
    f"text_summary/src/{project_name}/entity/__init__.py",
    f"text_summary/src/{project_name}/constants/__init__.py",
    "text_summary/config/config.yaml",
    "text_summary/params.yaml",
    "text_summary/app.py",
    "text_summary/main.py",
    "text_summary/Dockerfile",
    "text_summary/requirements.txt",
    "text_summary/setup.py",
    "text_summary/research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
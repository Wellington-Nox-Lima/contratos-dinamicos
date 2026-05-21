from pathlib import Path
import os
import runpy
import sys


APP_DIR = Path(__file__).resolve().parent / "Projeto contrato dinamico"

os.chdir(APP_DIR)
sys.path.insert(0, str(APP_DIR))
runpy.run_path(str(APP_DIR / "app_streamlit.py"), run_name="__main__")

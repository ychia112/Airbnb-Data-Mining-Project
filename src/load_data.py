import os
import pandas as pd

def load_data(relative_path):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    full_path = os.path.join(project_root, relative_path)
    
    return pd.read_csv(full_path)
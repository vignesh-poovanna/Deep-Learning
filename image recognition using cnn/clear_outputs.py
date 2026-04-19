import nbformat as nbf

notebook_path = 'imagerecognition.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Clear all outputs so the user is forced to rerun and see the fresh state
for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None

# Save the clean notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook outputs cleared. Please Restart & Run All.")

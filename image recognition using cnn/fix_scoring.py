import nbformat as nbf

notebook_path = 'imagerecognition.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# 1. Update imports in the first cell
first_cell = nb.cells[0]
if 'from sklearn.metrics import accuracy_score' not in first_cell.source:
    first_cell.source += "\nfrom sklearn.metrics import accuracy_score"
    print("Added accuracy_score import.")

# 2. Replace scoring() with accuracy_score() in all cells
for cell in nb.cells:
    if cell.cell_type == 'code' and 'scoring(' in cell.source:
        print(f"Found target cell for scoring fix.")
        # Replace scoring(..., metric='accuracy') with accuracy_score(...)
        # We handle the 'metric' argument by removing it as accuracy_score doesn't take it that way
        cell.source = cell.source.replace("scoring(actual_train, predicted_train, metric='accuracy')", "accuracy_score(actual_train, predicted_train)")
        cell.source = cell.source.replace("scoring(actual_test, predicted_test, metric='accuracy')", "accuracy_score(actual_test, predicted_test)")
        print("Updated scoring calls.")

# Save the updated notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook updated successfully.")

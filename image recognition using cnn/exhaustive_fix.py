import nbformat as nbf
import re

notebook_path = 'imagerecognition.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

fixed_count = 0

for cell in nb.cells:
    if cell.cell_type == 'code':
        source = cell.source
        
        # 1. Check if 'accuracy_score' is used but not imported in this cell
        if 'accuracy_score(' in source and 'from sklearn.metrics import accuracy_score' not in source:
             cell.source = "from sklearn.metrics import accuracy_score\n" + source
             fixed_count += 1
             print(f"Added local import to a cell using accuracy_score.")
        
        # 2. Check if 'scoring(' is still used anywhere (just in case)
        if 'scoring(' in source:
            cell.source = cell.source.replace("scoring(actual_train, predicted_train, metric='accuracy')", "accuracy_score(actual_train, predicted_train)")
            cell.source = cell.source.replace("scoring(actual_test, predicted_test, metric='accuracy')", "accuracy_score(actual_test, predicted_test)")
            # And add the import if it's now using accuracy_score
            if 'accuracy_score(' in cell.source and 'from sklearn.metrics import accuracy_score' not in cell.source:
                cell.source = "from sklearn.metrics import accuracy_score\n" + cell.source
            fixed_count += 1
            print(f"Fixed a stray 'scoring' call and added import.")

# Save the updated notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

if fixed_count > 0:
    print(f"Notebook updated. Total fixes: {fixed_count}")
else:
    print("No further issues found in the code structure.")

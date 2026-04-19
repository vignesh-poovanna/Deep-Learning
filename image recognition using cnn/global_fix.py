import nbformat as nbf
import re

notebook_path = 'imagerecognition.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Global replacements for common Keras errors
for cell in nb.cells:
    if cell.cell_type == 'code':
        source = cell.source
        
        # 1. Fix .hdf5 extensions in ModelCheckpoint or file assignments
        source = re.sub(r"(['\"])[\w\.]+\.hdf5(['\"])", r"\1CIFAR10_checkpoint.keras\2", source)
        
        # 2. Fix val_acc -> val_accuracy
        source = source.replace("monitor='val_acc'", "monitor='val_accuracy'")
        
        # 3. Fix predict_classes -> np.argmax(model.predict(...), axis=1)
        # Regex to catch model.predict_classes(X) and similar
        source = re.sub(r"(\w+)\.predict_classes\(([^)]+)\)", r"np.argmax(\1.predict(\2), axis=1)", source)
        
        if cell.source != source:
            print(f"Updated a cell starting with: {cell.source[:50]}...")
            cell.source = source

# Save the updated notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook globally updated successfully.")

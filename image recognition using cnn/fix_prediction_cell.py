import nbformat as nbf

notebook_path = 'imagerecognition.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Target the cell with predict_classes
for cell in nb.cells:
    if cell.cell_type == 'code' and 'model.predict_classes' in cell.source:
        print(f"Found target cell: {cell.source}")
        # Apply the fix
        cell.source = """# Making predictions
pred_probs = model.predict(X_test[:10])
pred_indices = np.argmax(pred_probs, axis=1)
pred = encode_x.inverse_transform(pred_indices)

# Converting one-hot test labels back to class indices for comparison
act_indices = np.argmax(y_test[:10], axis=1)
act = encode_x.inverse_transform(act_indices)

# Creating results table
res = pd.DataFrame([pred, act]).T
res.columns = ['predicted', 'actual']
res"""
        print("Updated cell content.")

# Save the updated notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook updated successfully.")

import nbformat as nbf

notebook_path = 'imagerecognition.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Target the cell with ModuleNotFoundError
for cell in nb.cells:
    if cell.cell_type == 'code' and 'from vis.visualization' in cell.source:
        print(f"Found target cell: {cell.source}")
        # Apply the fix
        cell.source = """# Indexes of categories for our model
classes = encode_x.inverse_transform(np.arange(10))
print(f"Classes: {classes}")

# Fetching and displaying the ship image using PIL (Image.open)
img_path = 'cifar10/' + str(test_idx[6]) + '.png'
ship_img = Image.open(img_path)

plt.imshow(ship_img)
plt.title('Ship image')
plt.show()"""
        print("Updated cell content.")

# Save the updated notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook updated successfully.")

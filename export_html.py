import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
import traceback
import sys

notebook_filename = 'A4_2023202.ipynb'

try:
    with open(notebook_filename, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Provide the live GitHub Pages link based on the repository provided
    link_text = "**GitHub Pages Visualization Link:** [https://fatimaliaquat-29.github.io/Data_Visualization_Assignment4/](https://fatimaliaquat-29.github.io/Data_Visualization_Assignment4/)"
    
    # Inject it at the top
    found = False
    for cell in nb.cells:
        if 'GitHub Pages' in cell.source or 'Replace this with' in cell.source:
            cell.source = link_text
            found = True
            break
            
    if not found:
        new_cell = nbformat.v4.new_markdown_cell(link_text)
        nb.cells.insert(0, new_cell)

    # Execute the notebook to ensure all outputs/graphs are generated
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    print("Executing notebook to generate graphs...")
    ep.preprocess(nb, {'metadata': {'path': './'}})

    # Export to HTML
    html_exporter = HTMLExporter()
    html_exporter.template_name = 'classic' # Standard full HTML export
    (body, resources) = html_exporter.from_notebook_node(nb)

    # Save the HTML file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(body)
    print("Successfully generated 'index.html' for GitHub Pages!")

except Exception as e:
    print("Encountered an error while trying to generate the HTML export:")
    traceback.print_exc()
    sys.exit(1)

# Save the updated notebook with the outputs and new cell
with open(notebook_filename, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print(f"Notebook '{notebook_filename}' updated with outputs and GitHub Pages link.")

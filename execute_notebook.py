import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import traceback
import sys

notebook_filename = 'A4_2023202.ipynb'

try:
    with open(notebook_filename, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    print("Executing notebook to generate PNG graphs...")
    ep.preprocess(nb, {'metadata': {'path': './'}})

    # Save the updated notebook with the outputs
    with open(notebook_filename, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"Notebook '{notebook_filename}' executed successfully.")

except Exception as e:
    print("Encountered an error while executing notebook:")
    traceback.print_exc()
    sys.exit(1)

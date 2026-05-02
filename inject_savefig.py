import nbformat as nbf
import os

notebook_filename = 'A4_2023202.ipynb'

if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

with open(notebook_filename, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'code':
        source = cell.source
        if 'plt.show()' in source:
            if 'Kamada-Kawai' in source and 'visualizations/flare_kamada_kawai.png' not in source:
                source = source.replace('plt.show()', "plt.savefig('visualizations/flare_kamada_kawai.png', dpi=300, bbox_inches='tight')\nplt.show()")
            elif 'Flare Dataset - Spring' in source and 'visualizations/flare_spring.png' not in source:
                source = source.replace('plt.show()', "plt.savefig('visualizations/flare_spring.png', dpi=300, bbox_inches='tight')\nplt.show()")
            elif 'Karate Club - Circular' in source and 'visualizations/karate_circular.png' not in source:
                source = source.replace('plt.show()', "plt.savefig('visualizations/karate_circular.png', dpi=300, bbox_inches='tight')\nplt.show()")
            elif 'Karate Club - Spring' in source and 'visualizations/karate_spring.png' not in source:
                source = source.replace('plt.show()', "plt.savefig('visualizations/karate_spring.png', dpi=300, bbox_inches='tight')\nplt.show()")
            cell.source = source

with open(notebook_filename, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Injected plt.savefig into '{notebook_filename}'.")

import json
import os

filepath = 'A4_2023xxx.ipynb'

with open(filepath, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

for cell in notebook.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = "".join(cell.get('source', []))
        
        if "pos_flare_kk = nx.kamada_kawai_layout(flare_tree)" in source:
            cell['source'] = [
                "plt.figure(figsize=(16, 16))\n",
                "plt.title(\"Flare Dataset - Kamada-Kawai Layout\", fontsize=18)\n",
                "\n",
                "pos_flare_kk = nx.kamada_kawai_layout(flare_tree)\n",
                "nx.draw(flare_tree, pos_flare_kk, \n",
                "        node_size=10, \n",
                "        node_color=\"#1f78b4\", \n",
                "        edge_color=\"lightgray\", \n",
                "        width=0.3, \n",
                "        arrows=False, \n",
                "        with_labels=False, \n",
                "        alpha=0.6)\n",
                "\n",
                "plt.show()"
            ]
        elif "pos_flare_spring = nx.spring_layout(flare_tree, k=0.05, iterations=50)" in source:
            cell['source'] = [
                "plt.figure(figsize=(16, 16))\n",
                "plt.title(\"Flare Dataset - Spring Layout\", fontsize=18)\n",
                "\n",
                "pos_flare_spring = nx.spring_layout(flare_tree, k=0.15, iterations=50)\n",
                "nx.draw(flare_tree, pos_flare_spring, \n",
                "        node_size=10, \n",
                "        node_color=\"#33a02c\", \n",
                "        edge_color=\"lightgray\", \n",
                "        width=0.3, \n",
                "        arrows=False, \n",
                "        with_labels=False, \n",
                "        alpha=0.6)\n",
                "\n",
                "plt.show()"
            ]
        elif "pos_karate_circ = nx.circular_layout(karate_graph)" in source:
            cell['source'] = [
                "plt.figure(figsize=(12, 12))\n",
                "plt.title(\"Karate Club - Circular Layout\", fontsize=18)\n",
                "\n",
                "pos_karate_circ = nx.circular_layout(karate_graph)\n",
                "nx.draw(karate_graph, pos_karate_circ, \n",
                "        labels=node_labels,\n",
                "        node_color=club_colors, \n",
                "        node_size=400, \n",
                "        font_size=9, \n",
                "        font_weight='bold', \n",
                "        font_color='white',\n",
                "        edge_color=\"darkgray\",\n",
                "        width=0.8)\n",
                "\n",
                "plt.show()"
            ]
        elif "pos_karate_spring = nx.spring_layout(karate_graph, seed=42)" in source:
            cell['source'] = [
                "plt.figure(figsize=(12, 12))\n",
                "plt.title(\"Karate Club - Spring Layout\", fontsize=18)\n",
                "\n",
                "pos_karate_spring = nx.spring_layout(karate_graph, k=0.3, seed=42) # Set seed for reproducible layout\n",
                "nx.draw(karate_graph, pos_karate_spring, \n",
                "        labels=node_labels,\n",
                "        node_color=club_colors, \n",
                "        node_size=400, \n",
                "        font_size=9, \n",
                "        font_weight='bold',\n",
                "        font_color='white',\n",
                "        edge_color=\"darkgray\",\n",
                "        width=0.8)\n",
                "\n",
                "plt.show()"
            ]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print("Notebook updated successfully.")

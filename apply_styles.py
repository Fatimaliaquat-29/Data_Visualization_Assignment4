import nbformat as nbf

# Read the notebook
with open('A4_2023xxx.ipynb', 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

graph_creation_code = """# Load routes data
routes_df = pd.read_csv('archive (5)/routes.csv')

# Clean column names
routes_df.columns = [col.strip() for col in routes_df.columns]

# Create NetworkX Graph (using a slightly larger sample for a better network)
sampled_routes = routes_df.head(300)
G_routes = nx.Graph()
for _, row in sampled_routes.iterrows():
    G_routes.add_edge(row['source airport'], row['destination apirport'])

# Extract the largest connected component so the graph isn't fragmented
largest_cc = max(nx.connected_components(G_routes), key=len)
G_routes = G_routes.subgraph(largest_cc)

# Calculate the "degree" (number of connections) for each airport
degrees = dict(G_routes.degree())

# Create lists for node sizes and colors based on their degree
node_sizes = [v * 60 for v in degrees.values()] # Scale up the size
node_colors = [v for v in degrees.values()]"""

spring_layout_code = """plt.figure(figsize=(16, 12))
# k=0.9 spreads the nodes out much further
pos_spring = nx.spring_layout(G_routes, k=0.9, seed=42)

# 1. Draw edges FIRST with low opacity (alpha=0.3) so they sit behind nodes
nx.draw_networkx_edges(G_routes, pos_spring, alpha=0.3, edge_color='gray', width=1.5)

# 2. Draw nodes with dynamic sizes, a colormap (viridis), and black outlines
nodes = nx.draw_networkx_nodes(G_routes, pos_spring, node_size=node_sizes, 
                               node_color=node_colors, cmap=plt.cm.viridis, 
                               edgecolors='black', linewidths=1.5)

# 3. Draw labels ONLY for prominent hubs (e.g., degree > 4) to avoid text clutter
labels = {k: k for k, v in degrees.items() if v > 4}
nx.draw_networkx_labels(G_routes, pos_spring, labels=labels, font_size=11, font_weight='bold')

plt.title("Flight Routes Network - Enhanced Spring Layout", fontsize=18)
plt.axis('off') # Hides the box outline
plt.tight_layout()
plt.savefig('flight_routes_spring.png', dpi=300, bbox_inches='tight')
plt.show()"""

circular_layout_code = """plt.figure(figsize=(14, 14))
pos_circ = nx.circular_layout(G_routes)

# Edges: thin and slightly transparent
nx.draw_networkx_edges(G_routes, pos_circ, alpha=0.2, edge_color='teal', width=1.0)

# Nodes: solid uniform color, but maintaining dynamic sizes
nx.draw_networkx_nodes(G_routes, pos_circ, node_size=[s*0.6 for s in node_sizes], 
                       node_color='skyblue', edgecolors='white', linewidths=1)

# Labels for major hubs
nx.draw_networkx_labels(G_routes, pos_circ, labels=labels, font_size=12, font_weight='bold')

plt.title("Flight Routes Network - Enhanced Circular Layout", fontsize=18)
plt.axis('off')
plt.tight_layout()
plt.savefig('flight_routes_circular.png', dpi=300, bbox_inches='tight')
plt.show()"""

# Replace the cells
for cell in nb.cells:
    if cell.cell_type == 'code':
        if 'sampled_routes =' in cell.source and 'routes_df' in cell.source:
            cell.source = graph_creation_code
        elif 'pos_spring =' in cell.source:
            cell.source = spring_layout_code
        elif 'pos_circ =' in cell.source:
            cell.source = circular_layout_code

with open('A4_2023xxx.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook updated successfully with prettier styles!")

import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title} | A4 Data Visualization</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:#0B0F1A;color:#E5E7EB;font-family:system-ui,sans-serif;display:flex;flex-direction:column;min-height:100vh}}
  header{{background:#111827;border-bottom:1px solid #1E3A8A;padding:18px 32px}}
  header a{{color:#22D3EE;text-decoration:none;font-size:13px;opacity:.8}}
  header a:hover{{opacity:1}}
  h1{{font-size:20px;font-weight:700;color:#E5E7EB;margin-top:4px}}
  .subtitle{{font-size:13px;color:#9CA3AF;margin-top:2px}}
  main{{flex:1;padding:24px 32px;display:flex;flex-direction:column;align-items:center;gap:24px}}
  .chart-wrap{{background:#111827;border:1px solid #1E3A8A22;border-radius:12px;padding:20px;width:100%;max-width:1400px;text-align:center}}
  .chart-wrap img{{width:100%;border-radius:8px;max-width:1360px}}
  .meta{{display:flex;gap:32px;flex-wrap:wrap;justify-content:center}}
  .meta-card{{background:#111827;border:1px solid #0EA5A422;border-radius:10px;padding:16px 24px;text-align:center;min-width:160px}}
  .meta-card .val{{font-size:28px;font-weight:800;color:#22D3EE}}
  .meta-card .key{{font-size:12px;color:#9CA3AF;margin-top:4px}}
  .insight{{background:#111827;border-left:3px solid #0EA5A4;border-radius:6px;padding:16px 20px;max-width:1000px;font-size:14px;color:#9CA3AF;line-height:1.7}}
  .insight strong{{color:#E5E7EB}}
  footer{{text-align:center;padding:16px;font-size:12px;color:#9CA3AF;border-top:1px solid #1E3A8A22}}
</style>
</head>
<body>
<header>
  <a href="../index.html">&#8592; Back to Dashboard</a>
  <h1>{h1}</h1>
  <p class="subtitle">{subtitle}</p>
</header>
<main>
  <div class="meta">
    {meta_cards}
  </div>
  <div class="chart-wrap">
    <img src="{img_src}" alt="{title}"/>
  </div>
  <div class="insight">
    <strong>Insight:</strong> {insight}
  </div>
</main>
<footer>A4 Data Visualization &nbsp;|&nbsp; Theme: Hierarchical Data & Social Network Connectivity</footer>
</body>
</html>"""

pages = [
    {
        'filename': 'flare_kamada_kawai.html',
        'title': 'Kamada-Kawai Layout — Flare Dataset',
        'h1': 'Flare Dataset — Kamada-Kawai Layout',
        'subtitle': 'Tree Visualization 1 | Force-directed Algorithm',
        'img_src': 'flare_kamada_kawai.png',
        'meta_cards': '<div class="meta-card"><div class="val">252</div><div class="key">Nodes</div></div><div class="meta-card"><div class="val">251</div><div class="key">Edges</div></div><div class="meta-card"><div class="val">Tree</div><div class="key">Structure</div></div>',
        'insight': 'The Kamada-Kawai algorithm models the tree hierarchy as a system of springs. It attempts to position nodes so that the geometric distance between them matches their graph-theoretic path distance. This naturally separates the distinct branches of the Flare package hierarchy, ensuring that related classes group tightly while independent sub-packages repel each other.'
    },
    {
        'filename': 'flare_spring.html',
        'title': 'Spring Layout — Flare Dataset',
        'h1': 'Flare Dataset — Spring Layout',
        'subtitle': 'Tree Visualization 2 | Force-directed Layout (Fruchterman-Reingold)',
        'img_src': 'flare_spring.png',
        'meta_cards': '<div class="meta-card"><div class="val">252</div><div class="key">Nodes</div></div><div class="meta-card"><div class="val">251</div><div class="key">Edges</div></div><div class="meta-card"><div class="val">Tree</div><div class="key">Structure</div></div>',
        'insight': 'A classic Spring layout operates on attractive and repulsive forces. The root node tends to center itself, while leaf nodes are pushed to the outer boundaries. Compared to Kamada-Kawai, the Spring layout provides a slightly more organic, tangled visual representation of the software architecture, highlighting the density of classes within specific Flare packages.'
    },
    {
        'filename': 'karate_circular.html',
        'title': 'Circular Layout — Karate Club',
        'h1': "Zachary's Karate Club — Circular Layout",
        'subtitle': 'Graph Visualization 1 | Classic Social Network',
        'img_src': 'karate_circular.png',
        'meta_cards': '<div class="meta-card"><div class="val">34</div><div class="key">Members</div></div><div class="meta-card"><div class="val">78</div><div class="key">Friendships</div></div><div class="meta-card"><div class="val">Undirected</div><div class="key">Graph Type</div></div>',
        'insight': 'The circular layout evenly distributes all 34 members of the karate club along a single large ring. The nodes are colored based on their ultimate club allegiance after the split (blue for Mr. Hi, red for the Officer). This layout avoids node overlap entirely and makes it easy to trace individual edge connections, showing that inter-faction friendships (edges crossing the center) were surprisingly common.'
    },
    {
        'filename': 'karate_spring.html',
        'title': 'Spring Layout — Karate Club',
        'h1': "Zachary's Karate Club — Spring Layout",
        'subtitle': 'Graph Visualization 2 | Force-directed Layout',
        'img_src': 'karate_spring.png',
        'meta_cards': '<div class="meta-card"><div class="val">34</div><div class="key">Members</div></div><div class="meta-card"><div class="val">78</div><div class="key">Friendships</div></div><div class="meta-card"><div class="val">Undirected</div><div class="key">Graph Type</div></div>',
        'insight': 'The force-directed spring layout allows the graph\'s natural community structure to emerge. Highly connected individuals pull together, naturally revealing the two distinct factions (the blue and red groups). You can clearly identify the "hubs" (the instructor and the administrator) acting as gravitational centers for their respective followers, while the sparsely connected nodes float on the periphery.'
    }
]

for p in pages:
    html = template.format(**p)
    filepath = os.path.join('visualizations', p['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filepath}")

# Synthetic graph experiments for k-core and k-truss with multiple datasets and colored visualizations

import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# -------------------------------
# Generate synthetic datasets
# -------------------------------
datasets = {
    "Erdos-Renyi (ER)": nx.erdos_renyi_graph(600, 0.015, seed=1),
    "Barabasi-Albert (BA)": nx.barabasi_albert_graph(600, 4, seed=2),
    "Watts-Strogatz (WS)": nx.watts_strogatz_graph(600, 8, 0.25, seed=3),
    "Random Geometric (RG)": nx.random_geometric_graph(600, 0.11, seed=4),
    "Power-law Cluster (PLC)": nx.powerlaw_cluster_graph(600, 3, 0.3, seed=5)
}

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"]

# -------------------------------
# k-core distribution plot
# -------------------------------
plt.figure()
for (name, G), c in zip(datasets.items(), colors):
    core_numbers = nx.core_number(G)
    dist = Counter(core_numbers.values())
    plt.plot(
        sorted(dist.keys()),
        [dist[k] for k in sorted(dist.keys())],
        marker='o',
        label=name,
        color=c
    )

plt.xlabel("Core number k")
plt.ylabel("Number of vertices")
plt.title("k-core Distributions on Synthetic Graphs")
plt.legend()
plt.show()

# -------------------------------
# k-truss hierarchy plot
# -------------------------------
plt.figure()
for (name, G), c in zip(datasets.items(), colors):
    truss_edges = {}
    k = 2
    while True:
        H = nx.k_truss(G, k)
        if H.number_of_edges() == 0:
            break
        truss_edges[k] = H.number_of_edges()
        k += 1

    plt.plot(
        list(truss_edges.keys()),
        list(truss_edges.values()),
        marker='s',
        linestyle='--',
        label=name,
        color=c
    )

plt.xlabel("Truss number k")
plt.ylabel("Number of edges")
plt.title("k-truss Hierarchies on Synthetic Graphs")
plt.legend()
plt.show()

# -------------------------------
# Summary statistics
# -------------------------------
summary = {}
for name, G in datasets.items():
    summary[name] = {
        "Nodes": G.number_of_nodes(),
        "Edges": G.number_of_edges(),
        "Max k-core": max(nx.core_number(G).values()),
        "Max k-truss": max(k for k in range(2, 20) if nx.k_truss(G, k).number_of_edges() > 0)
    }

summary

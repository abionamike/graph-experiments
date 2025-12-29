# Multi-dataset synthetic experiments with colored visualizations
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# Generate multiple synthetic graphs
datasets = {
    "Erdos-Renyi": nx.erdos_renyi_graph(500, 0.02),
    "Barabasi-Albert": nx.barabasi_albert_graph(500, 4),
    "Watts-Strogatz": nx.watts_strogatz_graph(500, 6, 0.3),
    "Random-Geometric": nx.random_geometric_graph(500, 0.12)
}

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

# ---- k-core comparison ----
plt.figure()
for (name, G), c in zip(datasets.items(), colors):
    core_numbers = nx.core_number(G)
    dist = Counter(core_numbers.values())
    plt.plot(list(dist.keys()), list(dist.values()), marker='o', label=name, color=c)

plt.xlabel("Core number k")
plt.ylabel("Number of vertices")
plt.title("k-core Distribution Across Synthetic Graphs")
plt.legend()
plt.show()

# ---- k-truss comparison ----
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
    plt.plot(list(truss_edges.keys()), list(truss_edges.values()), 
             marker='s', linestyle='--', label=name, color=c)

plt.xlabel("Truss number k")
plt.ylabel("Number of edges")
plt.title("k-truss Hierarchy Across Synthetic Graphs")
plt.legend()
plt.show()

# Summary statistics
summary = {}
for name, G in datasets.items():
    summary[name] = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "max_core": max(nx.core_number(G).values()),
        "max_truss": max([k for k in range(2,10) if nx.k_truss(G, k).number_of_edges()>0])
    }

summary

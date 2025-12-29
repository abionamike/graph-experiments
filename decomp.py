import networkx as nx
import matplotlib.pyplot as plt

def get_max_truss_values(G):
    # Initialize all edges with a base truss value of 2 (connected)
    edge_truss = {tuple(sorted(e)): 2 for e in G.edges()}
    
    k = 3
    while True:
        # Get the k-truss subgraph
        truss_subgraph = nx.k_truss(G, k)
        
        if len(truss_subgraph.edges()) == 0:
            break
            
        # Update edges that are part of this k-truss
        for e in truss_subgraph.edges():
            edge_truss[tuple(sorted(e))] = k
        k += 1
        
    return edge_truss, k - 1

# 1. Create/Load a graph (Karate Club is a great test case)
G = nx.karate_club_graph()

# 2. Compute truss values
truss_map, max_k = get_max_truss_values(G)
edges = G.edges()
colors = [truss_map[tuple(sorted(e))] for e in edges]

# 3. Visualization
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgrey')
nx.draw_networkx_labels(G, pos)

# Draw edges with color mapping based on truss value
edge_collection = nx.draw_networkx_edges(
    G, pos, 
    edgelist=edges, 
    edge_color=colors, 
    edge_cmap=plt.cm.coolwarm, 
    width=2
)

plt.colorbar(edge_collection, label='Max k-truss value')
plt.title(f"k-Truss Decomposition (Max k detected: {max_k})")
plt.axis('off')
plt.show()
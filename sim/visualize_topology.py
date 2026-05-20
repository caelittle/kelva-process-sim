"""
Static network topology diagram using NetworkX + Matplotlib.
Shows nodes and connections — use this to verify your flowsheet is wired correctly.
"""

import matplotlib.pyplot as plt
import networkx as nx


def draw_topology(graph_manager, title="Flowsheet Topology"):
    G = nx.DiGraph()

    for node in graph_manager.nodes.values():
        G.add_node(node.name)

    edge_labels = {}
    for (src_name, src_port, dst_name, dst_port) in graph_manager.connections:
        G.add_edge(src_name, dst_name)
        edge_labels[(src_name, dst_name)] = f"{src_port}→{dst_port}"

    plt.figure(figsize=(12, 6))
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="steelblue", alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=10, font_weight="bold")
    nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20,
                           edge_color="gray", width=2,
                           connectionstyle="arc3,rad=0.1")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_size=8, font_color="darkred")

    plt.title(title, fontsize=14)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("topology.png", dpi=150)
    plt.show()
    print("Topology saved to topology.png")

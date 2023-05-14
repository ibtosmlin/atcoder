import matplotlib.pyplot as plt
import networkx as nx
# Graphオブジェクトの作成
G = nx.Graph()
G = nx.DiGraph()
n, m = map(int, input().split())

nodes = [f'{i+1} / {i}' for i in range(n)]
edges = []
# nodeデータの追加
G.add_nodes_from(nodes)
for _ in range(m):
    xyw = tuple(map(int, input().split()))
    if len(xyw) == 3:
        x, y, w = xyw
        x -= 1; y -= 1
        edges.append((nodes[x], nodes[y], w))
        # edgeデータの追加
        G.add_weighted_edges_from(edges)
    else:
        x, y = xyw
        x -= 1; y -= 1
        edges.append((nodes[x], nodes[y], 1))
        # edgeデータの追加
        G.add_weighted_edges_from(edges)

edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
pos = nx.spring_layout(G)
# ネットワークの可視化
nx.draw(G, pos, with_labels = True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.savefig('graph')
print(G.edges(data=True))
import matplotlib.pyplot as plt
import networkx as nx
# Graphオブジェクトの作成
G = nx.Graph()
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
        edges.append((nodes[x], nodes[y]))
        # edgeデータの追加
        G.add_edges_from(edges)

# ネットワークの可視化
nx.draw(G, with_labels = True)
plt.savefig('graph')

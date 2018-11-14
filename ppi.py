import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import operator

normal = pd.read_excel("bone_normal.xlsx")

normal = normal.loc[normal['R']==1]

normal = normal[['P1','P2']]
normal.to_csv("temp.csv", sep='\t')
df_normal = list(zip(normal.P1, normal.P2))
#normal = pd.DataFrame({'from': normal[['P1']], 'to': normal[['P2']]})

G_normal = nx.Graph()
G_normal.add_edges_from(df_normal)
#print(G.neighbors('4EBP1'))
#print(len(df_normal))
#print(df)
#print(G.edges())
#print(G.nodes())
print("Number of Nodes: ",G_normal.number_of_nodes())
print("Number of Edges: ",G_normal.number_of_edges())
pos = nx.spring_layout(G_normal, k=1, iterations=50)
nx.draw(G_normal, node_size=10, font_size=8, with_labels=True)
plt.savefig("abc.png")

print("Average Clustering Coefficient: ",nx.average_clustering(G_normal))

print("Number of Cnnected Components: ",nx.number_connected_components(G_normal))

print("Diameter of the graph:  ",nx.diameter(G_normal))

print("Betweenness Centrality: ",nx.betweenness_centrality(G_normal))

degrees = [[node,val] for (node, val) in G_normal.degree()]
degrees.sort(key=lambda x: x[1],reverse=True)

print("Degree: ",degrees)


dict_degree_centrality=nx.degree_centrality(G_normal)
dict_degree_centrality=sorted(dict_degree_centrality.items(), key=operator.itemgetter(1), reverse=True)

print("Degree Centrality: ",dict_degree_centrality)





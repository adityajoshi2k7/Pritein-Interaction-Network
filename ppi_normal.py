import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import operator
from collections import defaultdict

normal = pd.read_excel("bone_normal.xlsx")

normal = normal.loc[normal['R']==1]

normal = normal[['P1','P2']]
normal.to_csv("temp.csv", sep='\t')
df_normal = list(zip(normal.P1, normal.P2))
#normal = pd.DataFrame({'from': normal[['P1']], 'to': normal[['P2']]})

G = nx.Graph()
G.add_edges_from(df_normal)
#print(G.neighbors('4EBP1'))
#print(len(df_normal))
#print(df)
#print(G.edges())
#print(G.nodes())
no_of_nodes = G.number_of_nodes()
no_of_edges = G.number_of_edges()
print("Number of Nodes: ", no_of_nodes)
print("Number of Edges: ", no_of_edges)
pos = nx.spring_layout(G, k=1, iterations=50)
plt.title("PPIN of Normal Human Bone")
nx.draw(G, node_size=10, font_size=8, with_labels=True)

plt.savefig("normal.png")

print("Average Clustering Coefficient: ",nx.average_clustering(G))

print("Number of Cnnected Components: ",nx.number_connected_components(G))

print("Diameter of the graph:  ",nx.diameter(G))

degrees = [[node,val] for (node, val) in G.degree()]
degrees.sort(key=lambda x: x[1],reverse=True)
degree_map = defaultdict(int)

print("Degree: ",degrees)

for each in degrees:
	degree_map[each[1]] += 1

#print(list(degree_map))
lists=sorted(degree_map.items())
#degree_map = dict(degree_map)
#print(degree_map)
x,y = zip(*lists)
#print(x)
#print(y)
plt.clf()
plt.plot(x,y)
plt.title("Degree Distribution of Normal Human Bone PPIN")
plt.ylabel("No. of vertices")
plt.xlabel("Degree")
#plt.show()
plt.savefig("degreeDist.png")

hub_proteins = [degree for degree in degrees if degree[1] >= 12]

print("hub: ", len(hub_proteins))

max_no_edges = no_of_nodes*(no_of_nodes-1)/2

connectivity = float(no_of_edges)/max_no_edges
print("Connectivity : ", connectivity)

avg_no_neighbours = float(sum(degree for _, degree in degrees))/no_of_nodes
print("Average number of neighbours : ", avg_no_neighbours)

btwn_centrality = sorted(nx.betweenness_centrality(G).items(), key=operator.itemgetter(1), reverse=True)
print("Betweenness Centrality: ", btwn_centrality)

dict_degree_centrality = nx.degree_centrality(G)
dict_degree_centrality = sorted(dict_degree_centrality.items(), key=operator.itemgetter(1), reverse=True)

print("Degree Centrality: ",dict_degree_centrality)

print("Closeness Centrality: ", nx.closeness_centrality(G))

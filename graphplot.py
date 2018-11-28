import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

plt.bar(['Cancerous','Normal'],[351,192],color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Number of Nodes')
plt.title('Number of Nodes in PPIN')
plt.savefig('no_of_Nodes.png')

plt.clf()

plt.bar(['Cancerous','Normal'],[1783,619] ,color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Number of Edges')
plt.title('Number of Edges in PPIN')
plt.savefig('no_of_Edges.png')

plt.clf()
plt.bar(['Cancerous','Normal'],[7,7] ,color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Diameter of Graph')
plt.title('Diameter of PPIN')
plt.savefig('diameter.png')

plt.clf()
plt.bar(['Cancerous','Normal'],[1,1],color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Number of Connected Components')
plt.title('Connected Components')
plt.savefig('connected_components.png')


plt.clf()
plt.bar(['Cancerous','Normal'],[95,29],color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Number of Hub Proteins')
plt.title('Hub Proteins')
plt.savefig('hub.png')


plt.clf()
plt.bar(['Cancerous','Normal'],[0.029,0.033],color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Connectivity')
plt.title('Network Connectivity')
plt.savefig('connectivity.png')

plt.clf()
plt.bar(['Cancerous','Normal'],[10.15,6.447],color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Average number of Neighbors')
plt.title('Average number of Neighbors')
plt.savefig('neighbors.png')


plt.clf()
plt.bar(['Cancerous','Normal'],[0.22900,0.20992],color=['indianred','mediumseagreen'])
plt.xlabel('Type of Bone Tissue')
plt.ylabel('Average Clustering Coefficient')
plt.title('Average Clustering Coefficient')
plt.savefig('cluster_coeff.png')

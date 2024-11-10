from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = nx.Graph()

    def getYears(self):
        return DAO.getYears()

    def getStates(self,year):
        return DAO.getStates(year)

    def buildGraph(self,year,state):
        self._grafo.clear()

        self.nodes = DAO.getAllNodes(year,state)
        self._grafo.add_nodes_from(self.nodes)

        for i in range(0,len(self.nodes)-1):
            for j in range(i+1,len(self.nodes)):
                if self.nodes[i].shape == self.nodes[j].shape and self.nodes[i].distance_HV(self.nodes[j]) < 100:
                    self._grafo.add_edge(self.nodes[i],self.nodes[j])

    def getGraphDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)

    def getNumConnesse(self):
        conn = list(nx.connected_components(self._grafo))
        return len(conn)

    def largestConnessa(self):
        conn = list(nx.connected_components(self._grafo))
        conn.sort(key= lambda x : len(x),reverse=True)
        return conn[0]



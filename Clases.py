import numpy as np

class Node:
    """A graph node with a label, its connections and its Dijkstra state."""
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.path_cost = np.inf   
        self.edges = []          
        self.came_from = None     
        self.visited = False

    def __repr__(self):
        return f"Node({self.name})"

class Edge:
    def __init__(self, first_node, second_node, weight):
        if weight < 0:
            raise ValueError("Dijkstra does not support negative weights")
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def other(self, node):
        return self.second_node if node is self.first_node else self.first_node

    def __repr__(self):
        return f"Edge({self.first_node.name}-{self.second_node.name}, {self.weight})"

class Graph:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def add_node(self, name, x=0, y=0):
        node = Node(name, x, y)
        self.nodes.append(node)
        return node

    def add_connection(self, node_a, node_b, weight):
        edge = Edge(node_a, node_b, weight)
        node_a.edges.append(edge)
        node_b.edges.append(edge)
        self.connections.append(edge)
        return edge

    def reset(self):
        for node in self.nodes:
            node.path_cost = np.inf
            node.came_from = None
            node.visited = False

def find_lowest_cost(node_list):
    lowest = np.inf
    index = -1
    for i in range(len(node_list)):
        if node_list[i].path_cost < lowest:
            lowest = node_list[i].path_cost
            index = i
    return index

def mark_visited(node, unvisited, visited):
    unvisited.remove(node)
    visited.append(node)
    node.visited = True

def update_costs(current_node):
    for edge in current_node.edges:
        neighbor = edge.other(current_node)
        if neighbor.visited:
            continue
        new_cost = current_node.path_cost + edge.weight
        if new_cost < neighbor.path_cost:
            neighbor.path_cost = new_cost
            neighbor.came_from = current_node

def rebuild_path(end_node):
    path = []
    node = end_node
    while node is not None:
        path.append(node)
        node = node.came_from
    path.reverse()
    return path

def dijkstra(graph, start_node, end_node):
    """Executes Dijkstra and saves its steps for graphing later. Duplicated from implementation.py since that is a standalone testing script."""
    graph.reset()
    start_node.path_cost = 0

    unvisited = graph.nodes.copy()
    visited_history = []

    while unvisited:
        index = find_lowest_cost(unvisited)
        if index == -1:
            break
        current = unvisited[index]

        mark_visited(current, unvisited, visited_history)

        if current is end_node:
            break

        update_costs(current)

    if end_node.path_cost == np.inf:
        return np.inf, [], visited_history

    return end_node.path_cost, rebuild_path(end_node), visited_history
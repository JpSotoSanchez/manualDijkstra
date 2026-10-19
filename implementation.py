import numpy as np
import Clases


def dijkstra(graph, start_node, end_node):
    graph.reset()
    start_node.path_cost = 0

    unvisited = graph.nodes.copy()
    visited = []

    while unvisited:
        index = Clases.find_lowest_cost(unvisited)
        if index == -1:
            break 
        current = unvisited[index]

        Clases.mark_visited(current, unvisited, visited)

        if current is end_node:
            break

        Clases.update_costs(current)

    if end_node.path_cost == np.inf:
        return np.inf, []
    return end_node.path_cost, Clases.rebuild_path(end_node)


def build_example_graph():
    graph = Clases.Graph()

    A = graph.add_node("A")
    B = graph.add_node("B")
    C = graph.add_node("C")
    D = graph.add_node("D")
    E = graph.add_node("E")
    F = graph.add_node("F")

    graph.add_connection(A, B, 2)
    graph.add_connection(A, C, 3)
    graph.add_connection(B, D, 2)
    graph.add_connection(B, C, 1)
    graph.add_connection(B, E, 2)
    graph.add_connection(C, E, 3)
    graph.add_connection(E, F, 2)
    graph.add_connection(D, F, 5)

    return graph, A, F


if __name__ == "__main__":
    graph, start_node, end_node = build_example_graph()

    total_cost, path = dijkstra(graph, start_node, end_node)

    if path:
        print("Shortest path:", " -> ".join(node.name for node in path))
        print("Total weight:", total_cost)
    else:
        print(f"No path from {start_node.name} to {end_node.name}")
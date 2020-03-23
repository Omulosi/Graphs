from util import Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for group in ancestors:
        graph.add_vertex(group[0])
        graph.add_vertex(group[1])
        graph.add_edge(group[1], group[0])

    queue = Queue()
    queue.enqueue([starting_node])

    longest_path_length = 1
    earliest_so_far = starting_node

    while queue.size() > 0:
        path = queue.dequeue()
        current_node = path[-1]

        if (len(path) > longest_path_length) or (len(path) == longest_path_length and current_node < earliest_so_far):
            earliest_so_far = current_node
            longest_path_length = len(path)

        for next_vert in graph.get_neighbors(current_node):
            new_path = list(path)
            new_path.append(next_vert)
            queue.enqueue(new_path)

    if earliest_so_far == starting_node:
        return -1
    return earliest_so_far

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Invalid vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)

        visited_nodes = set()

        while queue.size() > 0:
            current_vertice = queue.dequeue()

            if current_vertice not in visited_nodes:
                visited_nodes.add(current_vertice)
                print(current_vertice)

                for vertice in self.get_neighbors(current_vertice):
                    queue.enqueue(vertice)

    def dft(self, starting_vertex_id):
        s = Stack()
        s.push(starting_vertex_id)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, start_vert, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_vert)

        print(start_vert)

        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue([starting_vertex_id])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()

            vert = path[-1]

            if vert not in visited:
                if vert == target_value:
                    return path
                visited.add(vert)
                for next_vert in self.vertices[vert]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)

        return None

    def dfs(self, starting_vertex_id, target_value):
        s = Stack()
        s.push([starting_vertex_id])
        visited = set()

        while s.size() > 0:
            path = s.pop()

            vert = path[-1]

            if vert not in visited:
                if vert == target_value:
                    return path
                visited.add(vert)
                for next_vert in self.vertices[vert]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth - first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                new = self.dfs_recursive(
                    vertex, target_value, visited, path)

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

"""Útkereső scriptje"""

from collections import deque


class PathFinding:
    """Útkeresőt reprezentáló osztály"""

    def __init__(self, game):
        self.game = game
        self.map = self.game.map.mini_map
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], \
                    [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.graph = {}
        self.get_graph()
        self.visited = 0

    def get_path(self, start, goal):
        """Utat lekérő, annak végével visszatérő függvény"""

        self.visited = self.bfs(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        while step and step != start:
            path.append(step)
            step = self.visited[step]
        return path[-1]

    def bfs(self, start, goal, graph):
        """Szélességi bejárást (Breadth First Search, BFS)
         megvalósító függvény"""

        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break
            next_nodes = graph[cur_node]

            for next_node in next_nodes:
                if next_node not in visited and next_node \
                        not in self.game.object_handler.npc_positions:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return visited

    def get_next_nodes(self, x, y):  # pylint: disable=invalid-name
        """Következő nodeot lekérő és azzal visszatérő függvény"""

        return [(x + d_x, y + d_y) for d_x, d_y in self.ways
                if (x + d_x, y + d_y) not in self.game.map.world_map]

    def get_graph(self):
        """Játéktérből grafikont csináló függvény"""

        for y, row in enumerate(self.map):  # pylint: disable=invalid-name
            for x, col in enumerate(row):  # pylint: disable=invalid-name
                if not col:
                    self.graph[(x, y)] = self.graph.get((x, y), []) \
                                         + self.get_next_nodes(x, y)

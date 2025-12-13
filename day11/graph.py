from day11.node import Node


class Graph:
    def __init__(self, nodes: dict[str, Node]) -> None:
        self.nodes = nodes

    @staticmethod
    def create(input: list[str]) -> Graph:
        nodes: dict[str, Node] = {}
        for line in input:
            node = Node.create(line)
            nodes[node.name] = node
        graph = Graph(nodes)
        return graph

    def find_all_paths(self, from_node: str = "you", to_node: str = "out") -> list[list[str]]:
        results: list[list[str]] = []
        start = self.nodes[from_node]
        stack: list[tuple[Node, list[str]]] = [(start, [start.name])]
        while stack:
            current_node, path = stack.pop()
            if current_node.name == to_node:
                results.append(path)
                continue
            for next_node_name in current_node.next_nodes:
                if next_node_name not in path:
                    if next_node_name == to_node:
                        results.append(path + [next_node_name])
                        continue
                    next_node = self.nodes.get(next_node_name)
                    if next_node:
                        stack.append((next_node, path + [next_node.name]))
        return results
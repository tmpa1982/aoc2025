from day11.node import Node


class Graph:
    def __init__(self, nodes: dict[str, Node]) -> None:
        self.nodes = nodes
        self.nodes["out"] = Node("out", [])

    @staticmethod
    def create(input: list[str]) -> Graph:
        nodes: dict[str, Node] = {}
        for line in input:
            node = Node.create(line)
            nodes[node.name] = node
        graph = Graph(nodes)
        return graph

    def find_all_paths(self) -> list[list[str]]:
        results: list[list[str]] = []
        start = self.nodes["you"]
        stack: list[tuple[Node, list[str]]] = [(start, [start.name])]
        while stack:
            current_node, path = stack.pop()
            if current_node.name == "out":
                results.append(path)
                continue
            for next_node_name in current_node.next_nodes:
                if next_node_name not in path:
                    next_node = self.nodes.get(next_node_name)
                    if next_node:
                        stack.append((next_node, path + [next_node.name]))
        return results
class Node:
    def __init__(self, name: str, next_nodes: list[str]) -> None:
        self.name = name
        self.next_nodes = next_nodes
    
    @staticmethod
    def create(s: str) -> Node:
        parts = s.split(" ")
        name = parts[0].strip(":")
        next_nodes = parts[1:]
        return Node(name, next_nodes)

    def __repr__(self) -> str:
        return f"Node({self.name} -> {self.next_nodes})"
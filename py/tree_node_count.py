
"""
          []
   []   []   []   []
[]  []  [] [] ....

"""


n = 4

mp = {} 
class Node:
    node_id: int
    children_nodes: list["Node"] # max size of n
 
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children_nodes = []
    
    def sendMessage(self, to_node_id, message):
        # only called
        # to_node_id should get the msg 
        mp[to_node_id].receiveMessage(self.node_id, message)
        pass
    
    def receiveMessage(self, from_node_id, message) -> None:
        
        # send message to children to get counts (they will receive)
        if message == 'count':
            # first msg node receives
            self.count = 1
            self.parent = from_node_id
            self.processed = 0

            # dispatch msgs to get counts
            # leaf node edge case - need to send 1 to parent
            if len(self.children_nodes) == 0:
                self.sendMessage(from_node_id, 1)
            for child in self.children_nodes:
                self.sendMessage(child.node_id, "count")
        elif isinstance(message,int):
            self.count += int(message)
            self.processed += 1
            # on last receive, send count to parent
            if self.processed == len(self.children_nodes):
                if self.parent == None: # root node
                    print(self.count)
                else:
                    self.sendMessage(self.parent, self.count)
                        # after we receive all msgs, send its count to parent (we will get msgs)

        pass

def build_n_ary_tree(n: int, height: int, start_id=1):
    def create_node(current_height, next_id):
        node = Node(next_id)
        mp[next_id] = node
        next_id += 1
        if current_height < height:
            for _ in range(n):
                child, next_id = create_node(current_height + 1, next_id)
                node.children_nodes.append(child)
        return node, next_id

    root, _ = create_node(1, start_id)
    return root

def print_tree(node, level=0):
    print(" " * (level * 2) + f"Node {node.node_id}")
    for child in node.children_nodes:
        print_tree(child, level + 1)


# root node gets creceiveMessage(null, message).


root = build_n_ary_tree(n=n, height=3)
print_tree(root)

print()
print()
root.receiveMessage(None, "count")











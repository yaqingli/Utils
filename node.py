
class Node(object):
    def __init__(self, value):
        self.value = value
        #self.children = []
        self.first_child = None
        self.last_child = None
        self.next = None
        self.previous = None
        self.parent = None
    def add(self, node):
        if self.has_child() == False:
            self.first_child = node
            self.last_child = node
        #self.children.append(node)
        if self.last_child:
            self.last_child.next= node
        self.last_child = node
        node.parent = self
        return node
    def add_value(self, value):
        return self.add(Node(value))
    def remove(self, node):
        child = self.first_child
        while True:
            if child == node:
                child
    def has_child(self):
        return len(self.children)>0
    def get_first_child(self):
        return self.first_child
    def next_sibling(self):
        return self.next
    def get_parent(self):
        return self.parent
    def get_value(self):
        return self.value
    def is_leaf(self):
        return self.has_child()==False


class Edge(object):
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child


def next(node, level=0):
    if node.has_child():
        return node.get_first_child(), level+1
    elif node.next_sibling():
        return node.next_sibling(), level
    else:
        p = node.get_parent()
        level -= 1
        while p:
            if p.next_sibling():
                return p.next_sibling(), level
            p = p.get_parent()
            level -= 1
        return None, level


def search(tree, value):
    node, _ = next(tree)
    while node:
        if node.get_value() == value:
            return node
        node, _ = next(node)
    return None

def make_trees(edges):
    """
    edges:[['a', 'b'], ['b', 'c']]
    """
    root = Node(None)
    nodes = dict()
    for edge in edges:
        parent_node = nodes.get(edge.parent)
        if parent_node is None:
            parent_node = root.add_value(edge.parent)
            nodes[edge.parent] = parent_node
        child_node = nodes.get(edge.child)
        if child_node is None:
            child_node = Node(edge.child)
            nodes[edge.child] = child_node
        elif child_node in parent_node.children:
            if child_node.get_parent() == root:
                root.remove(child_node)
            else:
                continue #duplicate
        parent_node.add(child_node)
    return root, nodes
    


def print_tree(tree):
    next_node, level = next(tree)
    while next_node:
        print('----'*level, next_node.value)
        next_node, level = next(next_node, level)

def print_tree1(tree):
    print(tree.children)

def test():
    nodes = [['a0', 'b00'], ['a0', 'b01'], ['a0', 'b02'], ['b00', 'c00'], ['b00', 'c01'], ['a1', 'b11'], ['a2', 'b20']]
    edges = [Edge(node[0], node[1]) for node in nodes]
    root = make_trees(edges)
    print_tree(root)


def load_data():
    file_path = '/Users/liyaqing/Downloads/flows'
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip().split('\t') for line in lines]


import time
def test1():
    edges = load_data()
    edges = [Edge(edge[0], edge[1]) for edge in edges]
    start = time.time()
    root, nodes = make_trees(edges)
    print(time.time() - start)
    print(len(nodes))
    return root, nodes


if __name__ == "__main__":
    test1()

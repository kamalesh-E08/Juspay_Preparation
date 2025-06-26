class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.is_locked = False
        self.locked_by = None
        self.locked_decendent_cnt = 0
        
class LockingTree:
    def __init__(self, names, m):
        self.name_to_node = {}
        self.nodes = []
        # Initialize nodes for each name
        for name in names:
            node = Node(name)
            self.name_to_node[name] = node
            self.nodes.append(node)
        # Set the root node 
        for i in range(1, len(names)):
            parent = self.names[(i - 1)//m]
            self.nodes[i].parent = parent
            parent.children.append(self.nodes[i])
            
    def can_lock(self, node):
        current = self.name_to_node[node]
        # Check if any ancestor is locked
        while current:
            if current.is_locked:
                return False
            current = current.parent
        if node.locked_decendent_cnt > 0:
            return False
        return True
    
    def lock(self, X, uid):
        if self.can_lock(X):
            node = self.name_to_node[X]
            node.is_locked = True
            node.locked_by = uid
            current = self.name_to_node[X].parent
            while current:
                current.locked_decendent_cnt += 1
                current = current.parent
            return True
        return False
    
    def unlock(self, X, uid):
        node = self.name_to_node[X]
        if node.is_locked and node.locked_by == uid:
            node.is_locked = False
            node.locked_by = None
            current = node.parent
            while current:
                current.locked_decendent_cnt -= 1
                current = current.parent
            return True
        return False
            
    def upgrade(self, X, uid):
        node = self.name_to_node[X]
        if node.is_locked or node.locked_decendent_cnt == 0:
            return False
        decendents = [node]
        locked_decendents = []
        while decendents:
            current = decendents.pop()
            for child in current.children:
                if child.is_locked and child.locked_by != uid:
                    return False    
                if child.is_locked:
                    locked_decendents.append(child)
                    
                decendents.append(child)
        for n in locked_decendents:
            self.unlock(n.name, uid)
        self.lock(X, uid)
        return True
        
        
    
        
n = int(input())
m = int(input())
q = int(input())
names = [input().strip() for _ in range(n)]
tree = LockingTree(names, m)    

for _ in range(q):
    query = input().strip().split()
    if query[0] == "1":
        X = query[1]
        uid = int(query[2])
        print(tree.lock(X, uid))
    elif query[0] == "2":
        X = query[1]
        uid = int(query[2])
        print(tree.unlock(X, uid))
    elif query[0] == "3":
        X = query[1]
        uid = int(query[2])
        print(tree.upgrade(X, uid))
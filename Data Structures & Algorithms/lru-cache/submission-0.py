class TreeNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = TreeNode(0, 0), TreeNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.myDict = {}
        
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev, node.next = prev, self.right


    def get(self, key: int) -> int:
        if key in self.myDict:
            self.delete(self.myDict[key])
            self.insert(self.myDict[key])
            return self.myDict[key].val
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.myDict:
            self.delete(self.myDict[key])
        self.myDict[key] = TreeNode(key, value)
        self.insert(self.myDict[key])
        if len(self.myDict) > self.capacity:
            ntd = self.left.next
            self.delete(ntd)
            del self.myDict[ntd.key]

        

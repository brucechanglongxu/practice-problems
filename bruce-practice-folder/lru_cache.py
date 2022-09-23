class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.dic:
            return -1
        n = self.dic[key]
        self._removeElement(n)
        self._addElement(n)
        return n.val

    def put(self, key, value):
        if key in self.dic:
            self._removeElement(self.dic[key])
        
        n = Node(key, value)
        self._addElement(n)
        self.dic[key] = n
        
        if len(self.dic) > self.capacity:
            nodeToDelete = self.head.next
            self._removeElement(nodeToDelete)
            del self.dic[nodeToDelete.key]

    def _removeElement(self, node):
        previous = node.prev
        next = node.next
        previous.next = next
        next.prev = previous
        
    def _addElement(self, node):
        last = self.tail.prev
        last.next = node
        self.tail.prev = node        
        node.next = self.tail
        node.prev = last

# don't use OrderedDict, use Linked List instead

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: Node
        # set head and tail
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self,node: Node) -> None:
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev

    def _add_to_end(self, node:Node) -> None:
        # insert at the end, before tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove_node(self.cache[key])
            self._add_to_end(self.cache[key])
            return self.cache[key].value
        return -1  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            node.value = value
        else:
            node = Node(key, value)
            self.cache[key] = node
        self._add_to_end(node)

        if len(self.cache) > self.capacity:
            next = self.head.next
            self._remove_node(next)
            del self.cache[next.key]


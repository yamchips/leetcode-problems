class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # initial linked list
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _disconnect_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        node.prev = None
        node.next = None
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node: Node):
        current_last = self.tail.prev
        current_last.next = node
        node.prev = current_last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        # check whether it's in cache
        # if not, return -1
        if key not in self.cache:
            return -1

        # else, disconnect the node, move it in front of tail
        # return the value 
        node = self.cache[key]
        self._disconnect_node(node)
        self._move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # check whether it's in cache
        # if so, update the node's value, disconnect the node
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._disconnect_node(node)
        else:
            # if not, add it to cache, in front of tail
            node = Node(key, value)
            self.cache[key] = node

        self._move_to_end(node)

        # check capacity
        if len(self.cache) > self.capacity:
            # disconnect first node
            first_node = self.head.next
            self._disconnect_node(first_node)
            del self.cache[first_node.key]

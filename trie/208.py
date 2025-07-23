class Node:
    def __init__(self):
        self.children = {} # char -> Node
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        parent = self.root
        for char in word:
            if char not in parent.children:
                parent.children[char] = Node()
            parent = parent.children[char]
        parent.isEnd = True
        
    def search(self, word: str) -> bool:
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]    
        return parent.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]    
        return True   


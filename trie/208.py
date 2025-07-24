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
        
    # dfs
    def search(self, word: str) -> bool:
        def dfs(node: Node, i: int) -> bool:
            if i == len(word):
                return node.isEnd
            char = word[i]
            if char not in node.children:
                return False
            return dfs(node.children[char], i + 1)
        return dfs(self.root, 0)
    
    # Iterative way
    # def search(self, word: str) -> bool:
        # parent = self.root
        # for char in word:
        #     if char not in parent.children:
        #         return False
        #     parent = parent.children[char]    
        # return parent.isEnd
        
    # dfs
    def startsWith(self, prefix: str) -> bool:
        def dfs(node: Node, i: int) -> bool:
            if i == len(prefix):
                return True
            char = prefix[i]
            if char not in node.children:
                return False
            return dfs(node.children[char], i + 1)
        return dfs(self.root, 0)
    
    # Iterative way
    # def startsWith(self, prefix: str) -> bool:
        # parent = self.root
        # for char in prefix:
        #     if char not in parent.children:
        #         return False
        #     parent = parent.children[char]    
        # return True   

if __name__=='__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('app'))
    print(trie.startsWith('app'))
    trie.insert('app')
    print(trie.search('app'))
    print(trie.startsWith('app'))

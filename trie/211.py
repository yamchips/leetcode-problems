class Node:
    def __init__(self):
        self.children = {} # char -> Node
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        parent = self.root
        for char in word:
            if char not in parent.children:
                parent.children[char] = Node()
            parent = parent.children[char]
        parent.isEnd = True
        
    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if node.isEnd:
                    return True
                continue
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    stack.append((child, i + 1))
            if char in node.children:
                stack.append((node.children[char], i + 1))
        return False

    # dfs
    def searchDfs(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.isEnd
            char = word[i]
            if char == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            if char not in node.children:
                return False
            return dfs(node.children[char], i + 1)
        return dfs(self.root, 0)
        
if __name__=='__main__':
    trie = WordDictionary()
    trie.addWord('bad')
    trie.addWord('dad')
    trie.addWord('mad')
    trie.search('.ad')
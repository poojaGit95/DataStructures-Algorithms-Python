class TrieNode:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.endOfString = True

    def search(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endOfString

    def startsWith(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

t = Trie()
t.insert("apple")
t.insert("api")
t.insert("xyz")
print(t.search("xyz"))
print(t.startsWith("pp"))

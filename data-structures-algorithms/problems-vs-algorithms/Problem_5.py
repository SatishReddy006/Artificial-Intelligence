## Represents a single node in the Trie
class TrieNode:
    def __init__(self,char=""):
        ## Initialize this node in the Trie
        self.char = word
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = self.children.get(char, TrieNode(char))
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffix_list = []
        for word in self.children:
            if self.children[word].children:
                suffix_list.extend(self.children[word].suffixes(suffix + word))
            elif word == '\x00':
                suffix_list.append(suffix)
        return suffix_list
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = {}

    def insert(self, word):
        ## Add a word to the Trie
        self.root[word[0]] = self.root.get(word[0], TrieNode(word[0]))
        current_node = self.root[word[0]]
        for i in range(1, len(word)):
            current_node.insert(word[i])
            current_node = current_node.children[word[i]]

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if not prefix:
            return self.root

        if prefix[0] not in self.root:
            return None

        current_node = self.root[prefix[0]]
        if current_node:
            for i in range(1, len(prefix)):
                if prefix[i] not in current_node.children:
                    return None
                current_node = current_node.children[prefix[i]]
        return current_node


#Testing
MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word+'\0')


print(MyTrie.find('f').suffixes())  #return ['un', 'unction', 'actory']
print(MyTrie.find('t').suffixes())  #return ['rie', 'rigger', 'rigonometry', 'ripod']
print(MyTrie.find('h'))             #return None
print(MyTrie.find('the'))           #return None
print(MyTrie.find('1'))             #return None
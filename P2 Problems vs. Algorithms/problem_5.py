class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            new_node =  TrieNode()
            self.children[char] = new_node      
        
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        node = self
        for char in suffix:
            print(char)
            node = node.children[char]
        
        suffixed_list = []
        for char,node in node.children.items():
            if node.is_word:
                suffixed_list.append(char)
            suffixed_list += [char + x for x in node.suffixes()]
        return suffixed_list
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        
        node.is_word = True
            
            
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

# Test case 1:
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print('Test case 1: ')
print('Word List: ',wordList)
print("\nUse prefix \'\': ")
f('')
# Return: 
#          ''

print("\nUse prefix \'a\': ")
f('a')
# Return: 
#       nt
#       nthology
#       ntagonist
#       ntonym

print("\nUse prefix \'an\': ")
f('an')
# Return: 
#       t
#       thology
#       tagonist
#       tonym

print("\nUse prefix \'fu\': ")
f('fu')
# Return: 
#       n
#       nction

print("\nUse prefix \'tri\': ")
f('tri')
# Return: 
#       e
#       gger
#       gonometry
#       pod

print("\nUse prefix \'trie\': ")
f('trie')
# Return: 
#       ''

print("\nUse prefix \'apple\': ")
f('apple')
# Return: 
#       apple not found




# Test case 2:
MyTrie = Trie()
wordList = []
for word in wordList:
    MyTrie.insert(word)

print('\nTest case 2: ')
print('Word List: ',wordList)
print("\nUse prefix \'\': ")
f('')
# Return: 
#        ''

print("\nUse prefix \'a\': ")
f('a')
# Return: 
#       a not found



# Test case 3:
MyTrie = Trie()
wordList = ['apple','ant','apply',
            'Rock', 'Nirvana', 'Green Day',
            'Happy','Birthday','haha'
            ]
for word in wordList:
    MyTrie.insert(word)

print('\nTest case 3: ')
print('Word List: ',wordList)
print("\nUse prefix \'app\': ")
f('app')
# Return: 
#       le
#       ly

print("\nUse prefix \'N\': ")
f('N')
# Return: 
#        irvana
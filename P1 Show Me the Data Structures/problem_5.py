import hashlib
import datetime  


class Block:

    def __init__(self, data='', previous_hash=None):

        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = (self.data + self.timestamp).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def insert(self,node):
        self.next = node
        node.previous_hash = self.hash



class BlockChain:
    def __init__(self, root_data=''):
        self.root = Block(root_data)
        self.end = None

    def insert(self, data):
        if not self.end:
            self.root.insert(Block(data)) 
            self.end = self.root.next

        else:
            self.end.insert(Block(data))
            self.end = self.end.next

    def printB(self):
        node = self.root
        while node:
            print(node.data)
            node = node.next


print("\nTest case 1:")

bc = BlockChain("Hello, everyone! I'm Groot!")
bc.insert("I'm Star-Lord. I'm the greatest idiot!")
bc.insert("Hi, my name is King Kong. I\'m strong!")
bc.insert("I'm Jack Black. School of Rock!!!")

print('Root hash: ',bc.root.hash) # Change each time
bc.printB()
# Return:
#       Hello, everyone! I'm Groot!
#       I'm Star-Lord. I'm the greatest idiot!
#       Hi, my name is King Kong. I'm strong!
#       I'm Jack Black. School of Rock!!!


print("\nTest case 2:")

bc = BlockChain("Groot is going out!!!")
bc.insert("Groot is getting out of bed!")

print('Root hash: ',bc.root.hash) # Change each time
bc.printB()
# Return:
#       Groot is going out!!!
#       Groot is getting out of bed!

print("\nTest case 3: Groot got lost.")

bc = BlockChain()

print('Root hash: ',bc.root.hash) # Change each time
bc.printB ()
# Return:
#       None
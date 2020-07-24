import hashlib
import datetime  

def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()

class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()



print("\nTest case 1:")
block0 = Block('Hello, everyone!',None)
block1 = Block('Hi, my name is Goose. Nice to meet you.',block0.hash)
block2 = Block('Hi, my name is King Kong. I\'m strong!',block1.hash)
block3 = Block("I'm Jack Black. School of Rock!!!",block2.hash)

print(block1.previous_hash)
# Return: '195e810fc1bf6bf935b9ba805bd5cba1ee56d7d3bf082103eb33d9bda30a16e4'

print(block2.previous_hash)
# Return: '70f7158a509eea5dda976dba7ef2c61e5663cb6a6dbd554f33d9660ae8365e7e'
print(block2.data)
# Return: "Hi, my name is KingKong. I'm strong!"

print(block3.previous_hash)
# Return: '1ecd4529283a1687b2bbec6dbd58935fa3652fed161714aa77db4f84abde776e'
print(block3.data)
# Return: "I'm Jack Black. School of Rock!!!"



print("\nTest case 2:")
block0 = Block('Hello, everyone!',None)
block1 = Block('Hi, my name is Goose. I hate block chain!',block0.hash)

print(block0.previous_hash)
# Return: None
print(block1.previous_hash)
# Return: '195e810fc1bf6bf935b9ba805bd5cba1ee56d7d3bf082103eb33d9bda30a16e4'


print("\nTest case 3:")
print("Zero length block chain. No outputs.") 
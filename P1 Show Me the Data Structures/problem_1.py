from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):

        if self.capacity == 0:
            return -1

        # Retrieve item from provided key. Return -1 if nonexistent.             
        value = self.cache.get(key) or -1
        if value != -1:
            # Put the recently queried data into the top of the ordered dict
            self.cache.pop(key)
            self.cache[key] = value
        return value


    def set(self, key, value):

        if self.capacity  > 0:
            # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
            if len(self.cache) < self.capacity:
                if self.cache.get(key):
                    self.cache.pop(key)
                    
                self.cache[key] = value
                
            else:
                # Remove the least recently used data and insert new value
                least_key = next(iter(self.cache))
                self.cache.pop(least_key)
                self.cache[key] = value
        

# Test case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("Test case 1:")
print(our_cache.get(1))       
# returns 1
print(our_cache.get(2))       
# returns 2
print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.set(7, 7)

print(our_cache.get(4)) 
# returns -1 because the cache reached it's capacity and 4 was the least recently used entry


# Test case 2
our_cache = LRU_Cache(0)

our_cache.set(1, 1);
our_cache.set(2, 2);

print("Test case 2:")
print(our_cache.get(1))       
# returns -1
print(our_cache.get(2))       
# returns -1


# Test case 3
our_cache = LRU_Cache(3)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("Test case 13")
print(our_cache.get(1))       
# returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(our_cache.get(2))       
# returns 2
print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache
print(our_cache.get(4))
# returns 4
print(our_cache.get(3))
# returns 3


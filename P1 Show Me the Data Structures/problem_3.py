import sys
from collections import Counter

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element.getValue() > child_element.getValue():
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                if parent.getValue() < left_child.getValue():
                    min_element = parent
                else:
                    min_element = left_child
            # compare with right child
            if right_child is not None:
                if right_child.getValue() < min_element.getValue():
                    min_element = right_child

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent_index = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent_index = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

class Node:
    def __init__(self,value,name = None):
        self.value = value
        self.name = name
        self.left = None
        self.right = None
        
    def getValue(self):
        return self.value
    
    def getName(self):
        return self.name
    
    def setLeft(self,node):
        self.left = node
        
    def setRight(self,node):
        self.right = node

def get_encoding_dict(root):
    if root.name:
        return {root.name:''}
    else:
        left ={ key: '0'+value for key,value in get_encoding_dict(root.left).items()} 
        right = { key: '1'+value for key,value in get_encoding_dict(root.right).items()}
        return {**left,**right}


def huffman_encoding(data):

	# Use Counter to count every kind of characters
    counter = Counter(data)
    counter = [(key,value) for key,value in counter.items()]
    
    # Use a min-heap to make sure the node with the min value are always at the top 
    heap = Heap(len(counter))
    for element in counter:
        heap.insert(Node(element[1],element[0]))
        
    
    # Iterate and generate the node tree
    while heap.size() >= 2:
        first = heap.remove()
        second = heap.remove()
 
        parent = Node(first.value + second.value)
        parent.setLeft(first)
        parent.setRight(second)
        
        heap.insert(parent)
        
    # Use the generated tree to make the encoding dict for each character
    tree = heap.cbt[0]
    encoding_dict = get_encoding_dict(tree)
    encoded_data = ''.join([encoding_dict[x] for x in data])
    
    return encoded_data, tree

def huffman_decoding(data,tree):
    decoded_data = []

    # Parse through the tree to decode the data
    node = tree
    for x in data:
        if x == '0':
            node = node.left
        else:
            node = node.right

        if node.name:
            decoded_data.append(node.name)
            node = tree
    return ''.join(decoded_data)



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Return: 69

    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Return: "The bird is the word"


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Return: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Return: "0010100011110001100010111101100000100110111101000111100101111111011110"

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Return: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Return: "The bird is the word"
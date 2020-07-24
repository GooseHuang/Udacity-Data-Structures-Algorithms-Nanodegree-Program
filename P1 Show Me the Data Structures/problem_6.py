class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_llist = LinkedList()
    union_set = set()
    union_next = None
    node = llist_1.head
    while node:
        if not node.value in union_set:
            union_set.add(node.value)
            if union_next:
                union_next.next = Node(node.value)
                union_next = union_next.next
            else:
                union_llist.head = Node(node.value)
                union_next = union_llist.head
        
        node = node.next
    
    node = llist_2.head
    while node:
        if not node.value in union_set:
            union_set.add(node.value)
            if union_next:
                union_next.next = Node(node.value)
                union_next = union_next.next
            else:
                union_llist.head = Node(node.value)
                union_next = union_llist.head
        
        node = node.next
    
    return union_llist 

def intersection(llist_1, llist_2):
    # Your Solution Here
    inter_llist = LinkedList()
    
    set1 = set()
    node = llist_1.head
    while node:
        set1.add(node.value)
        node = node.next

    set2 = set()
    node = llist_2.head
    while node:
        set2.add(node.value)
        node = node.next
        
    inter_set = set1.intersection(set2)
    
    inter_next = None
    for x in inter_set:
        if inter_next:
            inter_next.next = Node(x)
            inter_next = inter_next.next
        else:
            inter_llist.head = Node(x)
            inter_next = inter_llist.head
        
    return inter_llist 

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# Return: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print (intersection(linked_list_1,linked_list_2))
# Return: 4 -> 21 -> 6 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Return: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_3,linked_list_4))
# Return: None


# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [9,2,3,6,67]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Return: 9 -> 2 -> 3 -> 6 -> 67 ->
print (intersection(linked_list_3,linked_list_4))
# Return: None



# Test case 4
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [2,5,6,4,7,8]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Return: 2 -> 5 -> 6 -> 4 -> 7 -> 8 ->
print (intersection(linked_list_3,linked_list_4))
# Return: None


# Test case 5
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Return: None
print (intersection(linked_list_3,linked_list_4))
# Return: None
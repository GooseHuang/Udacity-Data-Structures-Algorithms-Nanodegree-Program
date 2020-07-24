I used the basic type set here to help getting the union and intersection of two linked list.

For the time complexity:
Let's assume we have two linked list A and B. A has m nodes, while B has n nodes.

In the union function, we will first iterate and insert all the node values of A to a set. The time complexity of this will be 1 * m, which is O(m) on average while  1 + 2 + 3 + ... +  m = O(m^2) on the worst case.
Then we will iter-through B and insert the element into the set we made previously. 
Same with before, that will be O(n) on average while m+1 + m+2 + m+3 + ... + m+n = O((m+n)*n).

So the whole process of union will be O(m+n) on the average and O((m+n)^2).

In the intersection function, we will first get two separate set for A and B, that will be O(m+n) on average and O(m^2 + n^2) on the worst case. Then we find the intersection of this two sets, which will be O(min(m,n)) on average and O(m*n) on the worst case.
So the whole process of intersection will be O(m+n) and O((m+n)^2).

For the space complexity:
Both the linked list and set takes O(m+n).
So the whole space-complexity is O(m+n).
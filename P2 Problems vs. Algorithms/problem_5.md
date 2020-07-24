For the suffixes function in the TrieNode, I used recursion to get all the words below this node.

For time complexity:
In TrieNode, the insert function takes O(1) and the suffix function will have five elements in its recursion stack, which takes O(k) (k is the number of all nodes under this node).
In the Trie, the insert function takes O(k*1) on the average, while O(k*n) on the worst case (k is the number of characters in the word). And the find function also takes O(k*1) on the average, while O(k*n) on the worst case (k is the number of characters in the  prefix).
So the time complexity is O(n) on the average, while O(n*n) on the worst case. 

For space complexity:
In TrieNode, it will take O(1) in insert function and O(k) in the recursion (k is the number of all nodes under this node).
In Trie, it will take O(n) to store all the nodes.
So the space complexity is O(n).

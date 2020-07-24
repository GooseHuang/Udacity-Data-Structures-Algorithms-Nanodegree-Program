The function is similar as the Trie before.

For time complexity:
In RouteTrie, both the insert and find function will take O(k) on average and O(k*alpha) on the worst cases (k is the number of paths in path_list; alpha is the average children numbers in each layer; so there will n/alpha layers, where n is the number of paths in this Trie). 
In Router, they just call the functions in RouteTrie.
So the time complexity is O(k) on average and O(n) on the worst cases (k is the number of paths in path_list, n is the number of paths in this Trie).

For space complexity:
In RouteTrie, let's assume there are k layers in the RouteTrie and alpha children for each layer, so the number of spaces it takes will be alpha^k, which will be n, the number of paths we have here. In this way,  we avoided to store the same previous road of too paths, which will be k times the size we are using now on average. So we have saved our path to 1/log(n) times.
The space complexity is O(n).

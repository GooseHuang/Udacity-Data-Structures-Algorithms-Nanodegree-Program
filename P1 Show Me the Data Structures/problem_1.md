I used OrderedDict and linked list here as it will keep the insert order automatically and I can always make the recently called data at the top of the list. 

For the time complexity:
As there is no loop in our class and the Big-O for OrderedDict set or get is O(1) on average and O(n) on worst, so the Big-O for this code is O(n)

For the space complexity:
As it keep using the same cache dict, it will be O(capacity)
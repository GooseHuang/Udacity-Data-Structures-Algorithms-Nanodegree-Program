The key ideal is that if we can first find the min value, we can then use the list like a sorted listed where the binary tree can be applied. So we can best use its information and make it efficient.
So I used a binary search like method here to compare the first,mid and last value and narrow the range in each loop. Once the range is less than two, we know we have found the start index.
 
For the time complexity:
It will take log(n) steps to find the start index and another log(n) steps to find if the target value are in the list. 
So the time complexity is O(log(n)).

For the space complexity:
Each call uses O(1) space, and the maximum depth of the recursive tree is O(log(n).
So the space complexity is O(log(n))  

Reference:
https://www.ideserve.co.in/learn/time-and-space-complexity-of-recursive-algorithms
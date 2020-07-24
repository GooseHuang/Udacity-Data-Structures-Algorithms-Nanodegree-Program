I chose a while loop here for it's much more direct and easier to understand than recursion. For each iteration, I will cut the range to half and calculate the squared value. If the squared middle is less than the target value, then set as new lower boundary, else set as upper boundary. In this way, we can reach to the square root within log(n) steps. 


For time complexity:
Let's say n is the number of digits of the input number.
It takes about approximate n steps to iterate and approximate n/2 * n/2 steps for multiplication in each step (Assume multiplication method takes O(k), based on the reference, the time complexity of multiplication will be O(k*k)).
So it will be O(n^3) on the whole.

For space complexity:
As it just calculates one mid square value on each step and update it timely, the space complexity will be O(n) on each multiplication, based on the reference.
So the space complexity will be O(n).


Reference:
https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations
https://en.wikipedia.org/wiki/Multiplication_algorithm#Optimizing_space_complexity
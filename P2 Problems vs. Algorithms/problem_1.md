I chose a while loop here for it's much more direct and easier to understand than recursion.

For time complexity:
As it takes log2(n) steps to iterate and approximate n^0.5 * n^0.5 steps for multiplication in each step,
so it will be O(log2(n)*n) on the whole.

For space complexity:
As it just calculates one mid square value on each step and update it timely, the space complexity will be O(1).

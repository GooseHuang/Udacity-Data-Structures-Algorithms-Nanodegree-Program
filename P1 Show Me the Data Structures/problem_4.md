I used recursion to check all the subgroups automatically.

For time complexity:
And The function will iter-through each users. If there is n users, the checking of an users' existence will be n step at most.
So the Big-O is O(n).

For space complexity:
The function will create an instance for every group.
So the complexity on space will be O(n) (n for number of groups). 
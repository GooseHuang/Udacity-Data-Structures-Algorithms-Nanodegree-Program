I used recursion to check all the subgroups automatically.

For time complexity:
Let's assume there are n users and k groups, so the average time of searching all the children of one group is O(1) on average and O(n/k) on the worst cases. Let's assume we need to search all the groups until we make sure the user's existence. So that will be O(1*k) on average, while O(n/k*k) on the worst cases.
So the time complexity is O(n).

And The function will iter-through each users. If there is n users, the checking of an users' existence will be n step at most.
So the Big-O is O(n).

For space complexity:
The function will create an instance for every group.
So the complexity on space will be O(n) (n for number of groups). 
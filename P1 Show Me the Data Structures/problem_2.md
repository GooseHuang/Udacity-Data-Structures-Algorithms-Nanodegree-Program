I added a recursion here as it will automatically check all the sub-folders. I just need to add the parent location to it.

For the time complexity:
As the program just iter-through every files and do the same operations on each. 
So if there is n files under this folder, no matter what is the sub-hierarchy, there will always be n steps in the whole.
So The Big-O is O(n) for this code.

For the space complexity:
As it do the recursion, it will create an instance for each folder and add them to stacks.
So the space complexity is O(n) (n for number of folders). 
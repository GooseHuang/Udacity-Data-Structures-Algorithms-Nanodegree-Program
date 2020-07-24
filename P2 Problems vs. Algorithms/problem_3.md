The key point is to put the big elements at head of the arranged numbers. So I need to sort the whole list first. 
I chose merge-sort here as there is no better way than this if you want to sort the whole list.
Then I begin to apportion the elements. 
As the number of digits in both numbers cannot differ by more than 1, I should assign the max element to the one with longer digits and second largest element to the other one, etc.
By doing this, I can make sure my arranged numbers are one of the largest combinations.

For the time complexity:
The merge sort takes O(n*log(n)), while the later apportion process takes O(n). Simple and clear.
So the time complexity is O(n*log(n)).

And the space complexity is O(n).

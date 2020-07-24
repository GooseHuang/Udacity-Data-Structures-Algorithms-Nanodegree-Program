I used min-heap here as it will efficient put the smallest value at the top, which will make the logic much more clear and easier. 


For the time complexity:
As
	The counter takes O(n) time;
	The up-heapify and down-heapify take log(n) time;
	Heap sort insert all the element into one heap is log(1) + log(2) + ... + log(n) = log(n!);
	get_encoding_dict takes O(1*n) on average, while O(n*n) on the worst cases.
So the encoding process is O(log(n!)), which approximate to O(n*log(n)).

While The decoding process is O(n).

So the whole process is O(n*log(n)) on average, while O(n*n) on the worst cases.


For the space complexity:
Let n be the number of characters, and k be the number of distinct characters.
As
	The counter takes O(k);
	The heap doesn't take more spaces and the space is O(k);
	get_encoding_dict takes O(k);
	Encoding and decoding the string with tree and dict is O(n).
So the whole process is O(n) on space.
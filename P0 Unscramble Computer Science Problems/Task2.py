"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""



time_list = []
for call in calls:
	# print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*call))
	time_list.append(int(call[3]))

max_time = max(time_list)


max_call = []
for call in calls:
	# print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*call))
	if int(call[3]) == max_time:
		max_call.append(call[0])
		max_call.append(call[1])


print("{} spent the longest time, {} seconds, on the phone during \
September 2016.".format(', '.join(set(max_call)),max_time))

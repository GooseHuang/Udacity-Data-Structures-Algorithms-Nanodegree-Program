import csv
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

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
time_dict = {}
for call in calls:
	if call[0] in time_dict.keys():
		time_dict[call[0]] += int(call[3])
	else:
		time_dict[call[0]] = int(call[3])

	if call[1] in time_dict.keys():
		time_dict[call[1]] += int(call[3])
	else:
		time_dict[call[1]] = int(call[3])

max_time = max(time_dict.values())

max_calls = []
for key, value in time_dict.items():
	if value == max_time:
		max_calls.append(key) 

print("{} spent the longest time, {} seconds, on the phone during \
September 2016.".format(' ,'.join(max_calls),max_time))

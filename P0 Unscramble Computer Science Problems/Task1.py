import csv
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
number_list = []
for text in texts:
	number_list.append(text[0])
	number_list.append(text[1])


for call in calls:
	number_list.append(call[0])
	number_list.append(call[1])

print("There are {} different telephone numbers in the records.".format(len(set(number_list))))
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

send_text = []
receive_text = []
receive_call = []
outgoing_call = []


for text in texts:
	# print("First record of texts, {} texts {} at time {}".format(*text))
	send_text.append(text[0])

	receive_text.append(text[1])

for call in calls:
	# print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*call))
	outgoing_call.append(call[0])
	receive_call.append(call[1])


telemarketers = set(outgoing_call) - set(receive_call) - set(send_text) - set(receive_text)
telemarketers = sorted(list(telemarketers))

"These numbers could be telemarketers: "
for x in telemarketers:
	print(x)
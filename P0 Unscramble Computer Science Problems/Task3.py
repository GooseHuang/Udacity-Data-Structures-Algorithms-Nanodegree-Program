import csv
import re
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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def find_area(number):
	if "(" in number:
		code = re.findall('\((.*?)\)',number)[0]
		code = "(" + code +")"
	elif " " in number and number[0] in ('7','8','9'):
		code = number[:4]
	elif number[:3] == "140":
		code = "140"
	else:
		code = None
	return code

# Part A:

phone_number_list = []
for call in calls:
	if find_area(call[0]) == "(080)":
		phone_number_list.append(find_area(call[1]))

phone_number_list = sorted(list(set(phone_number_list)))

print("The numbers called by people in Bangalore have codes: ")
for phone_number in phone_number_list:
	print(phone_number)

# Part B: 
calls_from_bangalore = 0
answer_from_bangalore = 0
for call in calls:
	if "(" in call[0]:
		code = find_area(call[0])
		if code == "(080)":
			calls_from_bangalore += 1
			if "(" in call[1]:
				code = find_area(call[1])
				if code =="(080)":
					answer_from_bangalore += 1

if calls_from_bangalore != 0:
	percentage = answer_from_bangalore/float(calls_from_bangalore)*100
else:
	percentage = 0


print("{:.2f} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(percentage)) 


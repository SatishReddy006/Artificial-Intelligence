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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
texts_sent = set([text[0] for text in texts])
texts_received = set([text[1] for text in texts])

calls_sent = set([call[0] for call in calls])
calls_received = set([call[1] for call in calls])

#then union these sets
unique_telephone_numbers = texts_sent.union(texts_received).union(calls_sent).union(calls_received)

print("There are "+ str(len(unique_telephone_numbers)) + " different telephone numbers in the records.")
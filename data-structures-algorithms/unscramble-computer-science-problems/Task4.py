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

callers = set([call[0] for call in calls])
call_receivers = [call[1] for call in calls]
text_senders = [text[0] for text in texts]
text_receivers = [text[1] for text in texts]
tele_marketers = []
for caller in callers:
    if (caller not in call_receivers and caller not in text_senders and caller not in text_receivers):
        tele_marketers.append(caller)

tele_marketers_sorted=sorted(set(tele_marketers))
print("These numbers could be telemarketers:")
for tele_marketer in tele_marketers_sorted:
    print(tele_marketer)
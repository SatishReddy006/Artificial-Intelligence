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
index=0
max_time=0
callers_map={}
for call in calls:
    callers_map[call[0]]=callers_map.get(call[0],0)+ int(call[3])
    callers_map[call[1]]=callers_map.get(call[1],0)+ int(call[3])
Keymax = max(callers_map, key= lambda x: callers_map[x])
Valuemax=callers_map.get(Keymax)
print(Keymax +" spent the longest time, "+str(Valuemax)+" seconds, on the phone during September 2016.")
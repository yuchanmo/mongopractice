#!/usr/bin/env python

from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client.ds2
enron = db.emails

raw_input = sys.argv[1]

#fill in the blank


print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
for item in result:
    print('{}\t{}\t{}\t{}'.format(
        item['sender'].rjust(16)[:16],
        item['subject'].rjust(16)[:16],
        item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
        item['date'].rjust(16)[:16]
    ))

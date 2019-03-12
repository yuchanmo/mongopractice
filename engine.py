#!/usr/bin/env python

from pymongo import MongoClient, TEXT
from pprint import pprint
import sys

client = MongoClient()
db = client['ds2']
enron = db['emails']

raw_input = sys.argv[1]

def convertedkeywordvalue(val):
    if val.find(','):
        ck = dict()
        ck['$in'] = list(map(lambda x:x.strip(),val.split(',')))
        return ck
    else:
        return ck.strip()


def createqueryandsortcondition(searchkeyword):
    query =dict()   
    sortoption =[]     
    splitted_keyword = searchkeyword.split('/')
    for sk in splitted_keyword:
        if sk.find(':')<0:            
            query['$text']={'$search' : sk.replace(',',' '),'$caseSensitive':False,'$language':'en'}        
        if sk.find(':')>=0:
            option,keyword = list(map(lambda x : x.strip(), sk.split(':')))            
            if option =='from':
                query['sender'] = convertedkeywordvalue(keyword)
            elif option =='to':
                query['to'] = convertedkeywordvalue(keyword)
            elif option =='not':
                if '$text' not in query.keys():
                    query['$text']={'$caseSensitive':False,'$language':'en','$search':''}
                for k in keyword.split(','):
                    query['$text']['$search']=query['$text']['$search']+'-'+k.strip()
            else:
                if keyword.strip()=='score':
                    sortoption.extend(['score',{'$meta': 'textScore'}])
                else:
                    sortoption.extend(['date',-1])
    return query,sortoption


def searchfromemail(searchkeyword):
    # options={'not':'','from':'sender','to':'to','sort':''}
    query,sortoption = createqueryandsortcondition(searchkeyword)
    result = enron.find(query)
    if len(sortoption)!=0:
        result = result.sort(*sortoption)
    print('sender\t\t\tsubject\t\t\ttext\t\t\t\t\tdate')
    for item in result:
        print('{}\t{}\t{}\t{}'.format(
            item['sender'].rjust(16)[:16],
            item['subject'].rjust(16)[:16],
            item['text'].replace('\n', '').replace('\t', ' ').rjust(36)[:36],
            item['date'].rjust(16)[:16]
        ))

#

#fill in the blank
existing_indexes = enron.index_information()
if 'subject_text_text_text' not in existing_indexes.keys():
    enron.create_index([('subject',TEXT),('text',TEXT)],weights={'subject':2,'text':1})

searchfromemail(raw_input)

if __name__ !='__main__':
    test_inputs=['Social / not: Network / sort: date','from: robyn@layfam.com','to: cindy.olson@enron.com, greg.whalley@enron.com / Please / not: Attached, previously']
    for i in test_inputs:
        print('keword : ',i)
        searchfromemail(raw_input)
    




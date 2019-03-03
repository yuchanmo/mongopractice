from pymongo import MongoClient
import sys
from pprint import pprint
from collections import OrderedDict
from bisect import bisect #for function 'letter' implementation


client = MongoClient()
db = client.ds2
gradecollection = db.grades
cursor = gradecollection.find()
result = []
letters ='FDCBA'
cutline = [60,70,80,90]
percentageoftype = {'quiz':0.2,'homework':0.3,'exam':0.5}


for row in cursor:
    t_dict = OrderedDict()
    total = 0
    for grade in row['grades']:        
        typeofgrade = grade['type']
        scoreofgrade = grade['score']               
        total += scoreofgrade*percentageoftype[typeofgrade]
    total = round(total,1)
    t_dict['letter'] = letters[bisect(cutline,total)]
    t_dict['sid'] = row['sid']
    t_dict['total'] = total
    result.append(t_dict)

result.sort(key=lambda x : x['total'],reverse=True)
for doc in result:
    print(dict(sorted(doc.items())))  
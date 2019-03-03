from pymongo import MongoClient
import sys
from pprint import pprint
from collections import OrderedDict
from bisect import bisect #for function 'letter' implementation

def pagination(collection,pageNum=1):
#problem A
    numberoflineperpage = 10
    skiplines = (pageNum -1)*numberoflineperpage
    result = collection.find({},{'grades':1,'sid':1,'_id':0}).skip(skiplines).limit(numberoflineperpage)            
    for doc in result:
        print(dict(doc.items()))

def letter(collection):
#problem B
    result = []
    letters ='FDCBA'
    cutline = [60,70,80,90]
    percentageoftype = {'quiz':0.2,'homework':0.3,'exam':0.5}
    cursor = collection.find()
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
        print(dict(doc.items()))   

def perfect(collection):
#problem C

    for doc in result:
        print(dict(sorted(doc.items())))

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2
    gradecollection = db.grades

    raw_input = str(sys.argv[1])
    if raw_input == '1':
        pagination(gradecollection, int(sys.argv[2]))
    elif raw_input == '2':
        letter(gradecollection)
    else:
        perfect(gradecollection)
     

    client.close()

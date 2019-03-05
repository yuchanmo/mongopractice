from pymongo import MongoClient
import sys
from pprint import pprint
from collections import OrderedDict
from bisect import bisect #for function 'letter' implementation


letters ='FDCBA'
percentageoftype = {'quiz':0.2,'homework':0.3,'exam':0.5}

def pagination(db,pageNum=1):
#problem A
    collection =db.grades
    numberoflineperpage = 10
    skiplines = (pageNum -1)*numberoflineperpage
    result = collection.find({},{'grades':1,'sid':1,'_id':0}).skip(skiplines).limit(numberoflineperpage).sort('sid',1)            
    for doc in result:
        print(dict(doc.items()))

def gettotal(row,checkplus=False):
    total = 0
    for grade in row['grades']:        
        typeofgrade = grade['type']
        scoreofgrade = grade['score']               
        total += scoreofgrade*percentageoftype[typeofgrade]
    if checkplus:
        scorelist = list(map(lambda x : x['score'], row['grades']))
        keylist = row.keys()
        if (100 in scorelist) or ('note' in keylist):
            total += 10
    total = round(total,1)
    return total

def letter(db):
#problem B
    collection =db.grades
    result = []    
    cursor = collection.find()
    for row in cursor:
        t_dict = OrderedDict()
        total = gettotal(row)        
        cutline = [60,70,80,90]
        t_dict['letter'] = letters[bisect(cutline,total)]
        t_dict['sid'] = row['sid']
        t_dict['total'] = total
        result.append(t_dict)

    result.sort(key=lambda x : x['total'],reverse=True)
    for doc in result:
        print(dict(doc.items()))   

def perfect(db):
#problem C
    if 'relative' in db.list_collection_names():
        db.drop_collection('relative')
    
    db.create_collection('relative')
    collection =db.grades            
    cursor = collection.find()
    relativeresultlist = []
    for row in cursor:
        t_dict = OrderedDict()
        total =  gettotal(row,True)        
        t_dict['sid'] = row['sid']
        t_dict['total'] = total
        relativeresultlist.append(t_dict)
    
    #letter 
    totallist = list(map(lambda x : x['total'],relativeresultlist))
    print(totallist)
    totalmin = min(totallist)
    totalmax = max(totallist)
    cutline = [10,20,50,80]
    for t in relativeresultlist:
        x = round((t['total'] - totalmin)/(totalmax-totalmin)*100,1)
        t['letter'] = letters[bisect(cutline,x)]
        db.relative.insert_one(t)

    result = db.relative.find({},{'_id':0,'total':0})
    for doc in result:
        print(dict((doc.items())))

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2
    raw_input = str(sys.argv[1])
    if raw_input == '1':
        pagination(db, int(sys.argv[2]))
    elif raw_input == '2':
        letter(db)
    else:
        perfect(db)
     

    client.close()

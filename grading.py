from pymongo import MongoClient
import sys

def pagination():
#problem A

    for doc in result:
        print(dict(sorted(doc.items())))

def letter():
#problem B

    for doc in result:
        print(dict(sorted(doc.items())))    

def perfect():
#problem C

    for doc in result:
        print(dict(sorted(doc.items())))

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2

    raw_input = sys.argv[1]
    #TODO  

    client.close()

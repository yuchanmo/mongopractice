from pymongo import MongoClient
from pprint import pprint
from collections import Counter


client = MongoClient()
db = client.ds2
pk = db.pokedex
wind_weak = []
wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']
wind = pk.find({'name':{'$in':wind_pokemon}})

weaklist = []

for i in wind:
    weaklist.extend(i['weaknesses'])

cnt = Counter(weaklist)        
intersect_pokemon = map(lambda x:x[0], filter(lambda v : v[1] == len(wind_pokemon),cnt.items()))

inter = weaklist[0].intersection(weaklist[1])


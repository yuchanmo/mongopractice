from pymongo import MongoClient
from pprint import pprint
from collections import Counter
from datetime import date
import re


client = MongoClient()
db = client.ds2
pk = db.pokedex
wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']
wind = pk.find({'name':{'$in':wind_pokemon}})
weaklist = []
for i in wind:
    weaklist.extend(i['weaknesses'])

cnt = Counter(weaklist)        
intersect_pokemon = list(map(lambda x:x[0], filter(lambda v : v[1] == len(wind_pokemon),cnt.items())))
result = pk.find({'$and': [{'spawn_time': {'$regex': '^2[0-3]:..'}},{'type':{'$in':intersect_pokemon}}]},{'id':1,'name':1,'spawn_time':1,'type':1})
for doc in result:
    print( dict(sorted(doc.items())))


final_pokemons = pk.find({'$and':[{'next_evolution':{'$exists':False}},{'prev_evolution':{'$exists':True}}]}).sort('id',1)


for pokemon in final_pokemons:
    candy, count = "", 0    
    prev_evolutions = pokemon['prev_evolution']
    candy = pokemon['candy']
    for prev in prev_evolutions:
        p = dict(pk.find_one({'num':prev['num']}))
        if 'candy_count' in p.keys():
            count += int(p['candy_count'])
    print(pokemon['name'], end=' => ')
    print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))

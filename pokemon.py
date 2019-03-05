import sys
import re
from pymongo import MongoClient


def problem_1(pokedex):
    from collections import Counter    
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']    
    wind = pokedex.find({'name':{'$in':wind_pokemon}})
    wind_weak = []
    for i in wind:
        wind_weak.extend(i['weaknesses'])
    cnt = Counter(wind_weak)        
    intersect_pokemon = list(map(lambda x:x[0], filter(lambda v : v[1] == len(wind_pokemon),cnt.items())))
    strong = pokedex.find({'$and': [{'spawn_time': {'$regex': '^2[0-3]:'}},{'type':{'$in':intersect_pokemon}}]},{'id':1,'name':1,'spawn_time':1,'type':1})    
    for item in strong:
        print(dict(sorted(item.items())))


def problem_2(pokedex):
    # TODO: Problem B
    final_pokemons = ...

    for pokemon in final_pokemons:
        candy, count = "", 0
        
        # TODO:

        print(pokemon['name'], end=' => ')
        print('{}: {} '.format(candy.encode('ascii', 'ignore').decode('ascii'), count))


def main(problem_type):
    client = MongoClient('127.0.0.1')
    db = client.ds2
    pokedex = db.pokedex

    if problem_type == 1:
        problem_1(pokedex)
    elif problem_type == 2:
        problem_2(pokedex)

    client.close()


if __name__ == '__main__':
    main(int(sys.argv[1]))


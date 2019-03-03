import sys
import re
from pymongo import MongoClient


def problem_1(pokedex):
    wind_weak = []
    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']

    # TODO: Problem A
    strong = ...

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


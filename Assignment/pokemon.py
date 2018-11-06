import sys
import re
from pymongo import MongoClient
from pprint import pprint


def problem_a():
    # Problem A

    wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']
    # TODO: Problem A

    string = ...

    for item in strong:
        pprint(item)


def problem_b():
    # Problem B
    # TODO: Problem B
    final_pokemons = ...

    for pokemon in final_pokemons:
        candy, count = "", 0
        // TODO:
        print('{} => {}: {}'.format(pokemon['name'], candy, count))


if __name__ == '__main__':
    client = MongoClient()
    db = client.ds2
    pokedex = db.pokedex

    raw_input = sys.argv[1]

    # TODO: process argument

    client.close()

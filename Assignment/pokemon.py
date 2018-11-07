import sys
import re
from pymongo import MongoClient
from pprint import pprint


def problem_a():
	# Problem A

	wind_pokemon = ['Scyther', 'Vileplume', 'Butterfree']
	# TODO: Problem A

	#
	result = pokedex.find({"name" : {"$in" : wind_pokemon}}, {"weaknesses":True, "name":True, "_id":False})
	weaknesses_intersect = []

	# find weaknesses in common
	for Mon_Info in result:
		if weaknesses_intersect == [] :
			weaknesses_intersect = set(Mon_Info["weaknesses"])
		else:
			weaknesses_intersect = weaknesses_intersect &  set(Mon_Info["weaknesses"])
		
	weaknesses_intersect = list(weaknesses_intersect)
	strong = pokedex.find( { "$and" :
		[{"spawn_time" : {"$gte" : "20:00", "$lte" : "24:00"}}, 
		{"type" : {"$in" : weaknesses_intersect}}
		]
		}, 
		{"id" :True, "name":True, "spawn_time" : True, "type" : True, "_id":False}).sort([("name", 1)])

	#for item in result :
	#	print(item)

	for item in strong:
		pprint(item)


def problem_b():
    # Problem B
    # TODO: Problem B
    #final_pokemons = ...

	result = pokedex.find({"$and" : [{"next_evolution" :{"$exists" : False}}, {"prev_evolution" :{"$exists" : True}}]}, {"id" : True, "name": True, "candy" : True, "prev_evolution" : True,  "_id" :False}).sort([("id", 1)])
	#print(len(list(result)))
	#pprint(list(result))


	for Mon_info in result:
		#print(Mon_info)
		FinalMon_Name = Mon_info["name"]
		Candy_Name = Mon_info["candy"]
		PreMon_Id = []
		for PreMon in Mon_info["prev_evolution"] :
			PreMon_Id.append(int(PreMon["num"]))
			#print(PreMon_Id)

		Candy_result = pokedex.find({"id" : {"$in" : PreMon_Id}}, {"id" : True, "name" : True, "candy_count": True, "candy" : True, "_id" : False})
		Candy_total = 0
		for Candy_Info in Candy_result:
			Candy_total += int(Candy_Info["candy_count"])

		print('{} => {}: {}'.format(FinalMon_Name, Candy_Name, Candy_total))

#    for pokemon in final_pokemons:
#        candy, count = "", 0
#        #// TODO:
#        print('{} => {}: {}'.format(pokemon['name'], candy, count))


if __name__ == '__main__':
    client = MongoClient()
    db = client.ds2
    pokedex = db.pokedex

    raw_input = sys.argv[1]

    # TODO: process argument
    if raw_input == "1" :
        problem_a()
    else:
        problem_b()

    client.close()

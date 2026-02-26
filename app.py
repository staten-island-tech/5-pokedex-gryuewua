import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
'print(data[0])'

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
'''for i in data: 
    print(i['name'])'''

# Add a language choice feature and print the pokemons name based on the user input
'''language = (input("Select a language: ")).lower()

for i in data: 
    print(i['name'][language])'''

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
typeslalala = open("./types.json", encoding="utf8")
types = json.load(typeslalala)

language = (input("Select a language: ")).lower()
typeinput = input("Select a type: ")

for t in types: 
    if types[1] == typeinput:
        print(t['name'][language]) and print(t['type'])

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type


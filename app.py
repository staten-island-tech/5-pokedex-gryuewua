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
""" def lang(z):
    for i in data: 
        print(i['name'][z])

lang('english') """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
language = (input("Select a language: ")).lower()
input = input("Select a type: ")
typeinput = input.capitalize()
found = []
none = 0

for i in data:
    try:
        for x in i['type']:
            if i['type'][0] == typeinput: 
                found.append(i['name'][language])
                if (i['type'][0] == typeinput) == False:
                    if i['type'][1] == typeinput: 
                        found.append(i['name'][language])               
    except IndexError:
        none + 1

if none == 0:
    print(found)
else:
    print(f"No {typeinput} Pokemon were found.")

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

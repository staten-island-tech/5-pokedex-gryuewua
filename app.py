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
""" language = (input("Select a language: ")).lower()
input = input("Select a type: ")
typeinput = input.capitalize()
found = []

for i in data:
    if typeinput in i['type']:
        found.append(i['name'][language])
    else:
        "idk"

if len(found) == 0:
    print(f"No {typeinput} Pokemon were found.")
else: 
    print(found) """

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def find_pokemon(search,language):
    characters = list(search)
    found2 = []
    match = 0
    l = 0 
    for i in data:
        for c in characters: 
                if c == i['name'][language][l]:
                    match += 1
                    l += 1
                else:
                    l = 0
                    match = 0
                if match == len(characters):
                    print (i['name'][language])
                    found2.append(i['name'][language])
                    l = 0
                    match = 0
    if len(found2) == 0:
         print(f"No Pokemon matched your search: {search}")

                    
find_pokemon("Char","english")

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

""" Check for every pokemon:
     for "c"th letter of input:
        if "c"th letter of input = "c"th letter of pokemon name:
            match + 1
            if match = amount of letters in input:
                print name """
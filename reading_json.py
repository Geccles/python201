import json

# a string of data
c3po = '''{"name": "C-3PO", "height": "167", "mass": "75", "hair_color": "n/a", "skin_color": "gold", "eye_color": "yellow", "birth_year": "112BBY", "gender": "n/a", "homeworld": "https://swapi.dev/api/planets/1/", "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/", "https://swapi.dev/api/films/3/", "https://swapi.dev/api/films/4/", "https://swapi.dev/api/films/5/", "https://swapi.dev/api/films/6/"], "species": ["https://swapi.dev/api/species/2/"], "vehicles": [], "starships": [], "created": "2014-12-10T15:10:51.357000Z", "edited": "2014-12-20T21:17:50.309000Z", "url": "https://swapi.dev/api/people/2/"}'''

c3po = json.loads(c3po) # transform it to a dictionary

print(c3po['name']) # print out name to confirm it's a dictionary
print(type(c3po)) # print out type to know it's <class 'dict'>

c3po['name'] = "Galina Nosti" # set name to Galina Nosti
c3po_str = json.dumps(c3po) # update json with new name
print(c3po['name']) # new name should print here

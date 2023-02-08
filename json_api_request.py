import requests

req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(person)
print(f"Name is\t\t{person['name']}")
print(f"Birth year is\t{person['birth_year']}")

for film in person['films']:
    filmReq = requests.get(film)
    film = filmReq.json()
    print(f"Film is: {film['title']}")

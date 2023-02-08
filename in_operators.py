names = ["John", "Galina", "Tom"]
userChoice = "rock"
options = ["rock", "paper", "scissors"]

for name in names:
    if "Galina" == name:
        print("This is the name")

if userChoice in options:
    print("That option is available")
else:
    print("Please choose a valid options")

lookupKey = "birthMonth"
person = {
    "name": "Galina",
    "gender": "female",
    "birthMonth": "January"
}

if lookupKey in person:
    print(f"There is valid key of {lookupKey} in {person}")

names = [("name", "Galina"), ("occupation", "coder")]
d = {}

for key, value in names:
    d[key] = value
print(d) # turns a list to a dictionary

d = {k:v for k,v in names} # short hand to make dictionary
print(d)

d = dict(names) # even shorter to create a dictionary!!
print(d)

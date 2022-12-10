import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y["name"])
json.dumps(x, indent=4)

import json

a={"lalalala": 3}
mystring = json.dumps(a)
print(mystring)
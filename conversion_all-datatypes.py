import json

x_person = {
    "name": "het",
    "age": 19,
    "married": True,
    "divorced": False,
    "children": ("trishul", "rudra"),
    "pets": None,
    "cars": [
        {"company": "BMW", "model": "BMW 230"},
        {"company": "Mahindra", "model": "Thar"}
    ]
}

# x_person_json = json.dumps(x_person, indent=2)
# x_person_json = json.dumps(x_person, indent=2, separators=(". ", ' = '))
# x_person_json = json.dumps(x_person, indent=2, sort_keys=True)
x_person_json = json.dumps(x_person)

print(x_person_json)

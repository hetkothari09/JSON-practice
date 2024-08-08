import json

person_dict = {
    "name": "het",
    "age": 19,
    "gender": "male"
}

person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))

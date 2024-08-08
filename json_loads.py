import json

# json object
# difference between json and dict is : json contains only str whereas dict contains any hashable object
# also dict doesn't allow repetition of items whereas json allows
person_json = ('{"name": "het",'
        '"age": 19,'
        '"gender": "male"}')

# converts json object into python
person_dict = json.loads(person_json)
print(person_dict)
print(type(person_dict))

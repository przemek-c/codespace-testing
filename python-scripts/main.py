import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)


# Create a custom object
person = Person("Ashutosh Krishna", 23)

# Encode the custom object using the custom encoder
json_str = json.dumps(person, cls=PersonEncoder)

# Print the encoded JSON string
print(json_str)

# Write data to a JSON file
with open('output.json', 'w') as f:
    json.dump(json_str, f)
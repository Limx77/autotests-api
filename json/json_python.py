import json
from shlex import split

json_data = """{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing"],
  "adress": {
    "city": "Москва",
    "zip": "100110",
    "point": {"name": "Иван"}
  }
}
"""
parsed = json.loads(json_data)
print(parsed["name"] , type(parsed), sep="\n")


data = {
    "name": "Ivan",
    "age": 30,
    "is_student": True,
}
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string), sep="\n")


with open("json_example.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)
    print(data2, type(data2), sep="\n")

with open("json_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
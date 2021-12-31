import json

with open('C:/Users/smile/Desktop/3학년 2학기 겨울계절/실습/JSON/example.json') as json_file:
    json_data = json.load(json_file)

json_string = json_data["cars"]
print(json_string)

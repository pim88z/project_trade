import json

# Import api_key. (improve)
with open('./api_key/api_key.json') as json_file:
     api_key = json.load(json_file)["api_key"]

print(api_key)
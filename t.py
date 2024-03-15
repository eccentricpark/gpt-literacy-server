import json
def read_json_file(file='./prompt.json'):
    with open(file, "r", encoding='UTF8') as f:
        data = json.load(f)      
    return data

x = read_json_file()
x = dict(x)
print(x)

import json


with open("test.json","r",encoding="UTF-8") as fp:
    data = json.load(fp)
print(data[0]["name"],data[0]["age"])
print(data[1]["name"],data[1]["age"])

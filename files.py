import json


f = open("C:\Test/new.json")
try:
    res = json.load(f)
except json.decoder.JSONDecodeError as ex:
    print(ex)
    res = {}
finally:
    f.close()

print(res)
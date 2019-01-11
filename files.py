import json


with open("C:\Test/new.json") as f:
    try:
        res = json.load(f)
    except json.decoder.JSONDecodeError as ex:
        print(ex)
        res = {}
#finally убираем, файл сам себя закроет автоматически, with - означает объект будет использоваться только в рамках этого блока
print(res)
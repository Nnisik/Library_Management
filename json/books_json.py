import json

def openJson():
    with open('books.json', 'r') as f:
        json_object = json.loads(f.read())
    
    print(json_object["1"][0]['title'])
    return    


openJson()
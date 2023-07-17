import json

def create_table(title, description, image):
    f = open('db.json', 'r+')
    dict = {
        'title':title,
        'description':description,
        'image':image,
    }
    try:
        test = eval(f.read())
        test.append(dict)
        f.write(test)
    except:
        full_dict = []
        full_dict.append(dict)
        full_dict = json.dumps(full_dict)
        f.write(full_dict)
    
import json

datas = {
    'John': [2, 4, 3, 4.5, 5],
    'Adams': [4, 5, 4.5, 4, 4.5],
    'Tocker': [3, 2, 3, 3.5, 2.5],
    'Smith': [5, 4.5, 5, 5, 4.5],
    'Taylor': [4, 5, 5, 5, 5]
    }

with open('data.json', 'w') as f:
    f.write(json.dumps(datas, indent=4))

import json

with open('.clabot') as f:
    data = json.load(f)

data['contributors'].sort(key=lambda x: x.lower())

with open('.clabot', 'w') as f:
    json.dump(data, f, indent=2)


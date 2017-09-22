import redis
import json

f = open('artist.json', 'r')

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


for row in f:
    data = json.loads(row)

    if 'area' in data.keys():
        r.set(data['name'], data['area'])
        #print(data['name'], data['area'])
    else:
        r.set(data['name'], 'nothing')
        #print(data['name'])
f.close()

print(r.keys())



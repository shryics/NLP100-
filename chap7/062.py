import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

keys = r.keys()
vals = r.mget(keys)
count = 0
all_count = 0
for i in range(len(vals)):
    if vals[i] is not None:
        if vals[i].decode('utf-8') == 'Japan':
            count = count + 1
    all_count = all_count + 1
print('the number of the artists in Japan is ' + str(count) + '/' + str(all_count))



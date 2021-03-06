https://api.github.com/users/willianresille/repos

# json
import json
json_str = '{"chave3": 3, "chave4": 4}'
json_dict = json.loads(json_str)

# fazer request
from urllib import request, parse
import json

req = request.Request('url', headers={})
with request.urlopen(req) as response:
    resp = response.read()
conteudo = json.loads(resp)

# csv
import csv

l = [['1', 'jenkins'], [2, 'docker']]
with open('/tmp/a.csv', 'w') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerows(l)

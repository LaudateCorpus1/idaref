import sqlite3
import json
import re
from collections import OrderedDict

conn = sqlite3.connect("x86-64.db3")
c = conn.cursor()

def processDescription(description):
    return description

briefdata = []
with open('x86') as f:
    for line in f.readlines():
        m = re.search("([^=]+)=(.+)", line)
        briefdata.append({'mnem': m.group(1), 'description': m.group(2)})
briefdata.sort(key=lambda x: x['mnem'])

data = []
for (mnem, description) in c.execute("SELECT mnem,description FROM instructions"):
    data.append({'mnem': mnem, 'description': processDescription(description)})
data.sort(key=lambda x: x['mnem'])

result = {}
result['__license_x86-64'] = 'GPLv2'
result['__github_x86-64'] = 'https://github.com/nologic/idaref/blob/master/x86-64.sql'
result['x86-64'] = data
result['_license_x86-64-brief'] = 'GPLv3'
result['_github_x86-64-brief'] = 'https://github.com/radare/radare2/blob/master/libr/asm/d/x86'
result['x86-64-brief'] = briefdata

print(json.dumps(result, indent=2, sort_keys=True))
#!python
import json
import argparse

parser = argparse.ArgumentParser(description='Convert logs into JSON format')
parser.add_argument("--filename", help="Location of the file to be converted.")
args = parser.parse_args()
filename = args.filename

def excludelines(startwith, data):
    data = [x for x in data if not x.startswith(startwith)]
    return data
data = open('/Users/ahmedhagag/customer/05612142/k10logs/services/executor-svc-6bfbb98df6-846p6.txt').readlines()
#print(data)
for x in data:
    if x == '\n':
        data.remove(x)
if data[0].startswith('Logs for container'):
    del data[0]
if data[-1].startswith('Logs for container'):
    del data[-1]

#print(data[1])

data = excludelines('I0807', data)
data = excludelines('Log message dropped', data)
data = excludelines('Logs for container', data)
data = excludelines('I0807', data)
data = excludelines('I0813', data)
data = excludelines('I08', data)
data = excludelines('I09', data)
data = [x for x in data if not 'Fluentbit connection error' in x]

"""x = data[2]
res = x
res = json.loads(res)
print(type(res))
print(json.dumps(res, indent=4))"""


for x in data:
    res = x
    print(res)
    res = json.loads(res)
    #convert_json2 = json.dumps(res, indent=4)
    #print(convert_json2)
    print(data.index(x))

"""    with open(filename + '-jsonformat.txt', 'a') as f:
        f.write(convert_json2)
        f.close()"""

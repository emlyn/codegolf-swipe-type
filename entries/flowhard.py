import requests
import json
import sys

input = sys.argv[1] if len(sys.argv) > 1 else raw_input()

r = requests.get(
'http://flowhard-lb-493371810.eu-west-1.elb.amazonaws.com/predict' +
'?api_key=flowhard&json=' +
json.dumps({
"context": "^",
"input": list(input),
"n": 1,
"lm-code": "en_US"}
)
)
r = json.loads(r.content)['predictions']
print r[0]['term'] if len(r) > 0 else ""

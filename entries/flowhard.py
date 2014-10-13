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

terms = [p['term'].encode('utf8') for p in json.loads(r.content)['predictions']];
for t in terms:
  if t[0]+t[-1] == input[0]+input[-1]:
    print t
    break
else:
  print terms[0] if len(terms) > 0 else ""

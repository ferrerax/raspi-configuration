from flask import Flask
from flask import request
import sys
import json

app = Flask(__name__)

@app.route('/retrieve')
def code():
  if request.args.get('error'):
    print("error " + request.args.get('error'))
    sys.exit(1);
  tokens = {}
  if request.args.get('code'):
    tokens['auth_code'] = request.args.get('code')
  with open('tokens.json', 'w') as f:
    json.dump(tokens, f)
  return "Done, please close firefox for correct performace", sys.exit(0)

if __name__ == '__main__':
  app.run()

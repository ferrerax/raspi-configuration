from flask import Flask
import sys
import json

app = Flask(__name__)


@app.route('/retrieve_code')
def code():
    if request.args.get('error'):
	    sys.exit(1);
    tokens = {}
    tokens['auth_code'] = request.args.get('code')
    with open('tokens.json', 'w') as f:
	json.dump(tokens, f)
    sys.exit(0)
	

if __name__ == '__main__':
    app.run()


from flask import Flask
import scrap
import json

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home_page():
    return 'welcome to the best API'


@app.route('/locality=<local>/domain=<domain>/')
def search(local, domain):
    df = scrap.scrap_api(domain, local)
    result = df.to_json(orient='split')
    parse = json.loads(result)
    test = json.dumps(parse, indent=4)
    open('data.json', 'w').write(str(test))
    return str(test)


app.run(host='127.0.0.1', port=5000)
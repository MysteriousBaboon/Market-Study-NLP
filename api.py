from flask import Flask, request, escape
import scrap

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home_page():
  return 'welcome'

@app.route('/locality=<local>/domain=<domain>/')
def search(local, domain):
    print(scrap.scrap_api(domain, local))
    return local + domain

search('paris', 'sports')

app.run(host='127.0.0.1', port=5000)
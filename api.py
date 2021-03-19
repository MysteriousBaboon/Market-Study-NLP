from flask import Flask, jsonify
import scrap
import NLP
import pandas as pd
import utils

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/p')
def home_page():
    return "Bienvenue sur la meilleur API du monde !!!!!!!!!!!!" \
           "!!!" \
           "" \
           "!!" \
           "!\n\n\n!!"


@app.route('/locality=<local>/domain=<domain>/')
def search(local, domain):

    scrap_df = scrap.scrap_api(domain, local)
    treated_df = NLP.predict(scrap_df)
    treated_df["note"] = treated_df["note"].astype(int)
    pos_recent = utils.remove_stop(treated_df[(treated_df["note"] > 3) & (treated_df["date"] != "too far")] )
    print(pos_recent)
    no_reviews = int(treated_df['review'].count())
    no_companies = int(treated_df['company'].nunique())

    return jsonify(
            wordcloud=
                    {'recent':
                        {
                        'pos':3,
                        'neg':6
                        },
                    'old':
                        {
                        'pos':0,
                        'neg':4,
                        }
                    },
            no_reviews=no_reviews,
            no_companies=no_companies
                   )


app.run(host='127.0.0.1', port=5000)
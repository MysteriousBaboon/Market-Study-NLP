from flask import Flask, jsonify
import scrap
import json
import NLP

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home_page():
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
            no_reviews=0,
            no_companies=1,
                    )


@app.route('/locality=<local>/domain=<domain>/')
def search(local, domain):

    scrap_df = scrap.scrap_api(domain, local)
    treated_df = NLP.predict(scrap_df)

    # df_recent = treated_df[treated_df[date]]

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
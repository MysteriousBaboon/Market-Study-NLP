from flask import Flask, jsonify, render_template

import scrap
import NLP
import utils

app = Flask(__name__)
# app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/p')
def home_page():
    return "Welcome to a NLP Sentiment analysis API. Look at the README to learn how to use it."


@app.route('/locality=<local>/category=<domain>/')
def search(local, domain):

    scrap_df = scrap.scrap_api(domain, local)
    treated_df = NLP.predict(scrap_df)
    treated_df["note"] = treated_df["note"].astype(int)
    pos_recent = utils.remove_stop(treated_df[(treated_df["note"] > 3) & (treated_df["date"] != "too far")])
    neg_recent = utils.remove_stop(treated_df[(treated_df["note"] <= 3) & (treated_df["date"] != "too far")])
    pos_old = utils.remove_stop(treated_df[(treated_df["note"] > 3) & (treated_df["date"] == "too far")])
    neg_old = utils.remove_stop(treated_df[(treated_df["note"] <= 3) & (treated_df["date"] == "too far")])

    no_reviews = int(treated_df['review'].count())
    no_companies = int(treated_df['company'].nunique())

    json = jsonify(
            wordcloud=
                    {'recent':
                        {
                        'pos':pos_recent,
                        'neg':neg_recent
                        },
                    'old':
                        {
                        'pos':pos_old,
                        'neg':neg_old,
                        }
                    },
            no_reviews=no_reviews,
            no_companies=no_companies
                   )

    return render_template("dashboard.html", json=json)
# noms des entreprises qui ont le plus de reviews
# treated_df['review'].tolist()


app.run(host='127.0.0.1', port=5000)
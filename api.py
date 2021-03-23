from flask import Flask, jsonify, render_template

import scrap
import NLP
import utils

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def home_page():
    return render_template("dashboard.html", wordcloud={"test": {"f": 1, "p": 4}})
    # return "Welcome to a NLP Sentiment analysis API. Look at the README to learn how to use it."


@app.route('/locality=<local>/category=<domain>/')
def search(local, domain):
    scrap_df = scrap.scrap_api(domain, local)

    treated_df = NLP.predict(scrap_df)

    pos_recent = utils.remove_stop(treated_df[(treated_df["pred"] > 3) & (treated_df["date"] != "too far")])
    neg_recent = utils.remove_stop(treated_df[(treated_df["pred"] <= 3) & (treated_df["date"] != "too far")])
    pos_old = utils.remove_stop(treated_df[(treated_df["pred"] > 3) & (treated_df["date"] == "too far")])
    neg_old = utils.remove_stop(treated_df[(treated_df["pred"] <= 3) & (treated_df["date"] == "too far")])

    no_reviews = int(treated_df['review'].count())
    no_companies = int(treated_df['company'].nunique())
    most_company = str(treated_df['company'].value_counts()[:1].keys().tolist()[0])

    wordcloud = {'recent':
                 {'pos': pos_recent, "neg": neg_recent},
                 'old':
                 {'pos': pos_old, 'neg': neg_old}}

    try:
        utils.create_wcloud(wordcloud)
        return render_template("dashboard.html", review=no_reviews,
                               company=no_companies, most_company=most_company)

    except:
        return "No reviews on this combination."

'''
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
            no_companies=no_companies,
            noms = nom
                   )
'''
app.run(host='127.0.0.1', port=5000)

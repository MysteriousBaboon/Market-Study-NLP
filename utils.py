from nltk.corpus import stopwords
from collections import Counter

french_stopwords = stopwords.words('french')
new_stop = ["très", "a", "!", "Je", "plus", "Très", "tout", "j'ai", "fait", ",", "c'est", "J'ai"]
french_stopwords.extend(new_stop)


def remove_stop(df):
    df['review'] = df['review'].fillna("")
    occ = Counter("".join(df["review"]).split()).most_common(100)
    real_occ = []

    for element in occ:
        if element[0] not in french_stopwords:
            real_occ.append(element)

    return real_occ
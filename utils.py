import nltk
from nltk.corpus import stopwords
from collections import Counter
import warnings
warnings.filterwarnings("ignore")

# Stopwords
nltk.download('stopwords')
french_stopwords = stopwords.words('french')
new_stop = ["très", "a", "!", "Je", "plus", "Très", "tout", "j'ai", "fait", ",", "c'est", "J'ai"]
french_stopwords.extend(new_stop)


def remove_stop(df):
    # Remove Nan
    df['review'] = df['review'].fillna("")

    # Counter the 100 most frequent words
    occurrence = Counter("".join(df["review"]).split()).most_common(100)
    cleaned_occurrence = []

    # Check if the word is in the stopwords list
    for word in occurrence:
        if word[0] not in french_stopwords:
            cleaned_occurrence.append(word)

    return cleaned_occurrence

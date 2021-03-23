import nltk
from nltk.corpus import stopwords
from collections import Counter
import wordcloud
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


def create_wcloud(data):
    word_occ = []
    # For each tuple (word:occurrence) multiply word by occurrence
    wordocc = [(lambda a: ((a[0] + "|") * a[1])[0:-1])(x) for x in data["recent"]["pos"]]
    # Transform the multiples list in one list
    [(lambda b: word_occ.extend(b.split("|")))(y) for y in wordocc]
    # Transform the list to a string
    text = ' '.join(word_occ)
    # Generate the Wordcloud and create an image
    cloud = wordcloud.WordCloud().generate(text)
    cloud.to_file("images/rec_pos.png")

    word_occ = []
    # For each tuple (word:occurrence) multiply word by occurrence
    wordocc = [(lambda a: ((a[0] + "|") * a[1])[0:-1])(x) for x in data["recent"]["neg"]]
    # Transform the multiples list in one list
    [(lambda b: word_occ.extend(b.split("|")))(y) for y in wordocc]
    # Transform the list to a string
    text = ' '.join(word_occ)
    # Generate the Wordcloud and create an image
    cloud = wordcloud.WordCloud().generate(text)
    cloud.to_file("images/rec_neg.png")

    word_occ = []
    # For each tuple (word:occurrence) multiply word by occurrence
    wordocc = [(lambda a: ((a[0] + "|") * a[1])[0:-1])(x) for x in data["old"]["pos"]]
    # Transform the multiples list in one list
    [(lambda b: word_occ.extend(b.split("|")))(y) for y in wordocc]
    # Transform the list to a string
    text = ' '.join(word_occ)
    # Generate the Wordcloud and create an image
    cloud = wordcloud.WordCloud().generate(text)
    cloud.to_file("images/old_pos.png")

    word_occ = []
    # For each tuple (word:occurrence) multiply word by occurrence
    wordocc = [(lambda a: ((a[0] + "|") * a[1])[0:-1])(x) for x in data["old"]["neg"]]
    # Transform the multiples list in one list
    [(lambda b: word_occ.extend(b.split("|")))(y) for y in wordocc]
    # Transform the list to a string
    text = ' '.join(word_occ)
    # Generate the Wordcloud and create an image
    cloud = wordcloud.WordCloud().generate(text)
    cloud.to_file("images/old_neg.png")




import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer


# nltk.download('punkt')  # first-time use only
# nltk.download('wordnet')

# d1 = "The quick brown fox jumps over the lazy dog"
# d2 = "The quick brown fox leaps over the lazy dog"
# documents = [d1, d2]


lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return LemTokens(nltk.word_tokenize(text.lower().
                                        translate(remove_punct_dict)))


def cos_similarity(textlist):
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()


def get_score(original, generated):
    doc = [original, generated]
    return cos_similarity(doc)[0][1]

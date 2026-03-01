from lib.search_utils import load_movies, load_stopwords
import string
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def tokenize_text(text):
    text = clean_text(text)
    stopwords = load_stopwords()
    res = []
    # tokens = [token for token in text.split() if token not in stopwords]
    
    def _filter(token):
        if token and token not in stopwords:
            return True
        return False
    for token in text.split():
        if _filter(token):
            token = stemmer.stem(token)
            res.append(token)

    return res

def has_matching_token(query_tokens, movie_tokens):
    for query_token in query_tokens:
        for movie_token in movie_tokens:
            if query_token in movie_token:
                return True
    return False

def search_command(query, n_results):
    movies = load_movies()
    res = []
    query_tokens = tokenize_text(query)
    for movie in movies:
        movie_tokens = tokenize_text(movie['title'])
        if has_matching_token(query_tokens, movie_tokens):
            res.append(movie)
        if len(res) == n_results:
            break
    return res
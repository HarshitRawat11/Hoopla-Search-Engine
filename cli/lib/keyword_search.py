from lib.search_utils import load_movies
import string

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def tokenize_text(text):
    text = clean_text(text)
    tokens = [token for token in text.split() if token]
    return tokens

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
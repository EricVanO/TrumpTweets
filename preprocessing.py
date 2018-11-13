def remove_urls(text):
    """Removes urls from a string"""
    import re
    return re.sub(r'http\S+', '', text)

def html_to_unicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    from bs4 import BeautifulSoup
    text = BeautifulSoup(text,'lxml').text
    return text

def smart_quotes_to_straight_quotes(text):
    """Replaces 'smart' quotes (like “) with straight quotes (like ")"""
    return text.replace('\u2018', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"').replace('’', "'")

def remove_punct(text):
    """Removes punctuation from a string"""
    import string
    punct_dict = dict.fromkeys(string.punctuation)
    # Instead of removing hyphens, I replace them with a space so that hypenated
    # words turn into two separate words. I also turn ampersands into the word 'and'.
    punct_dict['-'] = ' '
    punct_dict['&'] = 'and'
    return text.translate(text.maketrans(punct_dict))

def stem_text(text):
    """Stems the individual words of a string using the Porter stemming algorithm."""
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    stemmer = PorterStemmer()
    return ' '.join([stemmer.stem(token) for token in word_tokenize(text)])

def preprocess_text(text):
    """Preprocesses a string so that it can be better used for NLP."""
    text = remove_urls(text)
    text = html_to_unicode(text)
    text = smart_quotes_to_straight_quotes(text)
    text = remove_punct(text)
    text = stem_text(text)
    return text.lower()

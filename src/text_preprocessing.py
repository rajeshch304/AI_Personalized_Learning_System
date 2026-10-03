import re
import string
import nltk
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model for lemmatization
nlp = spacy.load("en_core_web_sm")

# Stopwords set
stop_words = set(stopwords.words('english'))


def clean_text(text):
    """
    Basic cleaning: lowercasing, removing noise, punctuation, numbers, etc.
    """

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def tokenize_text(text):
    """
    Convert text into tokens
    """
    return word_tokenize(text)


def remove_stopwords(tokens):
    """
    Remove common stopwords
    """
    return [word for word in tokens if word not in stop_words]


def lemmatize_tokens(tokens):
    """
    Convert words to base form using spaCy
    """
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]


def preprocess_text(text, return_string=False):
    """
    Full preprocessing pipeline
    """

    # Step 1: clean
    text = clean_text(text)

    # Step 2: tokenize
    tokens = tokenize_text(text)

    # Step 3: remove stopwords
    tokens = remove_stopwords(tokens)

    # Step 4: lemmatization
    tokens = lemmatize_tokens(tokens)

    # Return format
    if return_string:
        return " ".join(tokens)
    return tokens

import nltk
import re
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmitizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    words = nltk.word_tokenize(text)
    words = [lemmitizer.lemmatize(word) for word in words]
    return " ".join(words)

import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load the CSV data
df = pd.read_csv("new.csv")

# Text preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def preprocess_text(text):
    if isinstance(text, str):  # Check if text is a string
        # Tokenize the text
        tokens = nltk.word_tokenize(text.lower())
        return tokens
    else:
        return [] 
    
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Perform stemming
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    
    # Join the tokens back into a string
    preprocessed_text = ' '.join(stemmed_tokens)
    return preprocessed_text

df['Preprocessed_Review'] = df['Review Text'].apply(preprocess_text)

# Streamlit app
st.title("Product Reviews Analysis")

# Display the data
st.subheader("Product Reviews")
st.dataframe(df)





import pandas as pd
import nltk
from textblob import TextBlob
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import cmudict
from collections import Counter

nltk.download('punkt')
nltk.download('cmudict')

def calculate_metrics(text):
    # Tokenize the text 
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    # Calculate number of words
    word_count = len(words)
    
    # number of sentences
    sentence_count = len(sentences)
    
    # average sentence length
    avg_sentence_length = word_count / sentence_count if sentence_count != 0 else 0
    
    # number of complex words (words with more than 2 syllables)
    cmu = cmudict.dict()
    syllable_count = sum(len(cmu.get(word.lower(), [0])) for word in words)
    complex_word_count = len([word for word in words if len(cmu.get(word.lower(), [0])) > 2])
    
    # percentage of complex words
    percentage_complex_words = (complex_word_count / word_count) * 100 if word_count != 0 else 0
    
    # Calculate the Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # average number of words per sentence
    avg_words_per_sentence = word_count / sentence_count if sentence_count != 0 else 0
    
    # Count personal pronouns
    personal_pronouns = ['I', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours', 'ourselves']
    pronoun_count = sum(Counter(words)[pronoun] for pronoun in personal_pronouns)
    
    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / word_count if word_count != 0 else 0
    
    # syllables per word
    syllables_per_word = syllable_count / word_count if word_count != 0 else 0
    
    #  sentiment scores
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    # positive and negative scores
    positive_score = max(polarity_score, 0)
    negative_score = -min(polarity_score, 0)
    
    return positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, \
           percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count, \
           syllables_per_word, pronoun_count, avg_word_length

def main():
    # Read the extracted content from the text file
    with open("URL_ID.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Calculate metrics for the content
    metrics = calculate_metrics(content)
    
    df = pd.DataFrame([metrics], columns=['POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
                                          'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
                                          'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT',
                                          'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'])
    
    # Save the DataFrame to an Excel file
    df.to_excel("Output Data Structure.xlsx", index=False)

if __name__ == "__main__":
    main()

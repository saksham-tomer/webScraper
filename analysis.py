import nltk
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

# cleaning the text using stop words
def clean_text(text):
    stop_words = set(stopwords.words('english'))
    cleaned_text = ' '.join(word for word in text.split() if word.lower() not in stop_words)
    return cleaned_text

# creating dictionaries of positive and negative words
def create_word_dictionary(filename):
    word_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            word_dict[word] = 1
    return word_dict

# calculating syllable count of a word
def syllable_count(word):
    vowels = 'aeiouy'
    word = word.lower()
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        count += 1
    if count == 0:
        count += 1
    return count

# readability metrics
def calculate_readability(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    total_words = len(words)
    total_sentences = len(sentences)
    total_complex_words = sum(1 for word in words if syllable_count(word) > 2)
    avg_sentence_length = total_words / total_sentences
    percentage_complex_words = (total_complex_words / total_words) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = total_words / total_sentences
    return avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence

# personal pronouns count
def count_personal_pronouns(text):
    pronouns = re.findall(r'\b(?:I|we|my|ours|us)\b', text, flags=re.IGNORECASE)
    return len(pronouns)

# average word length
def average_word_length(text):
    words = word_tokenize(text)
    total_chars = sum(len(word) for word in words)
    avg_length = total_chars / len(words)
    return avg_length

def main():
    
    with open("URL_ID.txt", "r", encoding="utf-8") as file:
        text = file.read()

    cleaned_text = clean_text(text)

    positive_words = create_word_dictionary("MasterDictionary/PositiveWords.txt")
    negative_words = create_word_dictionary("MasterDictionary/NegativeWords.txt")

    positive_score = sum(1 for word in cleaned_text.split() if word.lower() in positive_words)
    negative_score = sum(1 for word in cleaned_text.split() if word.lower() in negative_words)
    
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    polarity_score = max(-1, min(1, polarity_score))  # Ensure polarity score falls within [-1, 1]

    # Calculate subjectivity score ensuring it falls within the range [0, 1]
    total_words = len(cleaned_text.split())
    subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)
    subjectivity_score = min(1, subjectivity_score)  # Ensure subjectivity score falls within [0, 1]

    avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence = calculate_readability(text)

    complex_word_count = sum(1 for word in cleaned_text.split() if syllable_count(word) > 2)
    word_count = len(cleaned_text.split())
    syllables_per_word = sum(syllable_count(word) for word in cleaned_text.split()) / word_count
    personal_pronouns = count_personal_pronouns(text)
    avg_word_length = average_word_length(text)

    data = {
        "Positive Score": [positive_score],
        "Negative Score": [negative_score],
        "Polarity Score": [polarity_score],
        "Subjectivity Score": [subjectivity_score],
        "Average Sentence Length": [avg_sentence_length],
        "Percentage of Complex Words": [percentage_complex_words],
        "Fog Index": [fog_index],
        "Average Number of Words Per Sentence": [avg_words_per_sentence],
        "Complex Word Count": [complex_word_count],
        "Word Count": [word_count],
        "Syllable Count Per Word": [syllables_per_word],
        "Personal Pronouns": [personal_pronouns],
        "Average Word Length": [avg_word_length]
    }

    df = pd.DataFrame(data)

    df.to_excel("OutputDataStructure.xlsx", index=False)

if __name__ == "__main__":
    main()
#
################################
# Data Analysis on Extracted Article Content

## Introduction

This project involves performing data analysis on textual content extracted from articles. The goal is to calculate various metrics such as sentiment scores, average sentence length, percentage of complex words, etc., and store the results in an Excel file.

## Approach

### Understanding the Problem

Initially, the problem statement was understood, which involves analyzing textual content extracted from articles to derive insights.

### Identifying Dependencies

The required dependencies for the task were identified:

* pandas: For data manipulation and creating DataFrames to store the calculated metrics.
* nltk: For natural language processing tasks such as tokenization, sentiment analysis, and accessing the CMU Pronouncing Dictionary for syllable counts.
* textblob: For sentiment analysis.

### Approach for Data Analysis

1. **Tokenization** : Tokenize the text into sentences and words using NLTK's `sent_tokenize` and `word_tokenize` functions.
2. **Sentiment Analysis** : Use TextBlob for sentiment analysis to calculate polarity and subjectivity scores.
3. **Complexity Metrics** :

* Calculate average sentence length, percentage of complex words, and Fog Index.
* Compute average words per sentence and syllables per word.

1. **Other Metrics** :

* Count personal pronouns and calculate average word length.

1. **Data Aggregation** : Aggregate the calculated metrics into a structured format, such as a DataFrame.
2. **Output Generation** : Store the calculated metrics in an Excel file for further analysis.

### Writing the Code

Python code was implemented to calculate the metrics using appropriate functions and orchestrate the process.

### Testing the Code

The code was tested on sample text data to ensure its correctness before running it on the actual dataset.

### Running the Code

Instructions were provided on how to run the Python script to generate the output Excel file containing the calculated metrics.

## How to Run

1. Ensure Python is installed on your system.
2. Install the required dependencies using pip:
   <pre><div class="dark bg-gray-950 rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install pandas nltk textblob
   </code></div></div></pre>
3. Download the required NLTK corpora:
   <pre><div class="dark bg-gray-950 rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">import nltk
   nltk.download('punkt')
   nltk.download('cmudict')
   </code></div></div></pre>
4. Place the provided `.py` file and the "URL_ID.txt" file (containing the extracted article content) in the same directory.
5. Run the `.py` file using the following command in the terminal or command prompt:
   <pre><div class="dark bg-gray-950 rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python filename.py
   </code></div></div></pre>
6. After running the script, you will find the output Excel file named "Output Data Structure.xlsx" containing the calculated metrics in the same directory.

## Conclusion

By employing various algorithms and techniques, valuable insights can be gained into the characteristics of the article content, including sentiment, complexity, readability, and linguistic features. These insights can inform various downstream tasks such as content evaluation, text summarization, and language style analysis.

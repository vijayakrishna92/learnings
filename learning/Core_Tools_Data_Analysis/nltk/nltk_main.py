#nltk 
# Natural Language Toolkit (NLTK) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.
#NLTK is a powerful library for natural language processing (NLP) in Python. It provides tools for tasks such as tokenization, stemming, lemmatization, part-of-speech tagging, named entity recognition, and more. NLTK is widely used in academia and industry for text analysis and NLP applications.
import nltk
'''
open terminal and run the following command 
python #Python interactive shell
import nltk
nltk.download('punkt_tab')                          # Tokenization
nltk.download('stopwords')                      # Stopword removal
nltk.download('wordnet')                        # Lemmatization & WordNet
nltk.download('omw-1.4')                        # WordNet synonyms
nltk.download('averaged_perceptron_tagger_eng')     # POS tagging
nltk.download('maxent_ne_chunker_tab')              # Named Entity Recognition
nltk.download('words')                          # NER support
nltk.download('movie_reviews')                  # Example for classification
nltk.download('names')                          # Classification support
nltk.download('treebank')                       # Parsing/Chunking examples
exit()

or run run nltk_setup.py file
'''
n1 = nltk.tokenize.word_tokenize("Hello, world!") # Tokenize the text into words
print(n1)
n2 = nltk.tokenize.sent_tokenize("Hello, world!") # Tokenize the text into sentences
print(n2)
n3 = nltk.corpus.stopwords.words('english') # Get the list of stopwords in English
print(n3)
n4 = nltk.stem.PorterStemmer() # Create a stemmer object
n5 = n4.stem("running") # Stem the word "running"
print(n5)
n6 = nltk.pos_tag(["running"]) # Part-of-speech tagging
print(n6)
n7 = nltk.ne_chunk(n6) # Named Entity Recognition
print(n7)
n8 = nltk.FreqDist(["running", "jumps", "over"]) # Frequency distribution of words
print(n8.most_common(2)) # Get the most common words
n9 = nltk.ngrams(["running", "jumps", "over"], 2) # Create bigrams
print(list(n9)) # Convert to list and print
grammar = "NP: {<DT>?<JJ>*<NN>}"
n10 = nltk.RegexpParser(grammar) # Create a parser with the defined grammar
n11 = n10.parse(n6) # Parse the tagged words
print(n11) # Print the parsed tree
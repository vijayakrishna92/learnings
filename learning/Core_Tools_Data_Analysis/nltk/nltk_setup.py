import nltk

resources = [
    'punkt_tab',                          # Tokenization
    'stopwords',                      # Stopword removal
    'wordnet',                        # Lemmatization & WordNet
    'omw-1.4',                        # WordNet synonyms
    'averaged_perceptron_tagger_eng',     # POS tagging
    'maxent_ne_chunker_tab',              # Named Entity Recognition
    'words',                          # NER support
    'movie_reviews',                  # Text classification (example)
    'names',                          # Classification support
    'treebank'                        # Parsing/Chunking examples
]

for resource in resources:
    nltk.download(resource)
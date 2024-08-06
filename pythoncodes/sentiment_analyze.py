import nltk
from nltk.corpus import movie_reviews
import random
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import string

nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = FreqDist(all_words)

word_features = list(all_words.keys())[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d, c) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]

classifier = NaiveBayesClassifier.train(train_set)

print(f"Classifier accuracy: {accuracy(classifier, test_set):.2f}")

classifier.show_most_informative_features(10)

def classify_text(text):
    tokens = preprocess_text(text)
    features = document_features(tokens)
    return classifier.classify(features)

sample_text = "I love this movie. It's fantastic!"
print(f"Sample text: '{sample_text}' is classified as {classify_text(sample_text)}")

sample_text = "This is the worst movie I've ever seen."
print(f"Sample text: '{sample_text}' is classified as {classify_text(sample_text)}")

def evaluate_model():
    positive_reviews = [preprocess_text(movie_reviews.raw(fileid)) 
                        for fileid in movie_reviews.fileids('pos')]
    negative_reviews = [preprocess_text(movie_reviews.raw(fileid)) 
                        for fileid in movie_reviews.fileids('neg')]
    
    positive_results = [classify_text(' '.join(review)) for review in positive_reviews]
    negative_results = [classify_text(' '.join(review)) for review in negative_reviews]
    
    positive_accuracy = positive_results.count('pos') / len(positive_results)
    negative_accuracy = negative_results.count('neg') / len(negative_results)
    
    overall_accuracy = (positive_accuracy + negative_accuracy) / 2
    
    print(f"Positive review accuracy: {positive_accuracy:.2f}")
    print(f"Negative review accuracy: {negative_accuracy:.2f}")
    print(f"Overall accuracy: {overall_accuracy:.2f}")

evaluate_model()
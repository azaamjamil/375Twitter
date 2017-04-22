import random
import pandas as pd
import nltk
import pickle
from nltk.corpus import twitter_samples

# http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
# https://www.digitalocean.com/community/tutorials/how-to-work-with-language-data-in-python-3-using-the-natural-language-toolkit-nltk
# http://stackoverflow.com/questions/25595334/nltk-naivebayesclassifier-is-extremely-slow-in-python

class TweetAnalyzer:
    def __init__(self, numrecords=None):
        
        print("Initializing positive tweets")
        positive_tweets = [(tweet.lower().split(), 'positive') for tweet in twitter_samples.strings('positive_tweets.json')[:numrecords]]
        
        print("Initializing negative tweets")
        negative_tweets = [(tweet.lower().split(), 'negative') for tweet in twitter_samples.strings('negative_tweets.json')[:numrecords]]
        
        print("Creating tweet set")
        tweets = positive_tweets + negative_tweets
        
        print("Analyzing word features")
        self.wordFeatures = self.getWordFeatures(self.getWordsInTweets(tweets))

            
        print("Splitting into training and testing sets")
        trainingIndex = int(len(tweets) * 0.75)
        training_set = nltk.classify.apply_features(self.extractFeatures, tweets[:trainingIndex])
        testing_set = nltk.classify.apply_features(self.extractFeatures, tweets[trainingIndex:])

        print("Creating Naive Bayes Classifier")
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)

        print("Ready for action!")
    
    def getWordsInTweets(self, tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words
    
    def getWordFeatures(self, wordlist):
        wordlist = nltk.FreqDist(wordlist)
        wf = wordlist.keys()
        return wf
    
    def extractFeatures(self, document):
        document_words = set(document)
        features = {}
        for word in self.wordFeatures:
            features['contains(%s)' % word] = (word in document_words)
        return features
    
    def loadClassifier(self):
        f = open('my_classifier.pickle', 'rb')
        classifier = pickle.load(f)
        f.close()

    def classify(self, tweet):
        features = self.extractFeatures(tweet.split())
        classification = self.classifier.classify(features)
        # accuracy = nltk.classify.util.accuracy(self.classifier, features)
        # return (classification, accuracy)
        return classification

if __name__ == '__main__':
    tw = TweetAnalyzer(2500)
    tw2 = TweetAnalyzer(load=True)
    tw2.classify("The Galaxy s8 is BLOWING UP")
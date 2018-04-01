from __future__ import division
import csv
from string import punctuation
 
positive_counts=[]
negative_counts=[]
clean_tweets=[]
 
tweets = open("/media/luqni/Data/oprekan/tugas kukuh/list.py/obama_tweets.txt").read()
tweets_list = tweets.split('\n')
 
pos_sent = open("/media/luqni/Data/oprekan/tugas kukuh/list.py/positive.txt").read()
positive_words=pos_sent.split('\n')
 
neg_sent = open("/media/luqni/Data/oprekan/tugas kukuh/list.py/Negative.txt").read()
negative_words=neg_sent.split('\n')
 
for tweet in tweets_list:
    positive_counter=0
    negative_counter=0
     
    tweet_processed=tweet.lower()
     
     
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
     
    clean_tweets.append(tweet_processed)
 
    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1
         
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)
 
 
output=zip(tweets_list,positive_counts,negative_counts,clean_tweets)
 
writer = csv.writer(open('/media/luqni/Data/oprekan/tugas kukuh/list.py/obama_tweets.txt', 'wb'))
writer.writerows(output)
# Pertama kali ada 3 module yang akan digunakan yaitu punctuation, csv dan division
from __future__ import division
import csv
from string import punctuation
# 3 list yang akan menampung jumlah kata positif, kata negatif pada setiap tweet
positive_counts=[]
negative_counts=[]
clean_tweets=[]
# membaca file txt yang ada di komputer dan tweet yang tersimpan dalam file akan dipisahkan pada setiap baris. Gunakan fungsi split 
tweets = open("/media/luqni/Data/oprekan/tugas kukuh/sentimen_analysis/obama_tweets.txt").read()
tweets_list = tweets.split('\n')
 
pos_sent = open("/media/luqni/Data/oprekan/tugas kukuh/sentimen_analysis/positive.txt").read()
positive_words=pos_sent.split('\n')
 
neg_sent = open("/media/luqni/Data/oprekan/tugas kukuh/sentimen_analysis/Negative.txt").read()
negative_words=neg_sent.split('\n')
# Lakukan proses looping agar mendapatkan tweet dari list tweets dan set positive_counter dan negative_counter dengan angka 0 dan lakukan proses shifting lowercase
for tweet in tweets_list:
    positive_counter=0
    negative_counter=0
     
    tweet_processed=tweet.lower()
     
# Kemudian hapus tanda baca dan simpan dalam clean_tweets  
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
     
    clean_tweets.append(tweet_processed)

# Lakukan proses Tokenizing yaitu proses memecah tweet yang didapat list tweets menjadi list kata. 
# Lakukan looping setiap kata pada setiap tweet apakah terdapat kata positif dan negatif jika ada maka 
# disimpan dalam counter

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1

# simpan ratio antara jumlah kata positif/negatif dibanding dengan jumlah kata pada tweet        
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)
 
# Gabungkan list tweets, list clean tweet, count positif dan count negatif menggunakan syntax zip
output=zip(tweets_list,positive_counts,negative_counts,clean_tweets)
# Simpan hasil sentiment analysis dalam bentuk CSV 
writer = csv.writer(open('/media/luqni/Data/oprekan/tugas kukuh/sentimen_analysis/Tweet_sentiment2.csv', 'wb'))
writer.writerows(output)
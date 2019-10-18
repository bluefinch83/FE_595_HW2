'''
Name: Main file for HW2 of FE 595
Intro: This file should load the cleaned data from theyfightcrime.org, sort the data, and return the required info.
Author: William Long
Date : 09/22/2019
'''

import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk

#First, Let's load the data

m_raw = pd.read_csv('Male_full.txt', names=["male"], sep='\t')
f_raw = pd.read_csv('Female_full.txt', names=["female"], sep='\t')

# We need to get the sentiment.
def char_sent(text):
    '''
    This fun should take in some text, and return the sentiment polarity using textblob
    :param text: String
    :return: sent, float
    '''
    sent = TextBlob(text).sentiment.polarity
    return sent

# Let's add the sentiment in

m_raw["sentiment"] = m_raw.apply(lambda row: char_sent(row["male"]), axis=1)
f_raw["sentiment"] = f_raw.apply(lambda row: char_sent(row["female"]), axis=1)

# Let's sort and return the values we want.
m_sort = m_raw.sort_values(by=["sentiment"])
f_sort = f_raw.sort_values(by=["sentiment"])

m_best = m_sort.tail(10)
f_best = f_sort.tail(10)
m_worst = m_sort.head(10)
f_worst = f_sort.head(10)

# Let's make a list of all the descriptors.

des = []
for i in range(len(m_raw["male"])):
    tokens = nltk.word_tokenize(m_raw["male"][i])
    tags = nltk.pos_tag(tokens)
    a = [wt[0] for wt in tags if wt[1] == 'JJ']
    des.extend(a)

for i in range(len(f_raw["female"])):
    tokens = nltk.word_tokenize(f_raw["female"][i])
    tags = nltk.pos_tag(tokens)
    a = [wt[0] for wt in tags if wt[1] == 'JJ']
    des.extend(a)

# We just need to do the last part.
word_dist = nltk.FreqDist(des)
top_words = word_dist.most_common(10)
top_words_df = pd.DataFrame(top_words, columns=["Word", "Count"])

# Save the data.
m_best.to_csv(r'Male_Best.csv',  index=None, header=True, sep=';')
f_best.to_csv(r'Female_Best.csv', index=None, header=True, sep=';')
m_worst.to_csv(r'Male_Worst.csv',  index=None, header=True, sep=';')
f_worst.to_csv(r'Female_Worst.csv', index=None, header=True, sep=';')
top_words_df.to_csv(r'Top_Words.csv', sep=';', index=None, header=True)




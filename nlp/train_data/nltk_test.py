#!/usr/bin/python3.6

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
import os

tokens = []

def ie_preprocess(document):
  sentences = sent_tokenize(document)
  sentences = [word_tokenize(sent) for sent in sentences]
  sentences = [nltk.pos_tag(sent) for sent in sentences]
  for sen in sentences:
    for i in sen:
      print(i) 

for cve in os.listdir():
  if "CVE" in cve:
    print("\nClassifying: {}\n{}".format(cve,"="*40))
    ie_preprocess(open(cve).read())
    tokens += [t.replace("\n","") for t in open(cve)]

def clean_tokens():
  clean_tokens = tokens[:]
  sr = stopwords.words('english')
  for token in tokens:
    if token in stopwords.words('english'):
      clean_tokens.remove(token)

#freq = nltk.FreqDist(tokens)
#for key,val in freq.items():
#  print(str(key) + ":" + str(val))

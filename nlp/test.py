#!/usr/bin/python3.6

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')

# Process whole documents
text_1 = (u"When Sebastian Thrun started working on self-driving cars at "
        u"Google in 2007, few people outside of the company took him "
        u"seriously. “I can tell you very senior CEOs of major American "
        u"car companies would shake my hand and turn away because I wasn’t "
        u"worth talking to,” said Thrun, now the co-founder and CEO of "
        u"online higher education startup Udacity, in an interview with "
        u"Recode earlier this week.")

text = "In CMS Made Simple (CMSMS) through 2.2.7, the 'module import' operation in the admin dashboard contains a remote code execution vulnerability, exploitable by an admin user, because an XML Package can contain  base64-encoded PHP code in a data element."
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# Determine semantic similarities
#doc1 = nlp(u"my fries were super gross")
#doc2 = nlp(u"such disgusting fries")
#similarity = doc1.similarity(doc2)
#print(doc1.text, doc2.text, similarity)

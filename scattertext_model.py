# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:19:14 2022

@author: Micha
"""

import json
import pandas as pd
# from nltk.corpus import stopwords
import gensim
import gensim.corpora as corpora
import spacy
import scattertext as st

####Stopwords alternative trial
# from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS


df = pd.read_csv("Second Party System.csv")


columns = df.columns

df = df.rename(columns={"clean text":"clean_text"})

texts = df["clean_text"]
party = df["Party"]

party.unique()

nlp = st.whitespace_nlp_with_sentences


print("Document Count")
print(df.groupby("Party")["clean_text"].count())

print("Word Count")

"""
We build a scattertext model by grouping them by Party, and then feeing the cleaned text into the model
"""

# df["parsed"] = df.clean_text.apply(nlp)

for party in df['Party'].unique():
    df['category'] = df['Party'].apply(lambda x: party if x == party else 'Other Parties')
    corpus = st.CorpusFromPandas(df, category_col= "category", text_col="clean_text").build()
    html = st.produce_scattertext_explorer(corpus,
                                           category=party,
                                           category_name=party,
                                           not_category_name='Other Parties',
                                           width_in_pixels=1000,
                                           minimum_term_frequency=8,
                                           term_ranker=st.OncePerDocFrequencyRanker,                        
                                           # metadata=df['parsed']
                                           )
    file_name = party+".html"
    with open(file_name, "wb") as fn:
        fn.write(html.encode("utf-8"))
    

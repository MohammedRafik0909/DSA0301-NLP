#!/usr/bin/env python
# coding: utf-8

# In[20]:


import nltk


# In[21]:


from nltk.stem import PorterStemmer


# In[22]:


nltk.download("punkt")


# In[23]:


stemmer = PorterStemmer()
sentences =["I am running in the park",
            "The running shoes are on sale",
           "She ran to catch the bus",
           ]


# In[24]:


for i in sentences:
    words = nltk.word_tokenize(i)
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_sentences = " ".join(stemmed_words)
    print(f"Original: {i}")
    print(f"Stemmed : {stemmed_sentences}\n")


# In[ ]:





# In[ ]:





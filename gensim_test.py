import gensim
from gensim import corpora
from pprint import pprint


doc = [
   "CNTK formerly known as Computational Network Toolkit",
   "is a free easy-to-use open-source commercial-grade toolkit",
   "that enable us to train deep learning algorithms to learn like the human brain."
]


text_tokens = [[text for text in doc.split()] for doc in doc]

dict_LoS = corpora.Dictionary(text_tokens)

print(dict_LoS)

print(dict_LoS.token2id)

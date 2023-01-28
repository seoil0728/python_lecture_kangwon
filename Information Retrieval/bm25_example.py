from rank_bm25 import BM25Okapi

corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]

tokenized_corpus = [doc.split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)
print(bm25)
# <rank_bm25.BM25Okapi at 0x1047881d0>

query = "windy London"
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)
print('doc_scroes :', doc_scores)
# array([0.        , 0.93729472, 0.        ])

print(bm25.get_top_n(tokenized_query, corpus, n=1))
# ['It is quite windy in London']
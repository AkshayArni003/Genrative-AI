import nltk
# nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize

corpus = """Hello Welcome, to Akshay RK world of Artificial Intelligence.
We build AI tools and Automate the world happily. To make this world beautiful!
"""

"""
1st step: Convert Sentence ---> paragraph
"""

documents = nltk.sent_tokenize(corpus)
# print(documents)

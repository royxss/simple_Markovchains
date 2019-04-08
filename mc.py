# ref: https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
import numpy as np

# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
trump = open('/home/roy/Downloads/Kaggle_Data/markovchains/speeches.txt', encoding='utf8').read()

corpus = trump.split()

'''
Then, we define a function to give us all the pairs of words in the speeches. We’re using lazy evaluation, and yielding a generator object instead of actually filling up our memory with every pair of words:
'''

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)


'''
Then we instantiate an empty dictionary, and fill it words from our pairs. If the first word of the pair is already a key in the dictionary, simply append the next word to the list of words that follow that word. 
Otherwise, initialize a new entry in the dictionary with the key equal to the first word and the value a list of length one:

'''
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]


'''
Finally we pick some random word to kick off the chain, and choose the number of words we want to simulate:
'''
 
first_word = np.random.choice(corpus)

while first_word.istitle():
    first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 50


'''
After the first word, every word in the chain is sampled randomly from the list of words which have followed that word in Trump’s actual speeches:
'''

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

' '.join(chain)
from nltk.corpus import stopwords
from collections import Counter
from nltk.collocations import BigramCollocationFinder
import matplotlib.pyplot as plt
import string
import matplotlib

word_output = open('copy.txt', 'r')
words = word_output.read()

print ("No of unique tokens",len(list(Counter(words.split()))))
print ("No of unigram tokens",len(words.split()))

tokens = list(Counter(words.split()).values())

#Frequency-Rank Plot

print (tokens)
plt.xscale('log')
plt.yscale('log')
plt.title('ZipfLaw Rank Frequency Plot')
plt.xlabel('Frequency')
plt.ylabel('Rank')

x = [i for i in range(1, len(tokens) + 1)]
y = sorted(tokens,reverse=True)
plt.plot(x, y, color='blue')
plt.show()

print("Twenty Most common words")
for token,value in Counter(words.split()).most_common(20):
    print (token)

# Removing punctuation from stopwords
punct_set = set(string.punctuation)
stop_words = str.join(' ', stopwords.words('english'))

no_punct_stop_words = str.join('',[t for t in stop_words if t not in punct_set])
no_punct_stop_words = no_punct_stop_words.upper().split()

new_sentence = []
for word in words.split():
    if word not in no_punct_stop_words:
        new_sentence.append(word)

#Length of new sentences
print (len(new_sentence))

print("Twenty Most common words after stopwords removal")
for token,value in Counter(new_sentence).most_common(20):
    print (token)


# Unigram probability

words_split = words.split()
unigram_probability = {}
for items,values in Counter(words.split()).items():
    unigram_probability[items] =  values/len(words_split)

# Bigram probability and pmi values

bigram_probability = {}
pmi_values = {}
finder = BigramCollocationFinder.from_words(words_split)
for items,values in finder.ngram_fd.items():
    bigram_probability[items] = values/unigram_probability[items[0]]
    pmi_values[items] = values/(unigram_probability[items[0]]*unigram_probability[items[1]])


# Unigram,Bigram Frequency

unigram_frequency = dict(Counter(words_split).items())
bigram_frequency = dict(finder.ngram_fd.items())


bigram_data = [(key, pmi_values[key]) for key in sorted(pmi_values, key=pmi_values.get, reverse=True)]

for key,value in bigram_data[:30]:
    #print(key, "=", value, "\t\t", key, '=', bigram_frequency[key], '\t', key[0], '=', unigram_frequency[key[0]], " ", key[1], "=", unigram_frequency[key[1]])


# Bigram Threshold values

pmi_values_threshold = {}
for items,values in finder.ngram_fd.items():
    if int(values) > 100:
        pmi_values_threshold[items] = values/(unigram_probability[items[0]]*unigram_probability[items[1]])



threshold_data = [(key, pmi_values_threshold[key]) for key in sorted(pmi_values_threshold, key=pmi_values_threshold.get, reverse=True)]
for key,value in threshold_data[:10]:
   print(key, "=", value, "\t\t", key, '=', bigram_frequency[key], '\t', key[0], '=', unigram_frequency[key[0]], " ", key[1], "=", unigram_frequency[key[1]])

print (unigram_frequency['NEW'])
print (bigram_frequency[('NEW','YORK')])
print (pmi_values[('NEW','YORK')])

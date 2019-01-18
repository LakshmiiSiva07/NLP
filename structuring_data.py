"""
Structuring Data
"""
import nltk
import string


punct_set = set(string.punctuation)

disjoint_sentence_file = open('out.txt','r')
line_sentence_file = open('line.txt','w')
word_sentence_file = open('word.txt','w')

disjoint_sentences = disjoint_sentence_file.read()
sentences = nltk.sent_tokenize(disjoint_sentences)

print "Total number of Sentences:", len(sentences)

#Writing sentence Line by Line
for sentence in sentences:
    target_sentence = str.join(" ", sentence.splitlines())
    line_sentence_file.write(target_sentence)
    line_sentence_file.write("\n")

# Removing Punctuation marks and tokenizing words
with open("line.txt") as f:
    for line in f.readlines():
        punct_removed = str.join('',[t for t in line if t not in punct_set])
        print nltk.word_tokenize(punct_removed.upper())
        word_sentence_file.write(' '.join(nltk.word_tokenize(punct_removed.upper())))
        word_sentence_file.write("\n")

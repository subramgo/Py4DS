"""
A Pure Python Nearest Neighbour
Algorithm

Mar-07-2016
Gopi Subramanian
"""

# Small input
data = 'A dog chased a cat.\n \
        The cat ran away from the dog.\n \
        Cat are from tiger family.\n \
        Dog is loyal. \n \
        Cat and dog is pet.'

# Process to get words
sentences = data.split('\n')
words = [ sent.strip().lower().split(' ') for sent in sentences ]

def jacc_similarity(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return len(s1.intersection(s2)) /(1.0 * len(s1.union(s2)))

# Get all possible pairs and their
# Similarity
for i in range(len(words)):
	for j in range(i+1,len(words)):
		print i,j,jacc_similarity(words[i], words[j])

# Find Nearset Neighbours
test = "some cat pet".split(' ')
sim = [ jacc_similarity(test,word) for word in words]

max_sim = max(sim)

# Cluster assignment
for i  in range(len(sim)):
	if sim[i] == max_sim:
		print words[i], sim[i]




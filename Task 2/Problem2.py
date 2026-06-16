text = input()
k = int(input())
freq = {}
patterns = []

for i in range(len(text) - k + 1):
    kmer = text[i:i+k]
    if kmer in freq:
        freq[kmer] += 1
    else:
        freq[kmer] = 1

max_freq = max(freq.values())

for kmer, count in freq.items():
    if max_freq == count:
        patterns.append(kmer)

print(patterns)
    
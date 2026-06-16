pattern = input()
text = input()
d = int(input())

def hamming_distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance+=1
            
    return distance

text_length = len(text)
k = len(pattern)
positions = []

for i in range(text_length - k + 1):
    substring = text[i:i+k]
    if hamming_distance(substring, pattern) <= d:
        positions.append(i)

print(*positions)
        

pattern = input()
text = input()

positions = []
for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        positions.append(i)

print(positions)
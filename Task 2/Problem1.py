text = input()
pattern = input()

count = 0 
pattern_length = len(pattern)
text_length = len(text)

for i in range(text_length - pattern_length + 1):
    if pattern == text[i:i+pattern_length]:
        count += 1
        
print(count)
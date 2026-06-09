text = input()
pattern = input()

count = 0 

for base in text:
    if base == pattern:
        count+=1 
    
print(count)


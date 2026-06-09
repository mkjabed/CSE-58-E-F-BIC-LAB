dna = input()

complement = {
    "A" : "T", 
    "T" : "A", 
    "C" : "G", 
    "G" : "C"
}

result = ""

for base in dna: 
    result += complement[base]
    
print(result[::-1])
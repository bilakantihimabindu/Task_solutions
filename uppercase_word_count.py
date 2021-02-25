from collections import Counter

def count_word(filename):

    with open(filename,encoding='utf-8') as f:
        count = 0
        text = f.read()
        for character in text:            
            if character.isupper():                           
                count += 1
    return count
            
filename=".\word_count.txt"
c=count_word(filename)
print(c)

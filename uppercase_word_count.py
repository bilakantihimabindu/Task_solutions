def count_word(filename):
    with open(filename,encoding='utf-8') as f:
        count = 0
        text = f.read()        
        for word in text.split():
            i=0
            print(word)
            for character in word:
                if character.isupper():
                    i+=1
            if(i>0):
                              
                count += 1
    return count
            
filename=".\word_count.txt"
c=count_word(filename)
print(c)

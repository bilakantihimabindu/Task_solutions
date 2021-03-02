def count_word(filename):
    #read the content of file
    with open(filename,encoding='utf-8') as f:
        count = 0
        text = f.read()
        #splitting the file content using space
        for word in text.split():
            i=0
            
            #Character in word
            for character in word:
                #check if Character is uppercase
                if character.isupper():
                    i+=1
            if(i>0):
                              
                count += 1
    f.close()
    return count

#input path and file name
try:
    filename=".\word_count.txt"
    c=count_word(filename)

    print("No of words with uppercase letter in the file :"+filename+" is "+str(c))
except Exception as e:
    print(e)

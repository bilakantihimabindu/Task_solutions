def fml():
      
    with open(r".\word_count.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
        first_line=lines[0]        
        last_line = lines[-2:]             
        middle_line=int(len(lines)/2)
        middle_lines=lines[middle_line-1]
        #print(middle_line-1)
        if(len(middle_lines)==0):
            middle_lines="Line no: "+str(middle_line)+" is Empty in the file "
        
        print ("****************First Line of the file****************\n "+first_line+"\n****************Middle Line of the file****************\n "+middle_lines+"\n****************Last 2 Line of the file****************\n "+str(last_line))
    f.close()

try:
    fml()
except Exception as err:
    print(err)
    

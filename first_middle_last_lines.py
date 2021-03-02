def fml():
      
    with open(r"C:\Users\himabindu.bilakanti\Desktop\snapshot.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
        first_line=lines[0]        
        last_line = lines[-2:]             
        middle_line=int(len(lines)/2)
        middle_lines=lines[middle_line]
        if(len(middle_lines)==0):
            middle_lines="Line no: "+str(middle_line-1)+" is Empty in the file "
        
        print ("****************First Line of the file****************\n "+first_line+"\n****************Middle Line of the file****************\n "+middle_lines+"\n****************Last 2 Line of the file****************\n "+str(last_line))
    f.close()

try:
    fml()
except Exception as err:
    print(err)
    

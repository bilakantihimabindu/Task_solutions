from collections import OrderedDict

def first_unique_char(input_string):
    od = OrderedDict()
    for char in input_string:
        if char in od:
            od[char] += 1
        else:
            od[char] = 1
            

    for char in input_string:
        if od[char] == 1:
            return char,input_string.index(char)
    return -1

try:
    input_string="abcab"
    if len(input_string) == 0:
        print("Input string is empty. Please change the input string and execute")
    else:
        first_non_rep_char=first_unique_char(input_string)
        print("First non-repetative char and its index :"+str(first_non_rep_char))

except Exception  as e:
    print(e)


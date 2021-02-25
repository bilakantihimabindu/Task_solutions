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

input_string="abacb"

first_non_rep_char=first_unique_char(input_string)
print(first_non_rep_char)


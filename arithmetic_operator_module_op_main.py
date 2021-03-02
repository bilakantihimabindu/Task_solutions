from arithmetic_operator_module import *

s1 = OP(58,69)
s2 = OP(69,65)

print("Performing + operator overloading")
s3 = s1 + s2
print(s3.x,s3.y)

print("Performing - operator overloading")
s3 = s1 - s2
print(s3.x,s3.y)

print("Performing * operator overloading")
s3 = s1 * s2
print(s3.x,s3.y)

print("Performing / operator overloading")
s3 = s1 / s2
print(s3.x,s3.y)

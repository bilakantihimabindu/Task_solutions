def fibonic_series(n): 
    
    n1, n2 = 0, 1
    count = 0

   
    if n <= 0:
       print("Please enter a positive integer")
    elif n == 1:
       print("Fibonacci sequence upto",n,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < n:
           print(n1)
           nth = n1 + n2
           n1,n2=n2,nth           
           count += 1

try:
    N= int(input("enter n value :"))
    #N=257
    fibonic_series(N)
except Exception as e:
    print(e)

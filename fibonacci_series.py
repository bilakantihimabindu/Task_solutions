def fibonacci_series(n):
   if n <= 1:
       return n
   else:
       return(fibonacci_series(n-1) + fibonacci_series(n-2))
try:
    nterms= int(input("Enter n value :"))
    if nterms <= 0:
       print("Plese enter a positive integer")
    else:
       print("Fibonacci sequence:")
       for i in range(nterms):
           print(fibonacci_series(i))        
        
except Exception as e:
    print(e)



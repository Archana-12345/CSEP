def recur_factorial(n):
        if n==1:
                return n
        else:
                return n*recur_factorial(n-1)
n=8
if n<0:
        print("factorial is not exist")
elif n==0:
        print("The factorial of 0 is 1")
else:
        print("The factorial of",n, "is",recur_factorial (n))

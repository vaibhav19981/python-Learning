
def sum(n):
    """Returns the sum of all numbers from 1 to n."""
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
    

n=int(input("Enter a number: "))
sum(n)
print("The sum of all numbers from 1 to", n, "is", sum(n))
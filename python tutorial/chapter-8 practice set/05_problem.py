
def pattern(n):
    """Prints a pattern of numbers."""
    if n == 0:
        return
    else:
        print("*"*n)
        pattern(n-1)

n = int(input("Enter a number: "))
pattern(n)


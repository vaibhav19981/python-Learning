def inches_to_cm(n):
    """Converts inches to centimeters."""
    return n * 2.54

n = float(input("Enter a number in inches: "))
cm = inches_to_cm(n)
print(f"{n} inches is equal to {cm} centimeters.")


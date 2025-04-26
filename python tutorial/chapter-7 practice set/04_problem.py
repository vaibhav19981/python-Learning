number = int(input("Enter a number: "))

for i in range(2,number):
    if number % i == 0:
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number.")
# The code above checks if a number is prime by iterating from 2 to the number itself and checking for divisibility.
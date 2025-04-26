num = int(input("Enter the factorial number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("The factorial of", num, "is:", fact)
# time complexity: O(n)
# space complexity: O(1)

# The above code can be optimized to O(1) time complexity using the formula:
# fact=n!
# time complexity: O(1)
# space complexity: O(1)
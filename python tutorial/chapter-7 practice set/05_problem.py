n = int(input("Enter the last number: "))
sum=0

for i in range(1,n+1):
    sum += i
print("The sum of all numbers from 1 to", n, "is:", sum)

# time complexity: O(n)
# space complexity: O(1)

# The above code can be optimized to O(1) time complexity using the formula:
# sum=n(n+1)/2
# time complexity: O(1)
# space complexity: O(1)


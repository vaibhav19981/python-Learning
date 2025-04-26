number1 = int(input("enter number to in greatest"))
number2 = int(input("enter number to in greatest"))
number3 = int(input("enter number to in greatest"))
number4 = int(input("enter number to in greatest"))


if(number1>number2 and number1>number3 and number1>number4 ):
  print(f" {number1} is greatest ")
elif(number2>number1 and number2>number3 and number2>number4 ):
  print(f" {number2} is greatest ")
elif(number3>number2 and number3>number1 and number3>number4 ):
  print(f" {number3} is greatest ")
elif(number4>number2 and number4>number3 and number4>number1 ):
  print(f" {number4} is greatest ")



sample_list = []

sample_list.append(input("Enter a character: "))
sample_list.append(input("Enter a character: "))
sample_list.append(input("Enter a character: "))
sample_list.append(input("Enter a character: "))

sample_input = input("Enter a character: ")
if sample_input in sample_list:
    print(f"The character {sample_input} is present in the list")

else:
    print(f"The character {sample_input} is not present in the list")
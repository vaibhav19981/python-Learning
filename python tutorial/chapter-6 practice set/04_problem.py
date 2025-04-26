comment1 = "make a lot of money"
comment2 = "buy now"
comment3 = "subscribe this"
comment4 = "click this"

statement = input("Enter a statement: ")
if comment1 in statement or comment2 in statement or comment3 in statement or comment4 in statement:
    print(f"This is a spam message : {statement}")

else:
    print(f"This is not a spam message : {statement}")
"""
Exercise - 1
Find the minimum number from 3 given number
"""

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

if num1<num2 and num2<num3:
    print("Minimum number is: ", num1)
elif num2<num1 and num2<num3:
    print("Minimum number is: ", num2)
else:
    print("Minimum number is: ", num3)


"""
Exercise -2
ATM Machine Menu

1. Pin Change
2. Balance Check
3. Withdraw
4. Deposit
5. Exit
"""

menu = input("""
Hi there! Welcome to ATM
please choose,

1. Enter 1 for Pin Change
2. Enter 2 for Balance Check
3. Enter 3 for Withdraw
4. Enter 4 for Deposit
5. Enter 5 for Exit 
""")

if menu == "1":
    print("Pin Change")
elif menu == "2":
    print("Balance Change")
elif menu == "3":
    print("Withdraw")
elif menu == "4":
    print("Deposit")
else:
    print("Exit")



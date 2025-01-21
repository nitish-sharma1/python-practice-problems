#write a program to check if a number is positive, negative or zero

def check_nature_of_number(num):
    if num < 0:
        print(f"{num} is a negitive number")
    elif num > 0:
        print(f"{num} is a positive number")
    else:
        print("number is zero")


number = int(input("Enter the number : "))
check_nature_of_number(number)

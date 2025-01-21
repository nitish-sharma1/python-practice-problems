#write a program to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


s1 = int(input("Enter a number: "))
check_even_odd(s1)

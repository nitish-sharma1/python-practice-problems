'''
write a program to find the factorial of a number
'''


def factorial_iterative(num):
    """
    function to return factorial of number iteratively
    :param num:
    :return: factorial
    """
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


def factorial_recursive(num):
    """
    function to return factorial of number recursively
    :param num:
    :return:
    """
    if num == 1:
        return 1
    return num * factorial_recursive(num - 1)


num = int(input("Enter a num "))

res = factorial_recursive(num)
print(res)

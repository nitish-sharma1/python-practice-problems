#program to reverse a number

def reverse_number(num):
    reversed_num =0
    while num!=0 :
        rem = num%10
        num = num //10
        reversed_num = (reversed_num *10 ) + rem
    return reversed_num

print(reverse_number(198))
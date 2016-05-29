##Create a program that asks the user
##for a number and then prints out a list
##of all the divisors of that number. (If you don’t
##know what a divisor is, it is a number that divides evenly
##into another number. For example, 13 is a divisor of 26 because
##26 / 13 has no remainder.)

b = input("what is your number? ")

numbers = list(range(1, int(b)))

def divide(lista):
    list_of_divisors = []
    for n in lista:
        global b
        n = int(n)
        b = int(b)
        if b % n == 0:
            list_of_divisors.append(n)
        else:
            continue
    print(list_of_divisors)

divide(numbers)
            

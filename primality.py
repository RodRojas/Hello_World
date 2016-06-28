##Ask the user for a number and determine whether
##the number is prime or not. (For those who have forgotten,
##a prime number is a number that has no divisors.). You can
##(and should!) use your answer to [Exercise 4]
##(/exercise/2014/02/26/04-divisors.html to help you. Take this opportunity

class UserInput:
    user = input("give me a number ")

def prime():
    numero = int(UserInput.user)
    numeros = list(range(2, numero))
    if any((numero % x) == 0 for x in numeros):
        print("this is not a prime")
    else:
        print("this is a prime")
        

prime()

    



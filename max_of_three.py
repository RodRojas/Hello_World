##Implement a function that takes as input three variables,
##and returns the largest of the three. Do this without using the
##Python max() function!


a = 1
b = 2
c = 3

def max_three(a,b,c):
    if a > b and a > c:
        print ("a is the biggest")
    elif b > a and b > c:
        print ("b is the biggest")
    else: 
        print ("c is the biggest")
    



max_three(a,b,c)

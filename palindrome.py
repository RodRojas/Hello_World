##Ask the user for a string and print out whether this string
##is a palindrome or not.
##(A palindrome is a string that reads the same forwards and
## backwards.)

a = input("could you write something for me? ")

a = a.lower()

a = "".join( a.split() )

h = list(a)
j = h[::-1]
b = "".join(j)


if a == b:
    print("this is a palindrome")
else:
    print("sorry, this is not a palindrone")

# a.lower()

#''.join( old_string.split() )


    

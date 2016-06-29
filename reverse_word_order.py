##Write a program (using functions!) that asks the
##user for a long string containing multiple words.
##Print back to the user the same string, except with
##the words in backwards order. 

# string example : 'My name is Michele'


def ask():
    a = input("please write a sentence ")
    return a

def reverse_string():
    a = ask()
    a = a.split()
    a = a[::-1]
    a = ' '.join(a)
    print("this is a reversed version of your string: '{}'".format(a))

reverse_string()

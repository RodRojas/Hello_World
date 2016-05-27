##Write a program that takes a list of numbers
##(for example, a = [5, 10, 15, 20, 25]) and makes a new
##list of only the first and last elements of the given list. For practice,
##write this code inside a function.


a = [5, 10, 15, 20, 25]

def ends(a_list):
    new_list = []
    new_list.append(a_list[0])
    new_list.append(a_list[(len(a_list)-1)])
    print(new_list)

ends(a)

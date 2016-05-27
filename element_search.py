##Write a function that takes an ordered
##list of numbers (a list where the elements
##are in order from smallest to largest)
##and another number. The function decides whether or
##not the given number is inside the list and returns
##(then prints) an
##appropriate boolean.

num_list = [4,5,3,2,6,7,8]
other_num = 4

def ordering(x):
    x = sorted(x)
    return x

ordering(num_list)

def find_num(a_list, a_num):
    if a_num in a_list:
        print (True)
    else:
        print (False)
        
find_num(num_list,other_num)



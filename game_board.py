##Exercise
##
##Time for some fake graphics! Let’s say we
##want to draw game boards that look
##like this:
##
## --- --- --- 
##|   |   |   | 
## --- --- ---  
##|   |   |   | 
## --- --- ---  
##|   |   |   | 
## --- --- --- 
##This one is 3x3 (like in tic tac toe).
##Obviously, they come in many other sizes
##(8x8 for chess, 19x19 for Go, and many more).
##
##Ask the user what size game board they want to
##draw, and draw it for them to the screen using
##Python’s print statement.

grid = int(input("what size grid do you want? "))

def first_line():
    one_line = " --- "
    print(one_line * grid)

def cell():
    walls = "|   |"
    one_line = " --- "
    print(grid * ((walls * grid) + "\n" + (one_line * grid) + "\n"))

first_line()
cell()


    










    

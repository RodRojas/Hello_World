##Given a .txt file that has a list of a bunch of names,
##count how many of each name
##there are in the file, and print out the results to the screen. 



file = open('nameslist.txt', 'r')
str_file = file.read().split()



file_dict = dict.fromkeys(str_file, 0)



def counter(str_file, file_dict):
    for entry in str_file:
        file_dict[entry] += 1
        
    print (file_dict)

counter(str_file, file_dict)
        



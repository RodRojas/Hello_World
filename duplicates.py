##Write a program  that takes a
##list and returns a new list that contains
##all the elements of the first
##list minus all the duplicates.

a = ['a' ,'a' ,4 ,4 ,'f' ,'g' ,'e' ,'j' ,7 ]


def no_duplicates(lista):
    lista = set(lista)
    print(lista)

no_duplicates(a)

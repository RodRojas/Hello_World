##Write a program that asks the user how many Fibonnaci
##numbers to generate and then generates them. (Hint: The
##Fibonnaci seqence is
##a sequence of numbers where the next number in the
##sequence
##is the sum of the previous two numbers in the sequence.

n = int(input("give me a number for a Fibonacci sequence please "))

def fibonacci_2(n):
    n_list = list(range(1, (n+1)))
    if n == 0:
        print ("you do not want fibonaccis")
        
    else:
        sequence = []
        for member in n_list:
            try:
                new = (sequence[-2] + sequence[-1])
            except IndexError:
                new = 1
            sequence = sequence + [new]
            continue
        print (sequence)

fibonacci_2(n)

        
    

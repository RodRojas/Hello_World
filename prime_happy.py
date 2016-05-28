##Given two .txt files that have lists of numbers
##in them, find the numbers that are overlapping. One
##.txt file has a list of all prime numbers under 1000, and
##the other .txt file has
##a list of happy numbers up to 1000. primenumbers.txt and happynumbers.txt

prime_open = open("primenumbers.txt")
happy_open = open("happynumbers.txt")

prime = prime_open.read().split()
happy = happy_open.read().split()


def match(prime, happy):
    overlapping = []
    for n in prime:
        if n in happy:
            overlapping.append(n)
        else:
            continue
    print("these are the overlapping numbers: {}"
          .format(overlapping))
    
match(prime, happy)

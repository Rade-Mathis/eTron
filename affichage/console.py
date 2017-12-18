# simple terminal view
# 80 colomns warning : don't print a NxM grid where M >= 20

def display (grid, _) :
    print_a_line (len (grid[0]))
    for i in grid :
        for j in i :
            print ("|", end="")
            if j == "free" :
                print ("   ", end="")
            elif j == "player-1" :
                print (" X ", end="")
            elif j == "player-2" :
                print (" O ", end="")
            elif j == "old" or j == "old-1" or j == "old-2" :
                print ("###", end="")
            else :
                print (" ? ", end="")
        print ("|")
        print_a_line (len (i))


def print_a_line (n) :
    for j in range (n) :
        print ("+---", end="")
    print ("+")


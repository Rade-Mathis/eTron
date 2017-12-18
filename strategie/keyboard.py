def instruction (grid, step, possible_moves) :
    if step == 0 or step == 1:
        return place (grid, step, possible_moves)
    else :
        return move (grid, step, possible_moves)

def place (grid, step, possible_moves) :
    max_x = len (grid[0]) - 1
    max_y = len (grid) - 1
    if step == 1 :
        forbidden = possible_moves[1:]
    print ("Player {}, please write : xx,yy".format (step % 2 + 1))
    print ("(where xx is between {} and {}".format (0, max_x))
    print ("   and yy is between {} and {})".format (0, max_y))
    if step == 1 :
        print ("(note that {},{} has alredy been taken by player-1)"
               .format (forbidden[0], forbidden[1]))
    print ("then press enter.")

    order = input ("")
    coord = order.split(",")

    # check if format is correct
    if len (coord) != 2 :
        print ("waiting for exactly 1 ',' recived {}. Please try again"
               .format (max_x))
        return place (grid, step, possible_moves)
    try :
        x_coor = int (coord[0])
    except :
        print ("\"{}\" isn't a valid integer coordinate. Please try again"
               .format (coord[0]))
        return place (grid, step, possible_moves)
    try :
        y_coor = int (coord[1])
    except :
        print ("\"{}\" isn't a valid integer coordinate. Please try again"
               .format (coord[1]))
        return place (grid, step, possible_moves)

    # check if position is in the grid
    if x_coor > max_x :
        print ("First coordinate ({}) is too big (>{}). Please try again"
               .format (x_coor, max_x))
        return place (grid, step, possible_moves)
    if y_coor > max_y :
        print ("Second coordinate ({}) is too big (>{}). Please try again"
               .format (y_coor, max_y))
        return place (grid, step, possible_moves)

    # for player 2, check if it's not alredy taken
    if step == 1 and x_coor == forbidden[0] and y_coor == forbidden[1] :
        print ("The place has alredy been taken by player-1. Please try again")
        return place (grid, step, possible_moves)
    
    return (x_coor, y_coor)

def move (grid, step, possible_moves) :
    print ("Player {}, please write a direction from the following list :"
           .format(step % 2 + 1))
    print (_sym2word (possible_moves))
    print ("and then press enter.")

    order = input ("")
    if (len (order) < 1) :
        print ("Please enter some text before pressing enter.")
        return move (grid, step, possible_moves)
               
    if (order[0] in ['>', 'r', 'e', 'd']) and ('>' in possible_moves) :
        return '>'
    if (order[0] in ['^', 't', 'u', 'n', 'h']) and ('^' in possible_moves) :
        return '^'
    if (order[0] in ['<', 'l', 'w', 'g', 'o']) and ('<' in possible_moves) :
        return '<'
    if (order[0] in ['v', 'b', 's']) and ('v' in possible_moves) :
        return 'v'

    print ("{} isn't in the valid input list. Please try again."
           .format (order))
    return move (grid, step, possible_moves)
    
def _sym2word (symList) :
    if symList == [] :
        return []
    if symList[0] == ">" :
        direct = "right"
    elif symList[0] == "^" :
        direct = "top"
    elif symList[0] == "<" :
        direct = "left"
    elif symList[0] == "v" :
        direct = "bot"
    else :
        direct = "???"
    return [direct] + _sym2word (symList[1:])

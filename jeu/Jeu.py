import sys

class Jeu :
    def __init__ (self,
            max_x=7,            # Size N of the board
            max_y=7,            # Size M of the board
            strat_1="keyboard", # Player 1 strategy
            strat_2="keyboard", # Player 2 strategy
            view="console"      # What kind of display is used here :
                                ## "console", "gui-display"
    ) :
        self.grid = [[ "free" for i in range (max_x)] for j in range (max_y)]
        self.strat_1 = get_strategy (strat_1)
        self.strat_2 = get_strategy (strat_2)
        self.view = get_view (view)
        self.step = 0

    def run (self) :
        while (self.winner () is None) :
            self.display ()
            self.update ()
        self.display ()
        return self.winner ()

    def winner (self) :
        if self.step == 0 :
            if len (self.grid) < 1 or len (self.grid[0]) < 1 :
                return "player-2"
            return None
        if self.step == 1 :
            if len (self.grid) == 1 and len (self.grid[0]) == 1 :
                return "player-1"
            return None

        if self.step % 2 == 0 and self._possible_moves () == [] :
            return "player-2"
        if self.step % 2 == 1 and self._possible_moves () == [] :
            return "player-1"
        return None

    def update (self) :
        player = self.step % 2 + 1
        strat  = self.strat_1 if player == 1 else self.strat_2

        # 1st turn : place yourself
        if self.step == 0 :
            orders = strat (self.grid, self.step, ["everywhere"])
            if (orders[0] < 0 or orders[0] >= len (self.grid[0])
                or orders[1] < 0 or orders[1] >= len (self.grid)
            ) :
                failed (player)
            self.x1 = orders[0]
            self.y1 = orders[1]
            self.grid[orders[1]][orders[0]] = "player-1"

        elif self.step == 1 :
            for i in range (len (self.grid)) :
                for j in range (len (self.grid[i])) :
                    if self.grid[i][j] == "player-1" :
                        alredy_taken = [j, i]
            orders = strat (self.grid, self.step,
                            ["everywhere but"] + alredy_taken)
            if (orders[0] < 0 or orders[0] >= len (self.grid[0])
                or orders[1] < 0 or orders[1] >= len (self.grid)
                or (orders[0] == alredy_taken[0]
                    and orders[1] == alredy_taken[1])
            ) :
                failed (player)
            self.x2 = orders[0]
            self.y2 = orders[1]                
            self.grid[orders[1]][orders[0]] = "player-2"

        # other turns : move to adjacent tile
        else :
            order = strat (self.grid, self.step, self._possible_moves())
            if not order in self._possible_moves() :
                failed (player)
            x_move = -1 if order == "<" else (1 if order == ">" else 0)
            y_move = -1 if order == "^" else (1 if order == "v" else 0)
            if player == 1 :
                self.grid[self.y1][self.x1] = "old-1"
                self.x1 += x_move
                self.y1 += y_move
                self.grid[self.y1][self.x1] = "player-1"
            else :
                self.grid[self.y2][self.x2] = "old-2"
                self.x2 += x_move
                self.y2 += y_move
                self.grid[self.y2][self.x2] = "player-2"
            
        self.step += 1 

    def display (self) :
        self.view (self.grid, self.step)

    def _possible_moves (self) :
        if self.step < 2 :
            return None
        if self.step % 2 == 0 :
            x = self.x1
            y = self.y1
        else :
            x = self.x2
            y = self.y2
        max_x = len (self.grid[0]) - 1
        max_y = len (self.grid) -1
        ret = []
        if (x < max_x and self.grid[y][x+1] == "free") :
            ret.append (">")
        if (y > 0     and self.grid[y-1][x] == "free") :
            ret.append ("^")
        if (x > 0     and self.grid[y][x-1] == "free") :
            ret.append ("<")
        if (y < max_y and self.grid[y+1][x] == "free") :
            ret.append ("v")
        return ret


def get_strategy (name) :
    if name == "keyboard" :
        import strategie.keyboard
        return strategie.keyboard.instruction
    else :
        print ("fatal error : Unknown strategy {}".format (name))
        sys.exit (1)

def get_view (name) :
    if name == "console" :
        import affichage.console
        return affichage.console.display
    elif name == "gui-display" :
        import affichage.gui
        window = affichage.gui.GuiDisplayer ()
        return window.display
    elif name == None :
        return lambda : None
    else :
        print ("[fatal error] Unknown view {}".format (name))
        sys.exit (1)

def failed (player) :
    print ("[fatal error] player {} is unable to have a working strategy"
           .format (player))
    sys.exit (2)

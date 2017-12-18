import sys, pygame
from threading import Thread
from pygame.locals import *

class GuiDisplayer :
    def __init__ (self) :
        pygame.init ()
        self.DISPLAYSURF = pygame.display.set_mode((800, 800))
        pygame.display.set_caption ("eTron")
        self.DISPLAYSURF.fill ((0xBB, 0xBB, 0xBB))
        self.fps_clock = pygame.time.Clock ()
        self._launched = False
        Thread(target = self._display).start()

    def display (self, grid, step) :
        self.grid = grid
        self.step = step
        self._launched = True

    def _display (self) :
        while True :
            for event in pygame.event.get () :
                if event.type == QUIT :
                    pygame.quit ()
                    sys.exit ()

            while not self._launched :
                pygame.time.wait (100)

            n = len (self.grid)
            m = len (self.grid[0])
            hight = (800 / n) - 2
            width = (800 / m) - 2
            for i in range (m) :
                x = (i * 800 / m) + 1
                for j in range (n) :
                    y = (j * 800 / n) + 1

                    # draw rectagle
                    if self.grid[j][i] == "free" :
                        color = (0xFF, 0xFF, 0xFF)
                    elif self.grid[j][i] == "player-1" :
                        color = (0x0,  0x0,  0xFF)
                    elif self.grid[j][i] == "player-2" :
                        color = (0xFF, 0x0,  0x0)
                    elif self.grid[j][i] == "old-1" :
                        color = (0x77, 0x77, 0xFF)
                    elif self.grid[j][i] == "old-2" :
                        color = (0xFF, 0x77, 0x77)
                    pygame.draw.rect (self.DISPLAYSURF, color,
                                      (x, y, width, hight))

                    # draw possible move arrow
                    if self.grid[j][i] == "free" and self.step > 1 :
                        if self.step % 2 == 0 :
                            color = (0x00, 0x00, 0xFF)
                            player = 1
                        else :
                            color = (0xFF, 0x00, 0x00)
                            player = 2
                        center = (x + (width / 2),  y + (hight / 2))
                        top = y + (hight / 10)
                        bot = y + hight - (hight / 10)
                        left = x + (width / 10)
                        right = x + width - (width / 10)
                        top_l = (left, top)
                        bot_l = (left, bot)
                        bot_r = (right, bot)
                        top_r = (right, top)
                        if (i > 0
                            and self.grid[j][i-1] == "player-" + str (player)
                        ) :
                            pygame.draw.polygon (self.DISPLAYSURF, color,
                                                 [top_l, center, bot_l])
                        elif (j < n - 1
                              and self.grid[j+1][i] == "player-" + str (player)
                        ) :
                            pygame.draw.polygon (self.DISPLAYSURF, color,
                                                 [bot_l, center, bot_r])
                        elif (i < m - 1
                              and self.grid[j][i+1] == "player-" + str (player)
                        ) :
                            pygame.draw.polygon (self.DISPLAYSURF, color,
                                                 [bot_r, center, top_r])
                        elif (j > 0
                              and self.grid[j-1][i] == "player-" + str (player)
                        ) :
                            pygame.draw.polygon (self.DISPLAYSURF, color,
                                                 [top_r, center, top_l])
                        
            pygame.display.update ()
            self.fps_clock.tick(12)

# TODO : maybe try to inverse hierarchy
def run () :

    pygame.init ()
    self.DISPLAYSURF = pygame.display.set_mode((800, 800))
    pygame.display.set_caption ("eTron")
    self.DISPLAYSURF.fill ((0xBB, 0xBB, 0xBB))
    self.fps_clock = pygame.time.Clock ()

    while True :
        for event in pygame.event.get () :
            if event.type == QUIT :
                pygame.quit ()
                sys.exit ()

        m = len (grid)
        n = len (grid[0])
        width = (800 / n) - 2
        hight = (800 / m) - 2
        for i in range (n) :
            y = (i * 800 / n) + 1
            for j in range (m) :
                x = (j * 800 / m) + 1
                if grid[i][j] == "free" :
                    color = (0xFF, 0xFF, 0xFF)
                elif grid[i][j] == "player-1" :
                    color = (0x0,  0x0,  0xFF)
                elif grid[i][j] == "player-2" :
                    color = (0xFF, 0x0,  0x0)
                elif grid[i][j] == "old-1" :
                    color = (0x77, 0x77, 0xFF)
                elif grid[i][j] == "old-2" :
                    color = (0xFF, 0x77, 0x77)
                pygame.draw.rect (self.DISPLAYSURF, color,
                                  (x, y, width, hight))
        pygame.display.update ()
        self.fps_clock.tick (60)

import pygame
# Import the system module
import sys
# Close the window and exit

class Snake:

    def __init__(self):
        pygame.init()
        self.size_x = 800
        self.size_y = 600
        self.screen = pygame.display.set_mode((self.size_x, self.size_y))
        # events
        self.events = pygame.event.get()
        # check
        print(self.events)


    def updatingDisplay(self):
        pygame.display.update()

    def quit(self):
        pygame.display.quit()
        sys.exit()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.update()
    loop = True
    while loop:
        

        for event in pygame.event.get():
                
            if event.type == 3:
                if event.key == pygame.K_DOWN:
                    print('Down was pressed')

                if event.key == pygame.K_UP:
                    print('Up was pressed')

                if event.key == pygame.K_RIGHT:
                    print('Right was pressed')

                if event.key == pygame.K_LEFT:
                    print('Left was pressed')
                if event.key == pygame.K_q:
                    loop = False
                
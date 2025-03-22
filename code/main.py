import pygame as pg
import random, sys

def main():
    pg.init()

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 600
    
    SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Flappy Bird")

    clock = pg.time.Clock()
    FPS = 60

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

        SCREEN.fill((160, 200, 120))

        pg.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
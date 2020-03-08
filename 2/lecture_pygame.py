import pygame
from random import randrange

    
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.time.Clock()


windows, nwin = [], 0
while True:
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.time.wait(500)
    evs = pygame.event.get()
    for e in evs:
        if e.type is pygame.QUIT:
            print("QUIT")
            break
        if e.type is pygame.MOUSEBUTTONDOWN:
            if e.button == 3:
                color = pygame.Color(randrange(100,256), randrange(100,256),randrange(100,256))
                t = randrange(1, 500)
                end = (e.pos[0] + t if e.pos[0] + t <= 800 else 800, e.pos[1])
                windows.append((nwin, color, pygame.draw.line(screen, color, e.pos, end, 1)))
                nwin += 1
        else:
            for (i, color, rect) in reversed(windows):
                if hasattr(e, "pos") and rect.collidepoint(e.pos):
                    print(f"{e} to {i}")
                    break
            else:
                print(e)

    else:
        screen.fill(0)
        for i, color, rect in windows:
            screen.fill(color, rect)

        pygame.display.flip()
        continue
    break

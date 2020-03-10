import sys, pygame
pygame.init()

dx, dy = 0.1, 0.1
size = width, height = 4000, 4300
screen_size = int(width * dx) + 1, int(height * dy) + 1
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load("intro_ball.gif")
x, y = width / 2, height / 2
ballrect = ball.get_rect()
w, h = ballrect.w / dx, ballrect.h / dy
pygame.time.set_timer(pygame.USEREVENT, 10)
pull = False

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN  and ballrect.collidepoint(event.pos): 
        pull = -event.pos[0] + ballrect.centerx, -event.pos[1] + ballrect.centery
    elif pull and event.type == pygame.MOUSEMOTION:
        x, y = pull[0] + event.pos[0] / dx, pull[1] + event.pos[1] / dy
    elif event.type == pygame.MOUSEBUTTONUP:
        pull = False
    elif event.type == pygame.USEREVENT:
        if not pull:
            if x - w / 2 < 0 or x + w / 2 > width:
                speed[0] = -speed[0]
            if y - h / 2 < 0 or y + h / 2 > height:
                speed[1] = -speed[1]
        
            x += speed[0]
            y += speed[1]
    
    screen.fill(black)
    ballrect.center = int(x * dx), int(y * dy)
    screen.blit(ball, ballrect)
    pygame.display.flip()

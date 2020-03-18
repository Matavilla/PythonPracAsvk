import sys, pygame, math

class Ball:
    def __init__(self, points, obj):
        dx = 0.1
        dy = 0.1
        self.x, self.y = points
        self.ballrect = obj.get_rect()
        self.w = self.ballrect.w / dx
        self.h = self.ballrect.h / dy
        self.circle = obj
        self.pull = False
        self.harm = None
        self.speed = [20, 20]

def check_distance (b1, b2):
    d = math.sqrt(abs(b1.ballrect.center[0] - b2.ballrect.center[0]) ** 2 + abs(b1.ballrect.center[1] - b2.ballrect.center[1]) ** 2)
    return d <= abs(2 * math.sqrt(2) * (b1.ballrect.right - b1.ballrect.center[0]))


pygame.init()
dx, dy = 0.1, 0.1
size = width, height = 4000, 4300
screen_size = int(width * dx) + 1, int(height * dy) + 1
black = 0, 0, 0

screen = pygame.display.set_mode(screen_size)

balls = [Ball((width / 4, height / 4), pygame.image.load("intro_ball.gif")), Ball((width * 0.75, height * 0.75), pygame.image.load("intro_ball.gif"))]
pygame.time.set_timer(pygame.USEREVENT, 10)

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: sys.exit()
    for b in balls:
        if event.type == pygame.MOUSEBUTTONDOWN  and b.ballrect.collidepoint(event.pos): 
            b.pull = -event.pos[0] + b.ballrect.centerx, -event.pos[1] + b.ballrect.centery
        elif b.pull and event.type == pygame.MOUSEMOTION:
            b.x, b.y = b.pull[0] + event.pos[0] / dx, b.pull[1] + event.pos[1] / dy
        elif event.type == pygame.MOUSEBUTTONUP:
            b.pull = False
        elif event.type == pygame.USEREVENT:
            if not b.pull:
                if b.x - b.w / 2 < 0 or b.x + b.w / 2 > width:
                    b.speed[0] = -b.speed[0]
                if b.y - b.h / 2 < 0 or b.y + b.h / 2 > height:
                    b.speed[1] = -b.speed[1]

            b.x += b.speed[0]
            b.y += b.speed[1]
    
        if (abs(balls[0].ballrect.left - balls[1].ballrect.right) < 5 or abs(balls[0].ballrect.right - balls[1].ballrect.left) < 5) and check_distance(balls[0], balls[1]) and (balls[0].harm != balls[1] or balls[1].harm != balls[0]):
            balls[0].speed[0] = -balls[0].speed[0]
            balls[1].speed[0] = -balls[1].speed[0]
            balls[0].harm = balls[1]
            balls[1].harm = balls[0]
        elif ((abs(balls[0].ballrect.top - balls[1].ballrect.bottom) < 5 or abs(balls[0].ballrect.bottom - balls[1].ballrect.top) < 5)) and check_distance(balls[0], balls[1]) and (balls[0].harm != balls[1] or balls[1].harm != balls[0]):
            balls[0].speed[1] = -balls[0].speed[1]
            balls[1].speed[1] = -balls[1].speed[1]
            balls[0].harm = balls[1]
            balls[1].harm = balls[0]
        elif not check_distance(balls[0], balls[1]):
            balls[0].harm = None
            balls[1].harm = None

    screen.fill(black)
    for b in balls:
        b.ballrect.center = int(b.x * dx), int(b.y * dy)
        screen.blit(b.circle, b.ballrect)
        pygame.display.flip()

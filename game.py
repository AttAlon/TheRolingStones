import pygame
import random

BACKROUND = (123, 189, 189)
LEANGTH = 500

MAX_ROCKS = 10
MAX_ROCK_SIZE = 70

PLAYER_SIZE = 25

APPLE_SIZE = 20
MAX_APPLE = 2

#COLOR_APPLE_3 = (,,)
#COLOR_APPLE_1 = (,,)
#COLOR_APPLE_2 = (,,)

#ROCK_WIDTH = 30
#ROCK_HIGHT = 30

def getRandomRockSize():
    return random.randint(5,MAX_ROCK_SIZE+1)

def getRandomX():
    return random.randint(0,LEANGTH+1)

def isDead(player, rocks):
    for r in rocks:
        if r.y+r.SIZE >= player.y and player.x <= r.x+r.SIZE and player.x+PLAYER_SIZE >= r.x and r.y <= player.y+PLAYER_SIZE:
            # Dead = True
            return True


def isEat(player, apple):
    if apple.y + APPLE_SIZE >= player.y and player.x <= apple.x+APPLE_SIZE and player.x+PLAYER_SIZE >= apple.x and apple.y <= player.y+PLAYER_SIZE:

        # add the apple power to the pase
        player.pase += apple.power
        return True


def moveApples(apples, win, player):
    delete = []
    for apple in apples:

        if isEat (player, apple):
            delete.append(apple)
        else:
            pygame.draw.rect(win, (0,0,0), (apple.x, apple.y, APPLE_SIZE, APPLE_SIZE))

    return delete


def moveRocks(rocks, win):
    delete = []
    for r in rocks:
        r.y += r.pase
        r.pase += r.pase / 7
        if r.y < LEANGTH :
            pygame.draw.rect(win, r.color, (r.x, r.y, r.SIZE, r.SIZE))
        else:
            delete.append(r)
    return delete

class rock:
    x = 250
    y = 0.0
    SIZE = 0
    pase = 1.0
    color = (64, 0, 100)

class player:
    x = 250
    y = 450
    width = PLAYER_SIZE
    hight = PLAYER_SIZE
    pase = 6
    color = (70, 20, 10)

class apple:
    x = 0;
    y = 0;

    power = 1; #power of the apple between: 1, 2 ,3


def main():
    pygame.init()
    #startMenue()
    player1 = player()
    win = pygame.display.set_mode((LEANGTH, LEANGTH))
    pygame.display.set_caption("Try To Survive...")
    rocks = []
    apples = []

    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player1.x > player1.pase:
            player1.x -= player1.pase
        if keys[pygame.K_RIGHT] and player1.x < LEANGTH - player1.width - player1.pase:
            player1.x += player1.pase
        if keys[pygame.K_UP] and player1.y > player1.pase:
            player1.y -= player1.pase
        if keys[pygame.K_DOWN] and player1.y < (LEANGTH - player1.hight - player1.pase):
            player1.y += player1.pase

        # add new apple
        if len(apples) < MAX_APPLE:
            this_apple = apple()
            this_apple.x = getRandomX()
            this_apple.y = getRandomX()

            this_apple.power = (getRandomRockSize() % 3) + 1
            apples.append(this_apple)

        # add new rock
        if len(rocks) < MAX_ROCKS:
            this_rock = rock()
            this_rock.x = getRandomX()
            this_rock.SIZE = getRandomRockSize()
            this_rock.pase = this_rock.SIZE / 20
            #print(this_rock.pase)
            rocks.append(this_rock)

        win.fill((BACKROUND))

        #move apples
        delete = moveApples(apples, win, player1)
        for ap in delete:
            apples.remove(ap)

        delete = moveRocks(rocks, win)
        for r in delete:
            rocks.remove(r)

        pygame.draw.rect(win, player1.color, (player1.x, player1.y, player1.width, player1.hight))
        pygame.display.update()
        if(isDead(player1, rocks)):
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
"""
for x in range(player.x, player.x+PLAYER_SIZE):
        for y in range(player.y, player.y+PLAYER_SIZE):
            playerBlock.append((x, y))
    for r in rocks:
        for x in range(r.x, r.x+ROCK_WIDTH):
            for y in range(r.y, r.y+ROCK_HIGHT):
                for point in playerBlock:
                    if (x, y) == point:
                        Dead = True
                        break
"""

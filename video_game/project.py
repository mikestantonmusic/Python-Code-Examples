import pygame
import random

# initialize pygame
pygame.init()

# set the screen size and caption
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame Game")

# create a moving object class which inherits from the pygame rect class
class moving_obj(pygame.Rect):
    def __init__(self, left, top, width, height, x_dir, y_dir):
        super().__init__(left, top, width, height)
        self.x_dir = x_dir
        self.y_dir = y_dir

    def move_random(self, iter):

        new_x_dir=self.x_dir
        new_y_dir=self.y_dir

        # define object direction logic for when the object is not bumping into the edges
        if 0 <= self.left <= (screen_width - self.width) and 0 <= self.top <= (screen_height - self.height):
            if random.randint(0, 100) == iter:
                new_x_dir=-1*self.x_dir
            if random.randint(0, 100) == iter:
                new_y_dir=-1*self.y_dir

        # establish what happens when one of the moving objects bumps into an edge
        elif self.left < 0:
            new_x_dir=-1*self.x_dir
        elif self.top < 0:
            new_y_dir=-1*self.y_dir
        elif self.left > (screen_width - self.width):
            new_x_dir=-1*self.x_dir
        elif self.top > (screen_height - self.height):
            new_y_dir=-1*self.y_dir

        # move the object in the established direction
        self.x_dir = new_x_dir
        self.y_dir = new_y_dir
        self.left = self.left + self.x_dir
        self.top = self.top + self.y_dir

# create an object for the player
player_size = 25
player_color = (0,0,0)
player = pygame.Rect(0, 0, player_size, player_size)

# create an obstacle object
obstacle_xpos = 175
obstacle_ypos = 175
obstacle_width = 115
obstacle_height = 175
obstacle_color = (255,0,0)
obstacle = moving_obj(obstacle_xpos, obstacle_ypos, obstacle_width, obstacle_height,1,1)

# create another obstacle object
obstacle2_xpos = 275
obstacle2_ypos = 275
obstacle2_width = 115
obstacle2_height = 175
obstacle2_color = (255,0,0)
obstacle2 = moving_obj(obstacle2_xpos, obstacle2_ypos, obstacle2_width, obstacle2_height,1,1)

obstacle_list = [obstacle, obstacle2]

# create a target object
target_xpos = 90
target_ypos = 175
target_width = 25
target_height = 25
target_color = (0,255,0)
target = moving_obj(target_xpos, target_ypos, target_width, target_height,1,1)

target_list = [target]

# set the end of game font
game_over_font = pygame.font.Font(None, 36)

# set the speed of movement
speed = 1

# set the starting point of player
xd = 0
yd = 0

# run the game loop
i = 0
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xd = -speed
            elif event.key == pygame.K_RIGHT:
                xd = speed
            elif event.key == pygame.K_UP:
                yd = -speed
            elif event.key == pygame.K_DOWN:
                yd = speed
            elif event.key == K_BACKSPACE:
                gameOn = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xd = 0
            elif event.key == pygame.K_RIGHT:
                xd = 0
            elif event.key == pygame.K_UP:
                yd = 0
            elif event.key == pygame.K_DOWN:
                yd = 0

    # stop movement if the player hits the edge of the screen
    if 0 <= player.x <= (screen_width - player_size) and 0 <= player.y <= (screen_height - player_size):
        player.x = player.x + xd
        player.y = player.y + yd
    elif player.x < 0 :
        player.x = 0 
        xd=0
    elif player.y < 0 :
        player.y = 0 
        yd=0
    elif player.x > (screen_width - player_size):
        player.x = (screen_width - player_size)
        xd=0
    elif player.y > (screen_height - player_size):
        player.y = (screen_height - player_size)
        yd=0

    # move the moving objects!
    obstacle.move_random(i)

    obstacle2.move_random(i)

    target.move_random(i)

    # next use rect.colliderect() to check if rectangles collide
    if player.collidelist(obstacle_list) != -1:
        # display "game over" message and wait for user to close window
        game_over_text = game_over_font.render("Game Over!", True, (255, 255, 0))
        game_over_rect = game_over_text.get_rect(center=screen.get_rect().center)
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    
    if player.collidelist(target_list) != -1:
        # display "you win" message and wait for user to close window
        game_over_text = game_over_font.render("You Win!", True, (255, 255, 0))
        game_over_rect = game_over_text.get_rect(center=screen.get_rect().center)
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    
    # fill the screen with a color
    screen.fill((255, 255, 255))

    # draw the player on the screen
    pygame.draw.rect(screen, player_color, player)

    # draw the obstacle on the screen
    pygame.draw.rect(screen, obstacle_color, obstacle)

    # draw the obstacle on the screen
    pygame.draw.rect(screen, obstacle2_color, obstacle2)

    # draw the target on the screen
    pygame.draw.rect(screen, target_color, target)

    pygame.time.wait(5)

    # update the display
    pygame.display.update()

    # the "i" variable creates a background status which is referenced by random events 
    if i==99:
        i=0
    else:
        i=i+1

# Quit pygame
pygame.quit()
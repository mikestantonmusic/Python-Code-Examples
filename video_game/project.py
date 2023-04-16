import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen size and caption
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame Game")

# Create a player object
player_size = 25
player_color = (0,0,0)
player = pygame.Rect(0, 0, player_size, player_size)


# Create an obstacle object
obstacle_xpos = 175
obstacle_ypos = 175
obstacle_width = 115
obstacle_height = 175
obstacle_color = (255,0,0)
obstacle = pygame.Rect(obstacle_xpos, obstacle_ypos, obstacle_width, obstacle_height)

# Create another obstacle object
obstacle2_xpos = 275
obstacle2_ypos = 275
obstacle2_width = 115
obstacle2_height = 175
obstacle2_color = (255,0,0)
obstacle2 = pygame.Rect(obstacle2_xpos, obstacle2_ypos, obstacle2_width, obstacle2_height)

obstacle_list = [obstacle, obstacle2]


# Create a target object
target_xpos = 90
target_ypos = 175
target_width = 25
target_height = 25
target_color = (0,255,0)
target = pygame.Rect(target_xpos, target_ypos, target_width, target_height)

target_list = [target]


game_over_font = pygame.font.Font(None, 36)

# Set the speed of movement
speed = 1

# Set the starting point of movement
xd = 0
yd = 0


# NEXT - Create a class for all these functions!
# Create a function for player movement
def plr_mvmt(x_dir, y_dir):
    player.x = player.x + x_dir
    player.y = player.y + y_dir

def obs_mvmt(x_dir, y_dir):
    obstacle.x = obstacle.x + x_dir
    obstacle.y = obstacle.y + y_dir

def obs2_mvmt(x_dir, y_dir):
    obstacle2.x = obstacle2.x + x_dir
    obstacle2.y = obstacle2.y + y_dir

def targ_mvmt(x_dir, y_dir):
    target.x = target.x + x_dir
    target.y = target.y + y_dir

# Run the game loop
i = 0
obs_x_dir = 1
obs_y_dir = 1
obs2_x_dir = 1
obs2_y_dir = 1
tar_x_dir = 1
tar_y_dir = 1


running = True
while running:
    # Handle events
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


    #stop movement if the player hits the edge of the screen
    if 0 <= player.x <= (screen_width - player_size) and 0 <= player.y <= (screen_height - player_size):
        plr_mvmt(x_dir = xd, y_dir = yd)
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

# Create a function for obstacle movement


    if 0 <= obstacle.x <= (screen_width - obstacle_width) and 0 <= obstacle.y <= (screen_height - obstacle_height):
        if random.randint(0, 100) == i:
            obs_x_dir = -1*obs_x_dir
        if random.randint(0, 100) == i:
            obs_y_dir = -1*obs_y_dir
    elif obstacle.x < 0:
        obs_x_dir = -1*obs_x_dir
    elif obstacle.y < 0 :
        obs_y_dir = -1*obs_y_dir
    elif obstacle.x > (screen_width - obstacle_width):
        obs_x_dir = -1*obs_x_dir
    elif obstacle.y > (screen_height - obstacle_height):
        obs_y_dir = -1*obs_y_dir
    obs_mvmt(obs_x_dir, obs_y_dir)

    if 0 <= obstacle2.x <= (screen_width - obstacle2_width) and 0 <= obstacle2.y <= (screen_height - obstacle2_height):
        if random.randint(0, 100) == i:
            obs2_x_dir = -1*obs2_x_dir
        if random.randint(0, 100) == i:
            obs2_y_dir = -1*obs2_y_dir
    elif obstacle2.x < 0:
        obs2_x_dir = -1*obs2_x_dir
    elif obstacle2.y < 0 :
        obs2_y_dir = -1*obs2_y_dir
    elif obstacle2.x > (screen_width - obstacle2_width):
        obs2_x_dir = -1*obs2_x_dir
    elif obstacle2.y > (screen_height - obstacle2_height):
        obs2_y_dir = -1*obs2_y_dir
    obs2_mvmt(obs2_x_dir, obs2_y_dir)


    if 0 <= target.x <= (screen_width - target_width) and 0 <= target.y <= (screen_height - target_height):
        if random.randint(0, 100) == i:
            tar_x_dir = -1*tar_x_dir
        if random.randint(0, 100) == i:
            tar_y_dir = -1*tar_y_dir
    elif target.x < 0:
        tar_x_dir = -1*tar_x_dir
    elif target.y < 0:
        tar_y_dir = -1*tar_y_dir
    elif target.x > (screen_width - target_width):
        tar_x_dir = -1*tar_x_dir
    elif target.y > (screen_height - target_height):
        tar_y_dir = -1*tar_y_dir
    targ_mvmt(tar_x_dir, tar_y_dir)


    # next use rect.colliderect() to check if rectangles collide
    if player.collidelist(obstacle_list) != -1:
        # Display "game over" message and wait for user to close window
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
        # Display "you win" message and wait for user to close window
        game_over_text = game_over_font.render("You Win!", True, (255, 255, 0))
        game_over_rect = game_over_text.get_rect(center=screen.get_rect().center)
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    


    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw the player on the screen
    pygame.draw.rect(screen, player_color, player)

    # Draw the obstacle on the screen
    pygame.draw.rect(screen, obstacle_color, obstacle)

    # Draw the obstacle on the screen
    pygame.draw.rect(screen, obstacle2_color, obstacle2)

    # Draw the target on the screen
    pygame.draw.rect(screen, target_color, target)

    pygame.time.wait(5)

    # Update the display
    pygame.display.update()

    if i==99:
        i=0
    else:
        i=i+1

# Quit pygame
pygame.quit()
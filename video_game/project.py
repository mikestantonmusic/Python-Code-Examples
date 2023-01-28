import pygame

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


# Create dimensions for a line object
obstacle_width = 3
obstacle_x_range = (60,80)
obstacle_y_range = (130,100)
line_color = (255, 0, 0)


# Set the speed of movement
speed = 1

# Set the starting point of movement
xd = 0
yd = 0

# Create a function for player movement
def plr_mvmt(x_dir, y_dir):
    player.x = player.x + x_dir
    player.y = player.y + y_dir

# Run the game loop
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



    



    


    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw the player on the screen
    pygame.draw.rect(screen, player_color, player)

    # Draw the obstacle on the screen
    pygame.draw.line(screen, line_color, obstacle_x_range, obstacle_y_range, obstacle_width)

    pygame.time.wait(5)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
import pygame

# Initialize pygame
pygame.init()

# Set the screen size and caption
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame Game")

# Create a rectangle object
rect_size = 25
rect = pygame.Rect(0, 0, rect_size, rect_size)

# Set the speed of movement
speed = 1

# Set the starting point of movement
xd = 0
yd = 0

# Create a function for player movement
def plr_mvmt(x_dir, y_dir):
    rect.x = rect.x + x_dir
    rect.y = rect.y + y_dir

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


    
    if 0 <= rect.x <= (screen_width - rect_size) and 0 <= rect.y <= (screen_height - rect_size):
        plr_mvmt(x_dir = xd, y_dir = yd)
    elif rect.x < 0 :
        rect.x = 0 
        xd=0
    elif rect.y < 0 :
        rect.y = 0 
        yd=0
    elif rect.x > (screen_width - rect_size):
        rect.x = (screen_width - rect_size)
        xd=0
    elif rect.y > (screen_height - rect_size):
        rect.y = (screen_height - rect_size)
        yd=0



    



    


    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw the rectangle on the screen
    pygame.draw.rect(screen, (0, 0, 0), rect)

    pygame.time.wait(5)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
import pygame  # Import the Pygame library
import random  # Import random library

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound effects
pygame.mixer.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My 8-Bit Platformer")

# Define colors
WHITE = (255, 255, 255)

# Square settings
square_x = 50        # Starting X position of the square
square_y = 50        # Starting Y position of the square
square_size = 50     # Size of the square
square_color = (0, 128, 255)  # Color of the square (RGB format)
speed = 400           # Speed of the square's movement

# Target settings
target_x = 300
target_y = 300
target_size = 30
target_color = (255, 0, 0)  # Red color for the target

# Score variable
score = 0  # Initialize the score to 0
score_display_height = 50  # Height of the score area at the top

# Clock to control the frame rate
clock = pygame.time.Clock()
fps = 60  # Frames per second

# Initialize font
font = pygame.font.Font(None, 36)  # None uses default font, 36 is the size

# Load sound effect and background music
reach_sound = pygame.mixer.Sound('item.wav')  # Load the sound effect
pygame.mixer.music.load('game_music.mp3')  # Load background music

# Set volume levels
pygame.mixer.music.set_volume(0.25)  # Set background music volume to 25%
reach_sound.set_volume(0.7)  # Set sound effect volume to 70%

# Start playing background music
pygame.mixer.music.play(-1)  # -1 means it will loop indefinitely

def show_start_menu():
    while True:
        screen.fill(WHITE)  # Fill the screen with a white background

        # Render the start message
        start_font = pygame.font.Font(None, 74)  # Create a font object
        start_text = start_font.render("Press Spacebar to Start", True, (0, 0, 0))  # Black color
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2 - start_text.get_height() // 2))  # Center the text

        pygame.display.flip()  # Update the display

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                if event.key == pygame.K_SPACE:  # If it's the spacebar
                    return  # Exit the function to start the game

# Game loop
running = True

# Show the start menu before entering the game loop
show_start_menu()

while running:
    # Calculate delta_time (time between frames in seconds)
    delta_time = clock.tick(fps) / 1000.0

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling for movement
    keys = pygame.key.get_pressed()  # Check which keys are pressed
    if keys[pygame.K_a]:          # Move left
        square_x -= speed * delta_time
    if keys[pygame.K_d]:         # Move right
        square_x += speed * delta_time
    if keys[pygame.K_w]:            # Move up
        square_y -= speed * delta_time
    if keys[pygame.K_s]:          # Move down
        square_y += speed * delta_time

    # Ensure the square stays within the screen boundaries and below the score area
    square_x = max(0, min(square_x, screen_width - square_size))
    square_y = max(score_display_height, min(square_y, screen_height - square_size))

    # Fill the screen with a white background
    screen.fill(WHITE)

    # Draw the square on the screen
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Draw the target square
    pygame.draw.rect(screen, target_color, (target_x, target_y, target_size, target_size))

    # Check for collision with the target
    if (square_x < target_x + target_size and
            square_x + square_size > target_x and
            square_y < target_y + target_size and
            square_y + square_size > target_y):
        score += 1  # Increase score by 1
        reach_sound.play()  # Play the sound effect
        target_x = random.randint(0, screen_width - target_size)
        target_y = random.randint(score_display_height, screen_height - target_size)  # Adjust target position

        # Optional: Change target size based on score
        if score > 0 and score % 5 == 0:  # Every 5 points
            target_size = max(10, target_size - 2)  # Reduce size but no smaller than 10

    # Render the score text
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))  # Black color
    screen.blit(score_text, (10, 10))  # Draw score text at position (10, 10)

    # Update the display to show changes
    pygame.display.flip()

# Quit Pygame when the loop ends
pygame.quit()
#TEST CODE
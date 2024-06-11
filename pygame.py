import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spin Wheel")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the wheel sections
sections = ["Prize 1", "Prize 2", "Prize 3", "Prize 4", "Prize 5"]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
angle = 360 / len(sections)

# Draw the wheel
def draw_wheel():
    center = (width // 2, height // 2)
    radius = min(width, height) // 3

    for i in range(len(sections)):
        pygame.draw.arc(screen, colors[i], (center[0] - radius, center[1] - radius, radius * 2, radius * 2),
                        angle * i, angle * (i + 1), radius // 2)

# Spin the wheel
def spin_wheel():
    global spin_start, spin_time, spin_speed, selected_value

    # Randomly select a value
    selected_value = random.choice(sections)

    # Set the initial spin speed and time
    spin_start = pygame.time.get_ticks()
    spin_time = random.randint(2000, 5000)  # Spin for 2-5 seconds
    spin_speed = random.randint(10, 30)  # Spin speed in degrees per second

    # Spin the wheel
    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - spin_start

        if elapsed_time > spin_time:
            # Slow down the spin gradually
            spin_speed -= 0.5
            if spin_speed <= 0:
                break

        # Rotate the wheel
        draw_wheel()
        pygame.display.flip()

    # Display the selected value
    print(f"You won: {selected_value}")

# Main game loop
spin_start = 0
spin_time = 0
spin_speed = 0
selected_value = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spin_wheel()

    screen.fill(WHITE)
    draw_wheel()
    pygame.display.flip()

pygame.quit()

import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spin Wheel")


wheel_image = pygame.image.load("wheel.png")
wheel_rect = wheel_image.get_rect()
wheel_rect.center = (400, 300)  # Center the wheel

sections = ["Prize 1", "Prize 2", "Prize 3", "Prize 4", "Prize 5"]
section_angles = [i * (360 / len(sections)) for i in range(len(sections))]

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

        # Rotate the wheel image
        rotated_wheel = pygame.transform.rotate(wheel_image, spin_speed * elapsed_time / 1000)
        rotated_rect = rotated_wheel.get_rect(center=wheel_rect.center)
        screen.blit(rotated_wheel, rotated_rect)

        pygame.display.flip()

    # Display the selected value
    print(f"You won: {selected_value}")

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

    screen.fill((255, 255, 255))  # Clear the screen
    screen.blit(wheel_image, wheel_rect)  # Draw the wheel
    pygame.display.flip()

pygame.quit()

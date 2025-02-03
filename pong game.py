import pygame

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
paddle_speed = 10

# Ball settings
BALL_SIZE = 20
ball_speed_x = 4
ball_speed_y = 4

# Initialize paddles and ball
left_paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2

# Set up the font for score display
font = pygame.font.SysFont('Arial', 30)

# Score
left_score = 0
right_score = 0

# Main game loop
clock = pygame.time.Clock()

def draw_objects():
    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (20, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Left paddle
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 20 - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Right paddle
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))  # Ball
    
    # Draw the net
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)
    
    # Draw the score
    left_score_text = font.render(f"{left_score}", True, WHITE)
    screen.blit(left_score_text, (SCREEN_WIDTH // 4, 20))
    
    right_score_text = font.render(f"{right_score}", True, WHITE)
    screen.blit(right_score_text, (SCREEN_WIDTH * 3 // 4, 20))

def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, left_score, right_score

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= 20 + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT) or \
       (ball_x >= SCREEN_WIDTH - 20 - PADDLE_WIDTH - BALL_SIZE and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball_x <= 0:
        right_score += 1
        reset_ball()

    if ball_x >= SCREEN_WIDTH - BALL_SIZE:
        left_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
    ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x *= -1
    ball_speed_y = 4

def move_paddles():
    global left_paddle_y, right_paddle_y

    keys = pygame.key.get_pressed()

    # Left paddle movement (W and S)
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += paddle_speed

    # Right paddle movement (Up and Down arrow keys)
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += paddle_speed

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball and paddles
    move_ball()
    move_paddles()

    # Draw the game objects
    draw_objects()

    # Update the display
    pygame.display.flip()

    # Set the game FPS
    clock.tick(FPS)

pygame.quit()

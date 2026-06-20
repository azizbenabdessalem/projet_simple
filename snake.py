import pygame
import random
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame

pygame.init()

#FENETRES
WIDTH = 300
HEIGHT = 600
CELL_SIZE = 20
FPS = 10

#COULEURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#DIRECTIONS
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
RIGHT  = (CELL_SIZE, 0)
LEFT = (-CELL_SIZE,0)





def init_game() :
    snake = [(140,300),(120,300),(100,300)]
    direction = RIGHT
    food = generate_food(snake)
    score = 0
    game_over = False
    return snake,direction,food,score,game_over

def generate_food(snake):
    while True :
        x = random.randrange(0,WIDTH,CELL_SIZE)
        y = random.randrange(0,HEIGHT,CELL_SIZE)
        food = (x,y)
        if food not in snake :
            return food

def handle_game_over_events():
    restart = False
    running = True

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r :
                restart = True
            elif event.key == pygame.K_q :
                running = False
    return restart,running

def handle_events(direction):
    running = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP

            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN

            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT

            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    return direction, running

def draw_game_over(screen, score):
    font_big = pygame.font.Font(None, 60)
    font_small = pygame.font.Font(None, 32)

    text1 = font_big.render("Game Over", True, WHITE)
    text2 = font_small.render(f"Score : {score}", True, WHITE)
    text3 = font_small.render("Appuie sur R pour recommencer", True, WHITE)
    text4 = font_small.render("Appuie sur Q pour quitter", True, WHITE)

    rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
    rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    rect3 = text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    rect4 = text4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))

    screen.blit(text1, rect1)
    screen.blit(text2, rect2)
    screen.blit(text3, rect3)
    screen.blit(text4, rect4)

def move_snake(snake,direction,grow) :
    head_x,head_y = snake[0]
    dx,dy=direction
    new_head = (head_x + dx , head_y + dy)
    snake.insert(0,new_head)
    if not grow :
       snake.pop()
    return snake

def check_food_collision(snake,food) :
    head = snake[0]

    if head == food :
        return True
    elif head != food :
        return False

def check_wall_collision(snake) :
    head_x,head_y = snake[0]
    collision = True

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT :
        collision = True
    else :
        collision = False
    return collision

def check_self_collision(snake) :
    head = snake[0]
    body = snake[1:]

    if head in body :
        return True
    elif head not in body :
        return False

def draw_snake(screen, snake) :

    for position in snake :
        x,y = position

        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)


def draw_food(screen,food) :
    x,y = food
    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)

def draw_score(screen,score):
    font = pygame.font.Font(None, 30)
    text = f"Score : {score}"
    score_surface = font.render(text, True, WHITE)
    screen.blit(score_surface, (10, 10))

def draw_game(screen,snake,food,score) :
    screen.fill((0, 0, 0))
    draw_food(screen,food)
    draw_snake(screen,snake)
    draw_score(screen,score)
    pygame.display.update()


def game_loop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake, direction, food, score, game_over = init_game()

    running = True

    while running:

        if not game_over:
            direction, running = handle_events(direction)

            head_x, head_y = snake[0]
            future_head = (head_x + direction[0], head_y + direction[1])

            if future_head == food:
                grow = True
            else:
                grow = False

            snake = move_snake(snake, direction, grow)

            if grow:
                score += 1
                food = generate_food(snake)

            if check_wall_collision(snake) or check_self_collision(snake):
                game_over = True

        else:
            restart, running = handle_game_over_events()

            if restart:
                snake, direction, food, score, game_over = init_game()

        draw_game(screen, snake, food, score)

        if game_over:
            draw_game_over(screen, score)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    game_loop()





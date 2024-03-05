import pygame
from random import randint

pygame.init()

#init vars
screen_width = 500
screen_height = 500
timer = 0
seconds = 0
x_pos = 10
y_pos = 10
x_dir = 1
y_dir = 0
scale=20
snake_length = 1
apple_num = 0
apple_array = [[0,0],[0,0]]
snake_array = [[10, 10]]
snake_color = (255, 255, 255)

window_size = (screen_width, screen_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snake")

running = True

def die():
    print(snake_length)
    global running
    running = False

while running:
# Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x_dir = 0
                y_dir = -1 
            if event.key == pygame.K_LEFT:
                y_dir = 0
                x_dir = -1
            if event.key == pygame.K_RIGHT:
                y_dir = 0
                x_dir = 1
            if event.key == pygame.K_DOWN:
                x_dir = 0
                y_dir = 1
        if event.type == pygame.QUIT:
            running = False
    
      
   # game loop (tick)
    timer += 1
    if timer%500 == 0:
        seconds+=1

        #MOVEMENT
        y_pos += y_dir
        x_pos += x_dir

        #DEATH
        for i in snake_array:
            if (i == [x_pos, y_pos]):
                snake_color = (255, 0, 0)
                die()
                break
            else:
                snake_color = (255, 255, 255)
    
        if x_pos > 24 or x_pos < 0:
                snake_color = (255, 0, 0)
                die()
        if y_pos > 24 or y_pos < 0:
            snake_color = (255, 0, 0)
            die()


        #SNAKE TICK
        snake_array.append([x_pos, y_pos])


    #BACKGROUND COLOR
    window.fill((0,0,0))

    #APPLES
    if apple_num < 2:
        if apple_array[0][0] == 0 and apple_array[0][1] == 0:
            rand_x = randint(1, scale) 
            rand_y = randint(1, scale)
            apple_array[0][0] = rand_x
            apple_array[0][1] = rand_y
            apple_num += 1
        if apple_array[1][0] == 0 and apple_array[1][1] == 0:
            rand_x = randint(1, scale) 
            rand_y = randint(1, scale)
            apple_array[1][0] = rand_x
            apple_array[1][1] = rand_y
            apple_num += 1
    
    for i in apple_array:
        if i[0] == x_pos and i[1] == y_pos:
            apple_num -= 1
            snake_length += 1
            i[0] = 0
            i[1] = 0

    #OBJECTS
    pygame.draw.rect(window, (255, 255, 255), (scale*apple_array[0][0], scale*apple_array[0][1], scale, scale))
    pygame.draw.rect(window, (255, 255, 255), (scale*apple_array[1][0], scale*apple_array[1][1], scale, scale))

    while len(snake_array) > snake_length:
            snake_array.pop(0)

    for i in snake_array:
        pygame.draw.rect(window, snake_color, (scale*i[0], scale*i[1], scale, scale))
    
    pygame.display.flip()
pygame.quit()
import pygame
import random

pygame.init()

display_width = 1536
display_height = 791

table_size = 4
table_list = []

selected = 1

yellow = (255,255,45)
black = (0,0,0)
white = (255,255,255)

my_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Keys")

end = False

def generate_table(bigght):
    global table_list
    table_list = []
    for i in range(bigght**2):
        table_list.append(random.randint(0,1))

def game_loop():
    global selected
    global table_list
    generate_table(table_size)
    while not end:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame:
                print("left")
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected > table_size:
                    selected -= table_size
                elif event.key == pygame.K_DOWN and selected <= table_size**2 - table_size:
                    selected += table_size
                elif event.key == pygame.K_RIGHT and selected % table_size != 0:
                    selected += 1
                elif event.key == pygame.K_LEFT and selected % table_size != 1:
                    selected -= 1
                elif event.key == pygame.K_SPACE:
                    print("cat")
                    column = (selected - 1) % table_size
                    change_list = []
                    for i in range(selected - column - 1, selected - column + table_size - 1) :
                        change_list.append(i)
                    for i in range(table_size):
                        change_list.append(i*table_size + column)
                    change_list.append(selected - 1)
                    for i in change_list:
                        if table_list[i] == 0:
                            table_list[i] = 1
                        else:
                            table_list[i] = 0

        
        my_display.fill(white)
        
        pygame.draw.rect(my_display,black,(display_width/2-(30*table_size + 5),display_height/2-(30*table_size + 5),(60*table_size + 10),(60*table_size + 10)))
        for a in range(table_size):
            for b in range(table_size):
                if selected == table_size*a + b + 1:
                    pygame.draw.rect(my_display,yellow,(display_width/2-(30*table_size - 5) + 60*b,display_height/2-(30*table_size - 5) + 60*a,50,50))
                else:
                    pygame.draw.rect(my_display,white,(display_width/2-(30*table_size - 5) + 60*b,display_height/2-(30*table_size - 5) + 60*a,50,50))
                if table_list[table_size*a + b] == 0:
                    pygame.draw.rect(my_display,black,(display_width/2-(30*table_size - 5) + 60*b + 10,display_height/2-(30*table_size - 5) + 60*a+20,30,10))
                else: #invalid syntax diyo burda
                    pygame.draw.rect(my_display,black,(display_width/2-(30*table_size - 5) + 60*b + 20,display_height/2-(30*table_size - 5) + 60*a + 10,10,30))
        pygame.display.update()
game_loop()
pygame.quit()
quit()
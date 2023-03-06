# file created by Arthur Dupont
# import libraries 


from time import sleep

from random import randint

import pygame as pg

import os

# set up asset folders - images and sounds
game_folder = os.path.dirname(__file__)
print(game_folder)

user_choice = ""
pc = "x"

# game setting
WIDTH = 1000
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RAIN = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BROWN = (104, 74, 35)
PURPLE = (128,0,128)


# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
clock = pg.time.Clock()

# sound
rock_sound = pg.mixer.Sound(os.path.join(game_folder, 'rock.wav')) 
paper_sound = pg.mixer.Sound(os.path.join(game_folder, 'paper.wav')) 
scissors_sound = pg.mixer.Sound(os.path.join(game_folder, 'scissors.wav')) 
beep_paper_sound = pg.mixer.Sound(os.path.join(game_folder, 'beep_paper.wav')) 
beep_rock_sound = pg.mixer.Sound(os.path.join(game_folder, 'beep_rock.wav')) 
beep_scissors_sound = pg.mixer.Sound(os.path.join(game_folder, 'beep_scissors.wav')) 

# images
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image2 = pg.image.load(os.path.join(game_folder, 'rock 2.png')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
paper_image2 = pg.image.load(os.path.join(game_folder, 'paper2.png')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image2 = pg.image.load(os.path.join(game_folder, 'scissors2.jpg')).convert()
play_again_box = pg.image.load(os.path.join(game_folder, 'play_again.jpg')).convert()

# creates transparency 
rock_image.set_colorkey(WHITE)
rock_image2.set_colorkey(WHITE)
scissors_image.set_colorkey(WHITE)
paper_image.set_colorkey(WHITE)
paper_image2.set_colorkey(WHITE)
scissors_image2.set_colorkey(WHITE)

# text
# sets the font
font = pg.font.SysFont(None,60)
character = font.render('CHOOSE YOUR CHARCTER', True, RED)
player_pick_rock = font.render("YOU CHOSE ROCK", True, WHITE)
player_pick_paper = font.render("YOU CHOSE PAPER", True, WHITE)
player_pick_scissors = font.render("YOU CHOSE SCISSORS", True, WHITE)
pc_rock = font.render("COMPUTER CHOSE ROCK", True, BLUE)
pc_paper = font.render("COMPUTER CHOSE PAPER", True, BLUE)
pc_scissors = font.render("COMPUTER CHOSE SCISSORS", True, BLUE)


# computer picks something
choices = ["rock", "paper", "scissors"]
def pc_choice():
    return choices[randint(0,2)]

# in progress
def pc_roc():
    pg.mixer.Sound.play(beep_rock_sound)





# gets the geometry of the image
rock_rect = rock_image.get_rect()
rock_rect2 = rock_image2.get_rect()
paper_rect = paper_image.get_rect()
paper_rect2 = paper_image2.get_rect()
scissors_rect = scissors_image.get_rect()
scissors_rect2 = scissors_image2.get_rect()
play_again_rect = play_again_box.get_rect()



# sets the first location of the image
paper_rect.x = WIDTH/2.75
scissors_rect.x = WIDTH/1.35
rock_rect2.x = WIDTH/1.35
scissors_rect2.x = WIDTH/1.35
paper_rect2.x = WIDTH/1.35
play_again_rect.x = WIDTH/2.75

# allows the loop to run
running = True
# shows player image 
rock = True 
paper = True
scissors = True
# shows pc image 
rock_2 = False
scissors_2 = False
paper_2 = False
# makes it so that you can only choose one option
made_choice = False
play_again = False


# cpu_rock = True
# cpu_paper = True
# cpu_scissors = True
while running:
    clock.tick(FPS)
    # rainbow thing  
    RAINBOW = (randint(0,255), randint(0,255), randint(0,255))
    # results
    lose = font.render("YOU LOSE", True, RED)
    win = font.render("YOU WIN", True, RAINBOW)
    tie = font.render("ITS A TIE", True, BROWN)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # if i press the x button the loop ends
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
            # gets the coords of the mouse
            mouse_coords = pg.mouse.get_pos()
            # only allows you to pick an option if made_choice is false
            if made_choice == False:
                # what happens if i click on the rock image
                if rock_rect.collidepoint(mouse_coords):
                    # says that user choice is rock
                    user_choice = "rock"
                    print("rock time")
                    # plays a the rock sound 
                    pg.mixer.Sound.play(rock_sound)
                    # removes the ability to choose other images
                    made_choice = True 
                    # defines pc so that it only picks one thing instead of every time
                    pc = pc_choice() 
                       
                        
                                
                elif paper_rect.collidepoint(mouse_coords):
                    user_choice = "paper"
                    print("paper time")
                    pg.mixer.Sound.play(paper_sound)
                    made_choice = True 
                    pc = pc_choice()  
                    
                    
                elif scissors_rect.collidepoint(mouse_coords):
                    user_choice = "scissors"
                    print("scissors time")
                    pg.mixer.Sound.play(scissors_sound)
                    made_choice = True   
                    pc = pc_choice()  
            # if play_again == True:
            #     if play_again_rect.collidepoint(mouse_coords):
            #         print("dsghsljdg")
            #         user_choice = ""
            #         pc = "x"
            #         made_choice = False
    

                

                

            # if mouse_coords[0] <= 246 and  mouse_coords[1] <= 175:
            # print("rock time")
    # get imput from player...

    # update
    # move the rock 
    # rock_rect.x += 1 
    # paper_rect.y += 1
    # scissors_rect.y += 2
    # scissors_rect.x += 1


    # draw
    # background is blakc
    screen.fill(BLACK)
    #  gets the player options and geometry
    if rock == True:
        screen.blit(rock_image, rock_rect)
    if paper == True:
        screen.blit(paper_image, paper_rect)
    if scissors == True:
        screen.blit(scissors_image, scissors_rect)
    # shows the character text
    screen.blit(character, (200, 400))
    # gets the pc images
    if rock_2 == True:
        screen.blit(rock_image2, rock_rect2)
    if scissors_2 == True:
        screen.blit(scissors_image2, scissors_rect2)
    if paper_2 == True:
        screen.blit(paper_image2, paper_rect2)
    if play_again == True:
        screen.blit(play_again_box, play_again_rect)
    # if cpu_rock == True:
    #     screen.blit(pc_rock, (0, 500))
    # if cpu_paper == True:
    #     screen.blit(pc_paper, (0, 500))
    # if cpu_scissors == True:
    #     screen.blit(pc_scissors, (0, 500))
# person choice
    # what happens when user choice is rock
    if user_choice == "rock":
        # makes the rock geometry shown while the other geometry is no longer shown 
        rock = True
        scissors  = False
        paper = False
        # makes the character text not exist anymore
        character = font.render('', True, BLACK)
        # shows text that says teh player picked rock
        screen.blit(player_pick_rock, (300, 400))
        # moves the geometry and image to a certian point 
        if rock_rect.y < 200:
            rock_rect.y += 5 
                 

    if user_choice == "paper":
        paper = True
        scissors = False
        rock = False
        character = font.render('', True, BLACK)
        screen.blit(player_pick_paper, (300, 400))

        if paper_rect.y < 200:
            paper_rect.y += 2.999999999999998 
        if paper_rect.x > 0:
            paper_rect.x -= 5
    
    if user_choice == "scissors":
        scissors = True
        rock = False
        paper = False
        character = font.render('', True, BLACK)
        screen.blit(player_pick_scissors, (250, 400))
        if scissors_rect.y < 250:
            scissors_rect.y += 3
        if scissors_rect.x > 0:
            scissors_rect.x -= 11

# game 
    
    # game thing now
    if user_choice == pc:
        screen.blit(tie, (400,200))
        # play_again = True
    elif user_choice == "scissors":
        if pc == "paper":
            screen.blit(win, (400,200)) 
            # play_again = True          
        if pc == "rock":
            screen.blit(lose, (400,200))
            # play_again = True
    
    elif user_choice == "rock":
        if pc == "scissors":
            screen.blit(win, (400,200))
            # play_again = True
        if pc == "paper":
            screen.blit(lose, (400,200))
            # play_again = True

    
    elif user_choice == "paper":
        if pc == "rock":
            screen.blit(win, (400,200))
            # play_again = True
        if pc == "scissors":
            screen.blit(lose, (400,200))
            # play_again = True

    

    
    

# computer choice
    # what happens when the computer chooses
    if pc == "rock":
        # shows the text  that says "computer chose rock"
        screen.blit(pc_rock, (200, 500))
        # only shows the pc rock geometry 
        rock_2 = True
        paper_2 = False
        scissors_2 = False
        # moves the image to my desired location
        if rock_rect2.y < 200:
            rock_rect2.y += 5
        if rock_rect2.x < 700:
            rock_rect2.x = 5
        
    if pc == "paper":
        paper_2 = True
        rock_2 = False
        scissors_2 = False
        screen.blit(pc_paper, (200, 500))
        if paper_rect2.y < 200:
            paper_rect2.y += 5
        if paper_rect2.x < 700:
            paper_rect2.x = 5
    
    if pc == "scissors":
        scissors_2 = True
        paper_2 = False
        rock_2 = False
        screen.blit(pc_scissors, (200, 500))
        if scissors_rect2.y < 200:
            scissors_rect2.y += 5
        if scissors_rect2.x < 700:
            scissors_rect2.x = 5
    
    


    

    pg.display.flip()
    
pg.quit()

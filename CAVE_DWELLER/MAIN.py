####################
## Kelly Norris
##
## December 2016 Semester 1
##
## CAVE DWELLER EX Main File
####################

#Importing libraries
import pygame
import random
import time

#import supporting classes
from Rooms import *
from Menu import *
from Player import *
from Battle import *
#making instances of supporting classes
rooms = Rooms()
menu = Menu()
player = Player()
battle = Battle()
enemy = Enemy()



#initialize pygame
pygame.init()
#creating font vars
font = pygame.font.SysFont('adobehebrew', 12)
font = pygame.font.Font('AdobeArabic-Regular.otf', 50)
roomFont = pygame.font.Font('AdobeArabic-Regular.otf', 30)
#get music
pygame.mixer.music.load('audio/Undertale OST- 031 - Waterfall.mp3')
pygame.mixer.music.play(loops=-1)

#Create window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window Title goes here")



##making main loop variables:

#done for loop
done = False
#clock for screen updates
clock = pygame.time.Clock()

#Other variables for looping:
cursor_position = 'topLeft'
current_menu = "main"
game_over = False
startup = True
menu_wait = False
z_wait = False

#Declare colors for draws
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

#Lock vars
lock1 = True
lock2 = True
key1 = False
key2 = False
#First Visit vars
room0_first = True
room1_first = True
room2_first = True
room7_first = True
room8_first = True
room9_first = True
room10_first = True
#Room images
roomimage_list = []
roomimage0 = pygame.image.load("img/room0.png").convert()
roomimage_list.append(roomimage0)
roomimage1 = pygame.image.load("img/room1.png").convert()
roomimage_list.append(roomimage1)
roomimage2 = pygame.image.load("img/room2.png").convert()
roomimage_list.append(roomimage2)
roomimage3 = pygame.image.load("img/room3.png").convert()
roomimage_list.append(roomimage3)
roomimage4 = pygame.image.load("img/room4.png").convert()
roomimage_list.append(roomimage4)
roomimage5 = pygame.image.load("img/room5.png").convert()
roomimage_list.append(roomimage5)
roomimage6 = pygame.image.load("img/room6.png").convert()
roomimage_list.append(roomimage6)
roomimage7 = pygame.image.load("img/room7.png").convert()
roomimage_list.append(roomimage7)
roomimage8 = pygame.image.load("img/room8.png").convert()
roomimage_list.append(roomimage8)
roomimage9 = pygame.image.load("img/room9.png").convert()
roomimage_list.append(roomimage9)
roomimage10 = pygame.image.load("img/room10.png").convert()
roomimage_list.append(roomimage10)

#####################
#Initialization done#
#####################

#-----Main Loop-----#
while not done:
    #Big 'ol Event Loop
    #First checks if the game is being quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Checking for keydown event
        #This loop is massive, be warned
        elif event.type == pygame.KEYDOWN:
            #Checking for startup/help window, pressing C makes it leave
            if startup == True:
                if event.key == pygame.K_c:
                    startup = False
            
            ###Main Menu logic
            if current_menu == "main":
                #top left - 'player' text
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'player'
                        cursor_position = 'topLeft'
                        menu_wait = True
                        
                #bottom left - 'move' text
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'move'
                        menu_wait = True

                #top right - 'interact' text
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RETURN:
                        rooms.interact = True

                        
            ###Move menu logic
            if current_menu == 'move':
                #backspace, to main menu
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'main'
                    cursor_position = 'topLeft'
                    
                #top left - 'north' text
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 'n'

                #bottom left - 'south' text
                #Uses the menu_wait var, which prevents going from the main menu into the move menu and still having the 'return' key active and pressing 'south'
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'botRight'
                    if menu_wait == False:
                        if event.key == pygame.K_RETURN:
                            rooms.go = 's'

                #top right - 'east' text
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botRight'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 'e'
                        
                #bottom right - 'west' text
                if cursor_position == 'botRight':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 'w'
                       
                        
            ###Player menu logic
            if current_menu == 'player':
                #backspace, goes to main menu
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'main'
                    cursor_position = 'topLeft'

                #top left - 'items' text
                #Uses the menu_wait var, which prevents going from the main menu into the player menu and still having the 'return' key active and pressing 'items'
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botLeft'
                    if menu_wait == False:
                        if event.key == pygame.K_RETURN:
                            current_menu = 'items'

                #top right - 'stats' text
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botRight'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'stats'

                #bottom left - 'keys' text
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'botRight'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'keys'
                        cursor_position = 'topLeft'

                #bottom right - 'help' text
                if cursor_position == 'botRight':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RETURN:
                        startup = True


            ###Items menu logic
            if current_menu == 'items':
                #backspace, goes to player menu
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'player'

                #top left - weapon text
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'

                #top right - health potion
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    #if a healing potion is there, the player can press z to use it
                    if event.key == pygame.K_z and player.items[2] == 'Healing Potion':
                        player.items[2] = ''
                        player.hp += 20

                #bottom left - health potion
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    #if a healing potion is there, the player can press z to use it
                    if event.key == pygame.K_z and player.items[1] == 'Healing Potion':
                        player.items[1] = ''
                        player.hp += 20


            ###Stats menu logic
            if current_menu == 'stats':
                #reset cursor to not go to blank space
                cursor_position = 'topLeft'
                #backspace, goes to player menu
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'player'

            ###Keys menu logic
            if current_menu == 'keys':
                #reset cursor to not go to blank space
                cursor_position = 'topLeft'
                #backspace, goes to player menu
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'player'
                
            
            ###Battle text logic
            #battle start screen
            if battle.beginBattlePhase == True:
                if event.key == pygame.K_z:
                    battle.battle = True
                    battle.beginBattlePhase = False
                    cursor_position = 'topLeft'
                    current_menu = 'battle'
                    battle.turn = 'shadow_realm'
                    battle.battleEvent = 'spawn'
                    z_wait = True

            #battle defeat monster end
            if battle.battleEvent == 'end':
                battle.battleEvent = ''
                battle.battle = False
                battle.turn = 'shadow_realm'
                cursor_position = 'shadow_realm'
                #dismissing battle end text and going back to room
                if event.key == pygame.K_z:
                    rooms.current_room = rooms.current_roomGhost
                    current_roomGhost = 1004
                    current_menu = 'main'
                    rooms.text = True
                    cursor_position = 'topLeft'
                    battle.endBattlePhase = False

            #battle 'enemy has appeared' text dismissal
            if battle.battleEvent == 'spawn':
                if z_wait == False:
                    if event.key == pygame.K_z:
                        battle.battleEvent = ''
                        battle.turn = 'player'

            #battle 'enemy has attacked' text dismissal
            if battle.battleEvent == 'enemyAttack':
                if event.key == pygame.K_z:
                    battle.battleEvent = ''
                    battle.event_text1 = ''
                    battle.turn = 'player'

            #battle 'you attack' text dismissal
            if battle.battleEvent == 'player_attack':
                if event.key == pygame.K_z:
                    battle.battleEvent = ''
                    battle.turn = 'enemy'
                    battle.event_text1 = ''
                    battle.event_text2 = ''

            

            ###Battle menu logic
            if battle.turn == 'player':
                ##Main battle menu
                if current_menu == 'battle':
                    #top left - 'attack' text
                    if cursor_position == 'topLeft':
                        if event.key == pygame.K_RIGHT:
                            cursor_position = 'topRight'
                        if event.key == pygame.K_DOWN:
                            cursor_position = 'botLeft'
                        if event.key == pygame.K_RETURN:
                            battle.attack = True

                    #bottom left - 'items' text
                    #uses menu_wait var to prevent using a health potion on the same loop as going into the menu
                    if cursor_position == 'botLeft':
                        if event.key == pygame.K_UP:
                            cursor_position = 'topLeft'
                        if event.key == pygame.K_RETURN:
                            current_menu = 'battle_items'
                            cursor_position = 'topLeft'
                            menu_wait = True

                    #top right - 'flee' text
                    if cursor_position == 'topRight':
                        if event.key == pygame.K_LEFT:
                            cursor_position = 'topLeft'
                        if event.key == pygame.K_RETURN:
                            battle.flee = True

                ##Battle items menu
                #uses menu_wait
                if current_menu == 'battle_items':
                    #backspace, goes to battle main menu
                    if event.key == pygame.K_BACKSPACE:
                        current_menu = 'battle'
                    if menu_wait == False:
                        #top left - healing potion 
                        if cursor_position == 'topLeft':
                            if event.key == pygame.K_DOWN:
                                cursor_position ='botLeft'
                            #using healing potion
                            if event.key == pygame.K_RETURN and player.items[1] == 'Healing Potion':
                                player.items[1] = ''
                                player.hp += 20
                                
                    #bottom left - healing potion
                    if cursor_position == 'botLeft':
                        if event.key == pygame.K_UP:
                            cursor_position = 'topLeft'
                        if event.key == pygame.K_RETURN and player.items[2] == 'Healing Potion':
                            player.items[2] = ''
                            player.hp += 20
                            
        
            #Text dismissal logic
            if event.key == pygame.K_z:
                if rooms.text == True and rooms.event == False:
                    rooms.text = False
                if rooms.text == True and rooms.event == True:
                    rooms.event = False
                if rooms.text == False and rooms.event == True:
                    rooms.event = False
                    
            
    #Game logic goes here
    #Direction checkers for moving between rooms
    rooms.checkDirection()
    rooms.setDirection()
    #Battle encounter 1
    if rooms.current_room == 1 and room1_first == True:
        battle.enemy = 1
        battle.beginBattlePhase = True
        rooms.current_roomGhost = rooms.current_room
        rooms.current_room = 1004
        enemy.statgen(5, ['Claw', 2], ['Bite', 2])
        room1_first = False
        
    #Battle encounter 2
    if rooms.current_room == 7 and room7_first == True:
        battle.enemy = 2
        battle.beginBattlePhase = True
        rooms.current_roomGhost = rooms.current_room
        rooms.current_room = 1004
        enemy.statgen(15, ['Bite', 3], ['Claw', 4])
        room7_first = False
        
    #Final battle
    if rooms.current_room == 10 and room10_first == True:
        battle.enemy = 3
        battle.beginBattlePhase = True
        rooms.current_roomGhost = rooms.current_room
        rooms.current_room = 1004
        enemy.statgen(30, ['Death Scythe', 5], ['Death Beam', 10])

    #Battle enemy turn
    if battle.turn == 'enemy':
        if enemy.hp <= 0:
            battle.battleEvent = 'end'
            battle.endBattlePhase = True

        #rolling for which attack enemy uses
        roll = random.randint(1,2)
        if battle.battleEvent != 'end':
            if roll == 1:
                battle.battleEvent = 'enemyAttack'
                player.hp -= enemy.attacks[0][1]
                battle.turn = 'shadow_realm'
            if roll == 2:
                battle.battleEvent = 'enemyAttack'
                player.hp -= enemy.attacks[1][1]
                battle.turn = 'shadow_realm'
            
        
    ##Checking for locked doors and their keys
    #Lock 1 - room 3
    if rooms.current_room == 3 and lock1 == True and key1 == True:
        lock1 = False
        rooms.event = True
        rooms.eventType = 'UNLOCK'
    if rooms.current_room == 3 and lock1 == True and key1 == False:
        rooms.current_room = 2
        rooms.event = True
        rooms.text = False
        rooms.eventType = 'LOCK'

    #Lock 2 - room 10
    if rooms.current_room == 10 and lock2 == True and key2 == True:
        lock2 = False
        menu.drawEventBox(screen)
        rooms.event = True
        rooms.eventType = 'UNLOCK'
    if rooms.current_room == 10 and lock2 == True and key2 == False:
        rooms.current_room = 7
        rooms.event = True
        rooms.text = False
        rooms.eventType = 'LOCK'


    ##Checking for first visit events
    #room 2
    if rooms.current_room == 2 and room2_first == True:
        room0_first = False
        rooms.event = True
        rooms.eventType = '2_FIRST'
        room2_first = False
    #room 9
    if rooms.current_room == 9 and room9_first == True:
        room9_first = False
        room8_first = False
        rooms.event = True
        rooms.eventType = '9_FIRST'


    ##Interactions
    if rooms.interact == True:
        #room 1
        if rooms.current_room == 0 and room0_first == False:
            rooms.event = True
            rooms.eventType = '0_FIRST'
            key1 = True
            rooms.interact = False
        #room 8
        if rooms.current_room == 8 and room8_first == False:
            rooms.event = True
            rooms.eventType = '8_FIRST'
            key2 = True
        if rooms.event == False:
            rooms.event = True
            rooms.eventType = 'None'

    
    
    

    ###Drawing things on screen
    
    #clear screen
    screen.fill(BLACK)

    ##Exploration Phase Draws
    #Drawing room
    if battle.battle == False and battle.beginBattlePhase == False and battle.endBattlePhase == False:
        screen.blit(roomimage_list[rooms.current_room], [0, 0])
        pygame.draw.rect(screen, BLACK, [50, 350, 600, 125], 0)
        menu.drawMenuBox(screen, WHITE)

    #Room text draws
    if rooms.text == True and battle.battle == False and battle.beginBattlePhase == False:
        menu.drawTextBox(screen, WHITE)
        menu.drawRoomText(screen, roomFont, WHITE, rooms.current_room)

    #Event draws
    if rooms.event == True and battle.battle == False:
        menu.drawEventBox(screen)
        rooms.eventText = True
        if rooms.eventType == 'LOCK':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventLock)
        if rooms.eventType == 'UNLOCK':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventUnlock)
        if rooms.eventType == '2_FIRST':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventCaveHall)
        if rooms.eventType == '0_FIRST':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventHouse)
        if rooms.eventType == '9_FIRST':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventLibrary)
        if rooms.eventType == '8_FIRST':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventWashroom)
        if rooms.eventType == 'None':
            menu.drawEventText(screen, roomFont, WHITE, rooms.eventNone)
        
   
    #Menu text draws
    if current_menu == 'main':
        menu.drawMenuText(screen, font, WHITE)
    elif current_menu == 'move':
        menu.drawMoveMenuText(screen, font, WHITE)
    elif current_menu == 'player':
        menu.drawPlayerMenuText(screen, font, WHITE)
    elif current_menu == 'items':
        menu.drawItemsPlayerMenuText(screen, font, WHITE)
    elif current_menu == 'keys':
        menu.drawKeysPlayerMenuText(screen, font, WHITE, key1, key2)
    elif current_menu == 'stats':
        menu.drawStatsPlayerMenuText(screen, font, WHITE, player)
    elif current_menu == 'battle':
        battle.drawBattleMainText(screen, WHITE, font)
    elif current_menu == 'battle_items':
        battle.drawBattleItemText(screen, WHITE, font, player)

    
    ##Battle Phase Draws
    #Battle begin image
    if battle.beginBattlePhase == True:
        battle.beginBattle(screen, WHITE, font)
        current_menu = 'shadow_realm'
        cursor_position = 'shadow_realm'

    #Battle normal menu
    if battle.battle == True:
        battle.drawBattleBox(screen, WHITE)
        battle.drawStats(screen, roomFont, WHITE, enemy, player)
        battle.drawEnemy(screen)
        
        if battle.attack == True:
            battle.rollPlayerAttack(player.equip, enemy)
            battle.turn = 'shadow_realm'
        if battle.battleEvent == 'spawn':
            battle.event_text1 = 'An enemy has appeared!'
            battle.drawBattleEventText(screen, WHITE, roomFont)
        if battle.battleEvent == 'enemyAttack':
            battle.event_text1 = 'The enemy attacks!'
            battle.drawBattleEventText(screen, WHITE, roomFont)
        if battle.battleEvent == 'player_attack':
            battle.drawBattleEventText(screen, WHITE, roomFont)


    #Battle end image
    if battle.battleEvent == 'end':
        battle.endBattle(screen, WHITE, font)
    #Returning cursor after end battle screen
    if battle.endBattlePhase == False:
        menu.drawMenuCursorSimple(cursor_position, screen, WHITE)
    
    
    ##Help Screen
    if startup == True:
        pygame.draw.rect(screen, BLACK, [0, 0, 700, 500], 0)
        text1 = roomFont.render('Welcome to Cave Dweller.', True, WHITE)
        text2 = roomFont.render('Use the arrow keys, enter, and backspace', True, WHITE)
        text3 = roomFont.render('to navigate the menu.', True, WHITE)
        text4 = roomFont.render('Sometimes, other text appears.', True, WHITE)
        text5 = roomFont.render('Press X to dismiss event text,', True, WHITE)
        text6 = roomFont.render('and Z to dismiss other text.', True, WHITE)
        text7 = roomFont.render('Also press Z to use healing potions.', True, WHITE)
        text8 = roomFont.render('Press C to exit this help window.', True, WHITE)
        screen.blit(text1, [20, 20])
        screen.blit(text2, [20, 40])
        screen.blit(text3, [20, 60])
        screen.blit(text4, [20, 80])
        screen.blit(text5, [20, 100])
        screen.blit(text6, [20, 120])
        screen.blit(text7, [20, 140])
        screen.blit(text8, [20, 160])
    
    ##Game Over Screen
    if player.hp <= 0:
        game_over = True
    if game_over == True:
        pygame.draw.rect(screen, BLACK,[0,0, 700,500], 0)
        text1 = font.render('GAME', True, WHITE)
        text2 = font.render('OVER', True, WHITE)
        renderText1 = screen.blit(text1, [300, 200])
        renderText2 = screen.blit(text2, [310, 240])
    
    
    #Make sure draws go on screen
    pygame.display.flip()

    #set frames per second
    clock.tick(60)

    #mop up variables
    rooms.interact = False
    menu_wait = False
    z_wait = False
    if player.items[1] == '' and player.items[2] == '' and player.items[3] == '':
        player.items[1] = '(Nothing)'
    
    
#when loop is done, close window
pygame.quit()


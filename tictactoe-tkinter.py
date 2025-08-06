



# __/\\\\\\\\\\\\\\\__/\\\\\\\\\\\________/\\\\\\\\\_            
#  _\///////\\\/////__\/////\\\///______/\\\////////__           
#   _______\/\\\___________\/\\\_______/\\\/___________          
#    _______\/\\\___________\/\\\______/\\\_____________         
#     _______\/\\\___________\/\\\_____\/\\\_____________        
#      _______\/\\\___________\/\\\_____\//\\\____________       
#       _______\/\\\___________\/\\\______\///\\\__________      
#        _______\/\\\________/\\\\\\\\\\\____\////\\\\\\\\\_     
#         _______\///________\///////////________\/////////__    





# __/\\\\\\\\\\\\\\\_____/\\\\\\\\\___________/\\\\\\\\\_        
#  _\///////\\\/////____/\\\\\\\\\\\\\______/\\\////////__       
#   _______\/\\\________/\\\/////////\\\___/\\\/___________      
#    _______\/\\\_______\/\\\_______\/\\\__/\\\_____________     
#     _______\/\\\_______\/\\\\\\\\\\\\\\\_\/\\\_____________    
#      _______\/\\\_______\/\\\/////////\\\_\//\\\____________   
#       _______\/\\\_______\/\\\_______\/\\\__\///\\\__________  
#        _______\/\\\_______\/\\\_______\/\\\____\////\\\\\\\\\_ 
#         _______\///________\///________\///________\/////////__





# __/\\\\\\\\\\\\\\\_______/\\\\\_______/\\\\\\\\\\\\\\\_        
#  _\///////\\\/////______/\\\///\\\____\/\\\///////////__       
#   _______\/\\\_________/\\\/__\///\\\__\/\\\_____________      
#    _______\/\\\________/\\\______\//\\\_\/\\\\\\\\\\\_____     
#     _______\/\\\_______\/\\\_______\/\\\_\/\\\///////______    
#      _______\/\\\_______\//\\\______/\\\__\/\\\_____________   
#       _______\/\\\________\///\\\__/\\\____\/\\\_____________  
#        _______\/\\\__________\///\\\\\/_____\/\\\\\\\\\\\\\\\_ 
#         _______\///_____________\/////_______\///////////////__









###############################################################################################################################################################

















# __/\\\\\\\\\\\__/\\\\____________/\\\\__/\\\\\\\\\\\\\_________/\\\\\_________/\\\\\\\\\______/\\\\\\\\\\\\\\\_        
#  _\/////\\\///__\/\\\\\\________/\\\\\\_\/\\\/////////\\\_____/\\\///\\\_____/\\\///////\\\___\///////\\\/////__       
#   _____\/\\\_____\/\\\//\\\____/\\\//\\\_\/\\\_______\/\\\___/\\\/__\///\\\__\/\\\_____\/\\\_________\/\\\_______      
#    _____\/\\\_____\/\\\\///\\\/\\\/_\/\\\_\/\\\\\\\\\\\\\/___/\\\______\//\\\_\/\\\\\\\\\\\/__________\/\\\_______     
#     _____\/\\\_____\/\\\__\///\\\/___\/\\\_\/\\\/////////____\/\\\_______\/\\\_\/\\\//////\\\__________\/\\\_______    
#      _____\/\\\_____\/\\\____\///_____\/\\\_\/\\\_____________\//\\\______/\\\__\/\\\____\//\\\_________\/\\\_______   
#       _____\/\\\_____\/\\\_____________\/\\\_\/\\\______________\///\\\__/\\\____\/\\\_____\//\\\________\/\\\_______  
#        __/\\\\\\\\\\\_\/\\\_____________\/\\\_\/\\\________________\///\\\\\/_____\/\\\______\//\\\_______\/\\\_______ 
#         _\///////////__\///______________\///__\///___________________\/////_______\///________\///________\///________


# - Import tkinter here which is a commonly used library for 
#       developing GUI in Python
from tkinter import *

# - Import random so that we choose a player at 
#       random to start after calling a new game(new_game()) 
import random








# __/\\\\\_____/\\\__/\\\\\\\\\\\\\\\__/\\\_______/\\\__/\\\\\\\\\\\\\\\_                                              
#  _\/\\\\\\___\/\\\_\/\\\///////////__\///\\\___/\\\/__\///////\\\/////__                                             
#   _\/\\\/\\\__\/\\\_\/\\\_______________\///\\\\\\/__________\/\\\_______                                            
#    _\/\\\//\\\_\/\\\_\/\\\\\\\\\\\_________\//\\\\____________\/\\\_______                                           
#     _\/\\\\//\\\\/\\\_\/\\\///////___________\/\\\\____________\/\\\_______                                          
#      _\/\\\_\//\\\/\\\_\/\\\__________________/\\\\\\___________\/\\\_______                                         
#       _\/\\\__\//\\\\\\_\/\\\________________/\\\////\\\_________\/\\\_______                                        
#        _\/\\\___\//\\\\\_\/\\\\\\\\\\\\\\\__/\\\/___\///\\\_______\/\\\_______                                       
#         _\///_____\/////__\///////////////__\///_______\///________\///________                                      
# __/\\\\\\\\\\\\\____/\\\_________________/\\\\\\\\\_____/\\\________/\\\__/\\\\\\\\\\\\\\\____/\\\\\\\\\_____        
#  _\/\\\/////////\\\_\/\\\_______________/\\\\\\\\\\\\\__\///\\\____/\\\/__\/\\\///////////___/\\\///////\\\___       
#   _\/\\\_______\/\\\_\/\\\______________/\\\/////////\\\___\///\\\/\\\/____\/\\\_____________\/\\\_____\/\\\___      
#    _\/\\\\\\\\\\\\\/__\/\\\_____________\/\\\_______\/\\\_____\///\\\/______\/\\\\\\\\\\\_____\/\\\\\\\\\\\/____     
#     _\/\\\/////////____\/\\\_____________\/\\\\\\\\\\\\\\\_______\/\\\_______\/\\\///////______\/\\\//////\\\____    
#      _\/\\\_____________\/\\\_____________\/\\\/////////\\\_______\/\\\_______\/\\\_____________\/\\\____\//\\\___   
#       _\/\\\_____________\/\\\_____________\/\\\_______\/\\\_______\/\\\_______\/\\\_____________\/\\\_____\//\\\__  
#        _\/\\\_____________\/\\\\\\\\\\\\\\\_\/\\\_______\/\\\_______\/\\\_______\/\\\\\\\\\\\\\\\_\/\\\______\//\\\_ 
#         _\///______________\///////////////__\///________\///________\///________\///////////////__\///________\///__
# __/\\\\\\\\\\\\\\\__/\\\________/\\\____/\\\\\\\\\______/\\\\\_____/\\\_                                             
#  _\///////\\\/////__\/\\\_______\/\\\__/\\\///////\\\___\/\\\\\\___\/\\\_                                            
#   _______\/\\\_______\/\\\_______\/\\\_\/\\\_____\/\\\___\/\\\/\\\__\/\\\_                                           
#    _______\/\\\_______\/\\\_______\/\\\_\/\\\\\\\\\\\/____\/\\\//\\\_\/\\\_                                          
#     _______\/\\\_______\/\\\_______\/\\\_\/\\\//////\\\____\/\\\\//\\\\/\\\_                                         
#      _______\/\\\_______\/\\\_______\/\\\_\/\\\____\//\\\___\/\\\_\//\\\/\\\_                                        
#       _______\/\\\_______\//\\\______/\\\__\/\\\_____\//\\\__\/\\\__\//\\\\\\_                                       
#        _______\/\\\________\///\\\\\\\\\/___\/\\\______\//\\\_\/\\\___\//\\\\\_                                      
#         _______\///___________\/////////_____\///________\///__\///_____\/////__



# - Upon every 'buttons[row][column]' click this function 
#       will be called to change to player '1' or '2'
# The parameters of this function take in row and column
def next_turn(row, column):

    # - We would like access to our 'player' in the entire 
    #       program to be used, so we will set it to 'global' 
    global player

    # - Here we will check if the button that we click on is empty
    # - If the text of our button that we click is equal to empty, and, check_winner() 
    #       is false, then, we will fill the current players symbol with it
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        # if the 'player' equals the first item in the list 'players' or aka player[0] then ...
        if player == players[0]:
            
            # This line will fill that button with the first players symbol if the condition is satisfied in the previous line
            buttons[row][column]['text'] = player

            # If there is no winner yet then..
            if check_winner() is False:
                
                # - We will assign the new player after we have filled the previous players 
                #       symbol into the button the player clicked
                # - In other words, this will tell the program that the next player is now 
                #       ready to make a move
                player = players[1]
                
                # - We justify that the next player's turn is ready by using the config() function 
                #       to modify the 'label' variable containing the text that tells the players 
                #           whose turn it is
                label.config(text=(players[1]+" turn"))

            # - This 'else if' condition will return a 
            #       Boolean value that will tell us if it has calculated a winner
            # - If there is a winner, then, we will modify the 'label' by use of the 
            #       config() functionality 
            # - And, meanwhile the check_winner() function will automatically highlight 
            #       the buttons in green that calculated the winner and end the game if there is a winner
            elif check_winner() is True:
                
                # - If the winner is found, then, modify the 'label' 
                #       by changing the text from 'players[n] turn' to 'players[n] wins'
                label.config(text=(players[0]+" wins"))

            # - This 'else if' condition will check if the check_winner() 
            #       function returned 'Tie'
            # - If a 'Tie' was returned, then, the 'label' will be modified by the 
            #       config() functionality
            # - In addition, the check_winner() function will highlight the entire 
            #       gameboard in yellow to indicate a tie
            elif check_winner() == "Tie":
                
                # - If check_winner() returns a 'Tie', then, we modify 'label' at the 
                #       top of our game window to say 'Tie!' instead of 'players[n] turn' 
                label.config(text="Tie!")

        # If all other 'else if' conditions are not satisfied then fire this code block ...
        else:
            
            # We will use this line to fill in the button with the symbol of the last player
            buttons[row][column]['text'] = player

            # Then we will check if the check_winner() function returned a winner
            if check_winner() is False:
                
                # - If no winner is returned then this line of code will 
                #       tell the program that it is the next players turn because 
                #           no winner was dediced
                player = players[0]
                
                # - Since no winner was found we also modify the 'label' with 
                #       the config() functionality to name the next players turn at 
                #           the top of the window
                label.config(text=(players[0]+" turn"))

            # - If the check_winner() function does return a Boolean value of True then 
            #       it wont be the next players turn and a winner is decided by modifying the 
            #           'label' with the config() functionality while the check_winner() function 
            #               highlights the winning path
            elif check_winner() is True:
                
                # - We modify the 'label' here with the config() functionality 
                #       from 'players[n] turn' to 'players[n] wins'
                label.config(text=(players[1]+" wins"))

            # - If the check_winner() function returns a 'Tie' then it will 
            #       highlight the entire game board in yellow and modify the 
            #           'label' with the config() functionality from 'players[n] turn' to 'Tie!'
            elif check_winner() == "Tie":
                label.config(text="Tie!")









# ________/\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\\\\\________/\\\\\\\\\__/\\\________/\\\_                          
#  _____/\\\////////__\/\\\_______\/\\\_\/\\\///////////______/\\\////////__\/\\\_____/\\\//__                         
#   ___/\\\/___________\/\\\_______\/\\\_\/\\\_______________/\\\/___________\/\\\__/\\\//_____                        
#    __/\\\_____________\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\______/\\\_____________\/\\\\\\//\\\_____                       
#     _\/\\\_____________\/\\\/////////\\\_\/\\\///////______\/\\\_____________\/\\\//_\//\\\____                      
#      _\//\\\____________\/\\\_______\/\\\_\/\\\_____________\//\\\____________\/\\\____\//\\\___                     
#       __\///\\\__________\/\\\_______\/\\\_\/\\\______________\///\\\__________\/\\\_____\//\\\__                    
#        ____\////\\\\\\\\\_\/\\\_______\/\\\_\/\\\\\\\\\\\\\\\____\////\\\\\\\\\_\/\\\______\//\\\_                   
#         _______\/////////__\///________\///__\///////////////________\/////////__\///________\///__                  
# __/\\\\\\\\\\\\\\\_______/\\\\\_________/\\\\\\\\\___________________/\\\\\\\\\____                                  
#  _\/\\\///////////______/\\\///\\\_____/\\\///////\\\_______________/\\\\\\\\\\\\\__                                 
#   _\/\\\_______________/\\\/__\///\\\__\/\\\_____\/\\\______________/\\\/////////\\\_                                
#    _\/\\\\\\\\\\\______/\\\______\//\\\_\/\\\\\\\\\\\/______________\/\\\_______\/\\\_                               
#     _\/\\\///////______\/\\\_______\/\\\_\/\\\//////\\\______________\/\\\\\\\\\\\\\\\_                              
#      _\/\\\_____________\//\\\______/\\\__\/\\\____\//\\\_____________\/\\\/////////\\\_                             
#       _\/\\\______________\///\\\__/\\\____\/\\\_____\//\\\____________\/\\\_______\/\\\_                            
#        _\/\\\________________\///\\\\\/_____\/\\\______\//\\\___________\/\\\_______\/\\\_                           
#         _\///___________________\/////_______\///________\///____________\///________\///__                          
# __/\\\______________/\\\__/\\\\\\\\\\\__/\\\\\_____/\\\__/\\\\\_____/\\\__/\\\\\\\\\\\\\\\____/\\\\\\\\\_____        
#  _\/\\\_____________\/\\\_\/////\\\///__\/\\\\\\___\/\\\_\/\\\\\\___\/\\\_\/\\\///////////___/\\\///////\\\___       
#   _\/\\\_____________\/\\\_____\/\\\_____\/\\\/\\\__\/\\\_\/\\\/\\\__\/\\\_\/\\\_____________\/\\\_____\/\\\___      
#    _\//\\\____/\\\____/\\\______\/\\\_____\/\\\//\\\_\/\\\_\/\\\//\\\_\/\\\_\/\\\\\\\\\\\_____\/\\\\\\\\\\\/____     
#     __\//\\\__/\\\\\__/\\\_______\/\\\_____\/\\\\//\\\\/\\\_\/\\\\//\\\\/\\\_\/\\\///////______\/\\\//////\\\____    
#      ___\//\\\/\\\/\\\/\\\________\/\\\_____\/\\\_\//\\\/\\\_\/\\\_\//\\\/\\\_\/\\\_____________\/\\\____\//\\\___   
#       ____\//\\\\\\//\\\\\_________\/\\\_____\/\\\__\//\\\\\\_\/\\\__\//\\\\\\_\/\\\_____________\/\\\_____\//\\\__  
#        _____\//\\\__\//\\\_______/\\\\\\\\\\\_\/\\\___\//\\\\\_\/\\\___\//\\\\\_\/\\\\\\\\\\\\\\\_\/\\\______\//\\\_ 
#         ______\///____\///_______\///////////__\///_____\/////__\///_____\/////__\///////////////__\///________\///__




# This function will return either a Boolean value of 'False', 'True', or, a string value of "Tie"
# This function will always fire after every button click from either player
def check_winner():

    # This for loop will iterate as many times as there are rows
    for row in range(3):
        
        # - This condition will test if any row returns three values equal to 
        #       eachother and also does not equal an empty string
        #  -If that is the case then whichever row that satisfies the condition 
        #       will be highlighted green while returning a Boolean value of 'True'
        # In other words, a winner was found and returned
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # This for loop will iterate as many times as there are columns
    for column in range(3):
        
        # - This condition will test if any column returns three values equal to 
        #       eachother and also does not equal an empty string
        # - If that is the case then whichever column that satisfies the condition 
        #       will be highlighted green while returning a Boolean value of 'True'
        # In other words, a winner was found and returned
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # - This condition will try to find a winner by seeing if the top left, center, 
    #       and bottom right buttons contain the same player symbol and does not equal 
    #           an empty string
    # - If this is the case then a diagonal line of highlighted squares will be presented 
    #       while also returning a Boolean value of 'True' aka a winner is identified
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    # - This condition will try to find a winner by seeing if the top right, center, 
    #       and bottom left buttons contain the same player symbol and does not equal 
    #           an empty string
    # - If this is the case then a diagonal line of highlighted squares will be presented 
    #       while also returning a Boolean value of 'True' aka a winner is identified
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # - This condition will check if the empty_spaces() functionality found 
    #       any empty spaces
    # - And this condition will run if no other condition was satisfied
    # - If that is the case then we use a for loop to highlight every button
    #       on the grid to be colored yellow while also returning a string value 
    #           of 'Tie'
    elif empty_spaces() is False:
        
        # Outside for loop will handle the 3 rows
        for row in range(3):
            
            # Inside for loop will handle the 3 columns
            for column in range(3):
                
                # - Here we will color the buttons yellow with the config() 
                #       functionality if no empty spaces were found
                buttons[row][column].config(bg="yellow")
        # - If no empty spaces were found, then after we have highlighted 
        #       the buttons we will return a string value of 'Tie'
        return "Tie"

    # - If none of the conditions above were satisfied then no 
    #       winner has been found and the game will continue on for 
    #           whether how many empty spaces are left or until enough buttons 
    #               have been clicked to satisfy either a winner or a tie in the check_winner() function
    # - If this code runs, then, either 'player = players[0]' OR 'player = players[1]' depending 
    #       on whose turn it is, or, what player was chosen at random to start the game
    else:
        return False







# _____/\\\\\\\\\_____/\\\\\_____/\\\__/\\\________/\\\__/\\\\____________/\\\\_______/\\\\\_________/\\\\\\\\\______/\\\\\\\\\\\\\\\_        
#  ___/\\\\\\\\\\\\\__\/\\\\\\___\/\\\_\///\\\____/\\\/__\/\\\\\\________/\\\\\\_____/\\\///\\\_____/\\\///////\\\___\/\\\///////////__       
#   __/\\\/////////\\\_\/\\\/\\\__\/\\\___\///\\\/\\\/____\/\\\//\\\____/\\\//\\\___/\\\/__\///\\\__\/\\\_____\/\\\___\/\\\_____________      
#    _\/\\\_______\/\\\_\/\\\//\\\_\/\\\_____\///\\\/______\/\\\\///\\\/\\\/_\/\\\__/\\\______\//\\\_\/\\\\\\\\\\\/____\/\\\\\\\\\\\_____     
#     _\/\\\\\\\\\\\\\\\_\/\\\\//\\\\/\\\_______\/\\\_______\/\\\__\///\\\/___\/\\\_\/\\\_______\/\\\_\/\\\//////\\\____\/\\\///////______    
#      _\/\\\/////////\\\_\/\\\_\//\\\/\\\_______\/\\\_______\/\\\____\///_____\/\\\_\//\\\______/\\\__\/\\\____\//\\\___\/\\\_____________   
#       _\/\\\_______\/\\\_\/\\\__\//\\\\\\_______\/\\\_______\/\\\_____________\/\\\__\///\\\__/\\\____\/\\\_____\//\\\__\/\\\_____________  
#        _\/\\\_______\/\\\_\/\\\___\//\\\\\_______\/\\\_______\/\\\_____________\/\\\____\///\\\\\/_____\/\\\______\//\\\_\/\\\\\\\\\\\\\\\_ 
#         _\///________\///__\///_____\/////________\///________\///______________\///_______\/////_______\///________\///__\///////////////__
# __/\\\\\\\\\\\\\\\__/\\\\____________/\\\\__/\\\\\\\\\\\\\____/\\\\\\\\\\\\\\\__/\\\________/\\\_                                           
#  _\/\\\///////////__\/\\\\\\________/\\\\\\_\/\\\/////////\\\_\///////\\\/////__\///\\\____/\\\/__                                          
#   _\/\\\_____________\/\\\//\\\____/\\\//\\\_\/\\\_______\/\\\_______\/\\\_________\///\\\/\\\/____                                         
#    _\/\\\\\\\\\\\_____\/\\\\///\\\/\\\/_\/\\\_\/\\\\\\\\\\\\\/________\/\\\___________\///\\\/______                                        
#     _\/\\\///////______\/\\\__\///\\\/___\/\\\_\/\\\/////////__________\/\\\_____________\/\\\_______                                       
#      _\/\\\_____________\/\\\____\///_____\/\\\_\/\\\___________________\/\\\_____________\/\\\_______                                      
#       _\/\\\_____________\/\\\_____________\/\\\_\/\\\___________________\/\\\_____________\/\\\_______                                     
#        _\/\\\\\\\\\\\\\\\_\/\\\_____________\/\\\_\/\\\___________________\/\\\_____________\/\\\_______                                    
#         _\///////////////__\///______________\///__\///____________________\///______________\///________                                   
# _____/\\\\\\\\\\\____/\\\\\\\\\\\\\_______/\\\\\\\\\___________/\\\\\\\\\__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\_______/\\\\\\\____             
#  ___/\\\/////////\\\_\/\\\/////////\\\___/\\\\\\\\\\\\\______/\\\////////__\/\\\///////////____/\\\/////////\\\__/\\\//////\\\__            
#   __\//\\\______\///__\/\\\_______\/\\\__/\\\/////////\\\___/\\\/___________\/\\\______________\//\\\______\///__\///_____\//\\\_           
#    ___\////\\\_________\/\\\\\\\\\\\\\/__\/\\\_______\/\\\__/\\\_____________\/\\\\\\\\\\\_______\////\\\___________________/\\\__          
#     ______\////\\\______\/\\\/////////____\/\\\\\\\\\\\\\\\_\/\\\_____________\/\\\///////___________\////\\\_____________/\\\\/___         
#      _________\////\\\___\/\\\_____________\/\\\/////////\\\_\//\\\____________\/\\\_____________________\////\\\_________/\\\/_____        
#       __/\\\______\//\\\__\/\\\_____________\/\\\_______\/\\\__\///\\\__________\/\\\______________/\\\______\//\\\_______\///_______       
#        _\///\\\\\\\\\\\/___\/\\\_____________\/\\\_______\/\\\____\////\\\\\\\\\_\/\\\\\\\\\\\\\\\_\///\\\\\\\\\\\/_________/\\\______      
#         ___\///////////_____\///______________\///________\///________\/////////__\///////////////____\///////////__________\///_______



# This checks if there are any empty spaces to input X or O
def empty_spaces():

    # We assign the number of spaces to the amount of buttons in our game
    spaces = 9

    # We use a for loop outside to handle the 3 rows
    for row in range(3):
        
        # We use a for loop inside to handle the 3 columns 
        for column in range(3):
            
            # - While iterating through all buttons, if a button does not equal 
            #       an empty string, then, we decrease 'spaces' by 1
            if buttons[row][column]['text'] != "":
                spaces -= 1



    # - If the variable 'spaces' is calculated to have decreased to 0 then 
    #       we return the Boolean value 'False' indicating that there are no more 
    #           spaces
    # - If this condition returns 'False' then the check_winner() function will 
    #       automatically return a string value of 'Tie' while highlighting the entire
    #           gameboard yellow 
    # - If this condition returns 'True', then, if the check_winner() function 
    #       has not found a winner then the next players turn will commence
    if spaces == 0:
        return False
    else:
        return True









# ____/\\\\\\\\\______/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\____/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\_        
#  __/\\\///////\\\___\/\\\///////////____/\\\/////////\\\_\/\\\///////////__\///////\\\/////__       
#   _\/\\\_____\/\\\___\/\\\______________\//\\\______\///__\/\\\___________________\/\\\_______      
#    _\/\\\\\\\\\\\/____\/\\\\\\\\\\\_______\////\\\_________\/\\\\\\\\\\\___________\/\\\_______     
#     _\/\\\//////\\\____\/\\\///////___________\////\\\______\/\\\///////____________\/\\\_______    
#      _\/\\\____\//\\\___\/\\\_____________________\////\\\___\/\\\___________________\/\\\_______   
#       _\/\\\_____\//\\\__\/\\\______________/\\\______\//\\\__\/\\\___________________\/\\\_______  
#        _\/\\\______\//\\\_\/\\\\\\\\\\\\\\\_\///\\\\\\\\\\\/___\/\\\\\\\\\\\\\\\_______\/\\\_______ 
#         _\///________\///__\///////////////____\///////////_____\///////////////________\///________
# __/\\\\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\\\\\_                                             
#  _\///////\\\/////__\/\\\_______\/\\\_\/\\\///////////__                                            
#   _______\/\\\_______\/\\\_______\/\\\_\/\\\_____________                                           
#    _______\/\\\_______\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\_____                                          
#     _______\/\\\_______\/\\\/////////\\\_\/\\\///////______                                         
#      _______\/\\\_______\/\\\_______\/\\\_\/\\\_____________                                        
#       _______\/\\\_______\/\\\_______\/\\\_\/\\\_____________                                       
#        _______\/\\\_______\/\\\_______\/\\\_\/\\\\\\\\\\\\\\\_                                      
#         _______\///________\///________\///__\///////////////__                                     
# _____/\\\\\\\\\\\\_____/\\\\\\\\\_____/\\\\____________/\\\\__/\\\\\\\\\\\\\\\_                     
#  ___/\\\//////////____/\\\\\\\\\\\\\__\/\\\\\\________/\\\\\\_\/\\\///////////__                    
#   __/\\\______________/\\\/////////\\\_\/\\\//\\\____/\\\//\\\_\/\\\_____________                   
#    _\/\\\____/\\\\\\\_\/\\\_______\/\\\_\/\\\\///\\\/\\\/_\/\\\_\/\\\\\\\\\\\_____                  
#     _\/\\\___\/////\\\_\/\\\\\\\\\\\\\\\_\/\\\__\///\\\/___\/\\\_\/\\\///////______                 
#      _\/\\\_______\/\\\_\/\\\/////////\\\_\/\\\____\///_____\/\\\_\/\\\_____________                
#       _\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\_____________\/\\\_\/\\\_____________               
#        _\//\\\\\\\\\\\\/__\/\\\_______\/\\\_\/\\\_____________\/\\\_\/\\\\\\\\\\\\\\\_              
#         __\////////////____\///________\///__\///______________\///__\///////////////__




# This will reset the game aka launch a new game for us
def new_game():

    # We want our 'player' variable to be global so we can utilize it
    global player

    # - This will use the random library and the choice() functionality 
    #       to pick a player at random to be the first player to start the game
    #           upon restarting the game
    player = random.choice(players)

    # - Since we are restarting the game we must make sure to update the 'label' with 
    #       the config() functionality and input the 'player' variable's random choice for 
    #           who will start the game
    label.config(text=player+" turn")


    # This for loop will handle the 3 rows outside
    for row in range(3):
        
        # This for loop will handle the 3 columns inside
        for column in range(3):
            
            # This will reset all buttons back to an empty string with grey boxes
            buttons[row][column].config(text="",bg="#F0F0F0")







# _____/\\\\\\\\\\\____/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\\\___                                      
#  ___/\\\/////////\\\_\/\\\///////////__\///////\\\/////__\/\\\_______\/\\\_\/\\\/////////\\\_                                     
#   __\//\\\______\///__\/\\\___________________\/\\\_______\/\\\_______\/\\\_\/\\\_______\/\\\_                                    
#    ___\////\\\_________\/\\\\\\\\\\\___________\/\\\_______\/\\\_______\/\\\_\/\\\\\\\\\\\\\/__                                   
#     ______\////\\\______\/\\\///////____________\/\\\_______\/\\\_______\/\\\_\/\\\/////////____                                  
#      _________\////\\\___\/\\\___________________\/\\\_______\/\\\_______\/\\\_\/\\\_____________                                 
#       __/\\\______\//\\\__\/\\\___________________\/\\\_______\//\\\______/\\\__\/\\\_____________                                
#        _\///\\\\\\\\\\\/___\/\\\\\\\\\\\\\\\_______\/\\\________\///\\\\\\\\\/___\/\\\_____________                               
#         ___\///////////_____\///////////////________\///___________\/////////_____\///______________                              
# __/\\\________/\\\_______/\\\\\_______/\\\________/\\\____/\\\\\\\\\_____                                                         
#  _\///\\\____/\\\/______/\\\///\\\____\/\\\_______\/\\\__/\\\///////\\\___                                                        
#   ___\///\\\/\\\/______/\\\/__\///\\\__\/\\\_______\/\\\_\/\\\_____\/\\\___                                                       
#    _____\///\\\/_______/\\\______\//\\\_\/\\\_______\/\\\_\/\\\\\\\\\\\/____                                                      
#     _______\/\\\_______\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\//////\\\____                                                     
#      _______\/\\\_______\//\\\______/\\\__\/\\\_______\/\\\_\/\\\____\//\\\___                                                    
#       _______\/\\\________\///\\\__/\\\____\//\\\______/\\\__\/\\\_____\//\\\__                                                   
#        _______\/\\\__________\///\\\\\/______\///\\\\\\\\\/___\/\\\______\//\\\_                                                  
#         _______\///_____________\/////__________\/////////_____\///________\///__                                                 
# _____/\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\_                                                                               
#  ___/\\\//////////__\/\\\_______\/\\\_\/////\\\///__                                                                              
#   __/\\\_____________\/\\\_______\/\\\_____\/\\\_____                                                                             
#    _\/\\\____/\\\\\\\_\/\\\_______\/\\\_____\/\\\_____                                                                            
#     _\/\\\___\/////\\\_\/\\\_______\/\\\_____\/\\\_____                                                                           
#      _\/\\\_______\/\\\_\/\\\_______\/\\\_____\/\\\_____                                                                          
#       _\/\\\_______\/\\\_\//\\\______/\\\______\/\\\_____                                                                         
#        _\//\\\\\\\\\\\\/___\///\\\\\\\\\/____/\\\\\\\\\\\_                                                                        
#         __\////////////_______\/////////_____\///////////__                                                                       
# __/\\\______________/\\\__/\\\\\\\\\\\__/\\\\\\\\\\\\\\\__/\\\________/\\\_                                                       
#  _\/\\\_____________\/\\\_\/////\\\///__\///////\\\/////__\/\\\_______\/\\\_                                                      
#   _\/\\\_____________\/\\\_____\/\\\___________\/\\\_______\/\\\_______\/\\\_                                                     
#    _\//\\\____/\\\____/\\\______\/\\\___________\/\\\_______\/\\\\\\\\\\\\\\\_                                                    
#     __\//\\\__/\\\\\__/\\\_______\/\\\___________\/\\\_______\/\\\/////////\\\_                                                   
#      ___\//\\\/\\\/\\\/\\\________\/\\\___________\/\\\_______\/\\\_______\/\\\_                                                  
#       ____\//\\\\\\//\\\\\_________\/\\\___________\/\\\_______\/\\\_______\/\\\_                                                 
#        _____\//\\\__\//\\\_______/\\\\\\\\\\\_______\/\\\_______\/\\\_______\/\\\_                                                
#         ______\///____\///_______\///////////________\///________\///________\///__                                               
# __/\\\\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\__/\\\\\_____/\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\____/\\\\\\\\\_____        
#  _\///////\\\/////__\/\\\_____/\\\//__\/////\\\///__\/\\\\\\___\/\\\_\///////\\\/////__\/\\\///////////___/\\\///////\\\___       
#   _______\/\\\_______\/\\\__/\\\//_________\/\\\_____\/\\\/\\\__\/\\\_______\/\\\_______\/\\\_____________\/\\\_____\/\\\___      
#    _______\/\\\_______\/\\\\\\//\\\_________\/\\\_____\/\\\//\\\_\/\\\_______\/\\\_______\/\\\\\\\\\\\_____\/\\\\\\\\\\\/____     
#     _______\/\\\_______\/\\\//_\//\\\________\/\\\_____\/\\\\//\\\\/\\\_______\/\\\_______\/\\\///////______\/\\\//////\\\____    
#      _______\/\\\_______\/\\\____\//\\\_______\/\\\_____\/\\\_\//\\\/\\\_______\/\\\_______\/\\\_____________\/\\\____\//\\\___   
#       _______\/\\\_______\/\\\_____\//\\\______\/\\\_____\/\\\__\//\\\\\\_______\/\\\_______\/\\\_____________\/\\\_____\//\\\__  
#        _______\/\\\_______\/\\\______\//\\\__/\\\\\\\\\\\_\/\\\___\//\\\\\_______\/\\\_______\/\\\\\\\\\\\\\\\_\/\\\______\//\\\_ 
#         _______\///________\///________\///__\///////////__\///_____\/////________\///________\///////////////__\///________\///__



# - Use the functionality of Tkinter to create a window variable assigned 
#       to the Tk() function
window = Tk()

# This is the Title of the window that pops up
window.title("Tic Tac Toe")

# These symbols can be swapped for any symbol to represent either player
# The symbols used in the Tic Tac Toe game
players = ["x","o"]

# - When the game first lanches this function decides at random what 
#       player will begin for example 'O starts' or 'X starts'
player = random.choice(players)

# This is a 2d list of buttons that represent the game board
buttons =  [[0,0,0],
            [0,0,0],
            [0,0,0]]


# This label will display whose turn it is in the game
label = Label(text=player + " turn", font=('consolas',40))

# - This Tkinter pack() function will tell where the label should be put, andso,
#       for this example we will put the 'label' identifying whose turn it is at the "top"
label.pack(side="top")



# - We will code in our reset button into the window which 
#       will 'restart' our game
# - We also added within the button function 'command=new_game' which will 
#       call our 'new_game()' function for us
reset_button = Button(text="restart", font=('consolas',20), command=new_game)

# - We will pack() our button once again at the "top" and so since 
#       the 'label' is the first one packed into the window
#           then, since the button is the second item to be packed at 
#               the "top" then it will be right under the 'label'
reset_button.pack(side="top")




# - This functionality will 'Frame()' the Tkinter window into a 
#       rectangular region in which to organize widgets
# - The Frame() widget will be used as a foundation class to implement 
#       complex widgets like the 'buttons' 2d list
frame = Frame(window)

# This will simply pack the widgets into the frame
frame.pack()



# We will use a nested for loop to consolidate the buttons inside the window
# Outer for loop will be in charge of the rows
for row in range(3):
    
    # The inner for loop will be in charge of the columns
    for column in range(3):
        
        # We will create a new button with two indexes because we are using a 2d list
        # Notice how in the 'Button()' we add 'Button(frame)' to add this to the frame
        # Next we customize the text(leave it blank), font, width, and height
        # And, we write a command assigned to a lambda function with row and column as key word arguments
        # Finally, in the lambda function our expression will call the 'next_turn()' function for every button press
        buttons[row][column] = Button(frame, text="", font=('consolas',40), width=5, height=2,
                                    command= lambda row=row, column=column: next_turn(row,column))
        
        # - Here we will add our 'buttons' to our frame and the grid() method is 
        #       used in the Tkinter library to arrange widgets in a table-like structure, 
        #           allowing you to specify their position using row and column indices
        buttons[row][column].grid(row=row,column=column)









# __/\\\_________________/\\\\\\\\\_____/\\\________/\\\__/\\\\\_____/\\\________/\\\\\\\\\__/\\\________/\\\_        
#  _\/\\\_______________/\\\\\\\\\\\\\__\/\\\_______\/\\\_\/\\\\\\___\/\\\_____/\\\////////__\/\\\_______\/\\\_       
#   _\/\\\______________/\\\/////////\\\_\/\\\_______\/\\\_\/\\\/\\\__\/\\\___/\\\/___________\/\\\_______\/\\\_      
#    _\/\\\_____________\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\//\\\_\/\\\__/\\\_____________\/\\\\\\\\\\\\\\\_     
#     _\/\\\_____________\/\\\\\\\\\\\\\\\_\/\\\_______\/\\\_\/\\\\//\\\\/\\\_\/\\\_____________\/\\\/////////\\\_    
#      _\/\\\_____________\/\\\/////////\\\_\/\\\_______\/\\\_\/\\\_\//\\\/\\\_\//\\\____________\/\\\_______\/\\\_   
#       _\/\\\_____________\/\\\_______\/\\\_\//\\\______/\\\__\/\\\__\//\\\\\\__\///\\\__________\/\\\_______\/\\\_  
#        _\/\\\\\\\\\\\\\\\_\/\\\_______\/\\\__\///\\\\\\\\\/___\/\\\___\//\\\\\____\////\\\\\\\\\_\/\\\_______\/\\\_ 
#         _\///////////////__\///________\///_____\/////////_____\///_____\/////________\/////////__\///________\///__


# - This will launch our game window because 
#       the 'window' variable is assigned to the Tk() function
window.mainloop()
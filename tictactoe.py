import random
game_list = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "] # the list where user's input will be stored
marker_list = [] # 2 values X and O, to determine which one is player 1 and player 2
player_names = [] # 2 values determines player 1 and player2 according to marker list
score_board = [0,0] # 2 values determines player 1 and player 2's score
game_played = 0
xo_times_list = [] # the list where the x and o values given by choose first function are stored, used with x_o index
player_times_list = [] # the list where the player names given by the choose first function are stored
index_list = [] # empty list where we will add all the position numbers user inputed
index_list_full = [1,2,3,4,5,6,7,8,9] # list to check which position number is not in index list
won_game = False # to check if the game is won
player_index = 0 # more on that below
game_on = True # to check if the game is on
game_continue = True # to check if the game is gonna continue from the memory or will it start fresh

# displaying the game
def display_game(game_list):
    
    # printing the board in a sequence with its format
    print(f"  Tic  tac  toe",end = "           |          ")
    print("Board positions",end = "         |        ")
    print("Game stats")
    print(" ",end = "                         |           ")
    print(" ",end = "                      |           ")
    print(" ")
    print(f"  {game_list[1]}  |  {game_list[2]}  |  {game_list[3]  }", end = "           |           ")
    print("1  |  2  |  3",end = "          |       ")
    print(f"{player_names[0]}'s score: {score_board[0]}")
    print(f"-----------------",end = "         |           ")
    print("-------------")
    print(f"  {game_list[4]}  |  {game_list[5]}  |  {game_list[6]}  ",end = "         |           ")
    print("4  |  5  |  6",end = "          |       ")
    print(f"{player_names[1]}'s score: {score_board[1]}")
    print(f"-----------------",end = "         |           ")
    print("-------------")
    print(f"  {game_list[7]}  |  {game_list[8]}  |  {game_list[9]}  ",end = "         |           ")
    print("7  |  8  |  9",end = "          |       ")  
    print(f"Games played: {game_played}")
    
# displayng the game format
def display_format():
    
    # displaying the format of playing the game
    print("   ")
    print("This is a two player Tic Tac Toe. First the players will choose who will be X or O")
    print("Then they will enter a position number where they want to mark thier X or O")
    print("   ")
    print("The board position numbers are like this: ")
    print("1  |  2  |  3")
    print("-------------")
    print("4  |  5  |  6")
    print("-------------")
    print("7  |  8  |  9")
    print("   ")
    print("If you want to stop the game at any certain point just write quit and the game will stop")
    print(" ")

# users gives thier name
def player_name():
    
    global game_on
    global game_continue
    player_list = ["Player 1", "Player 2"]
    # User will give either the choice X or O which will be then implemented on the board
    
    for name in player_list:
        # user gets the message to choose name
        choice = "0"
        while choice.isalpha() == False:
            choice_input = input(f"{name} please choose your name: ")
            choice = choice_input.strip()
        
            if choice.lower() == "quit":
                game_on = False
                game_continue = False
                print("Game quitted")
                return game_on, game_continue
            if choice.isalpha() == False:
                print("Numbers or special characters are not valid to be used in a name, please use alphabets only")     
        player_names.append(choice)
    
    print(" ")
    print(f"Player 1 is {player_names[0]}")
    print(f"Player 2 is {player_names[1]}")
    print(" ")
    game_continue = True # this is only for the "F" function which helps to refresh memory of the game
    return player_names 

# choosing who is x or o
def xory():
    
    global game_on
    choice = "Wrong" #taking the first choice so that the while loop runs
    x_o = ["X", "O"]
    # User will give either the choice X or O which will be then implemented on the board
    while choice not in x_o:
        
        # user gets the message to choose
        choice_input = input("Please choose your marker (capital X or O): ")
        choice = choice_input.strip()

        if choice.lower() == "quit":
            game_on = False
            print("Game quitted")
            return game_on
        # give error if someone wants to print anything else
        elif choice == "0":
            print("Wrong input, it's capital O not 0 (zero)")
        elif choice not in x_o:
            print("Sorry wrong input, choose either capital X or O")
    
    # creating the database where we will append the user input to marker list and player list
    def appending(): 
        marker_list.append(choice) # appending user input to marker list
        print(" ")
        print(f"{player_names[0]} choose {choice}")
        x_o.remove(choice) # removing the given user input to get the other value X or O form x_o
        marker_list.append(x_o[0]) # appending leftover to marker list
        print(" ")
        print(f"{player_names[1]} gets {x_o[0]}")
        print(" ")
    
    appending()
        
    return marker_list, player_names

# randomly choosing who gets the first turn
def choose_first():
    
    random_num = random.randint(0,9) #taking a random number
    
    display_game(game_list)
    
    # this function is to get how many x and o will be there, also this function determines the numbers of x and o by 
    # the below conditions
    def who_goes_first():
        while len(xo_times_list) < 9: # 9 places on board so we want 9 values
            # looping over the marker_list where x and o are stored
            whole_list = [marker_list, player_names] # creating a second database where marker list and player list exists
            # to append in the lists created above marker and player
            for index,value in enumerate(whole_list): 
                each_list = whole_list[index] # taking a single list
                # to append in a single list
                for value in each_list:
                    # if marker is the last value in the marker_list and the length of x_o list is 9, we finish the loop
                    if value == each_list[-1] and each_list == 9:
                        break
                    # append to marker
                    if each_list == whole_list[0]:
                        xo_times_list.append(value)
                    # or to the player
                    else:
                        player_times_list.append(value)
                        
    # if even number player 1 goes firs                
    if random_num % 2 == 0:
        print(" ")
        print(f"{player_names[0]} will go first")
        who_goes_first()
    
    # for odd player 2 goes first            
    else:
        print(" ")
        print(f"{player_names[1]} will go first")
        marker_list.reverse()
        player_names.reverse()
        who_goes_first()
    
    return xo_times_list, player_times_list

# function for checking if the space is empty where use has given input
def space_check():
    
    used_str = "The positions used: " # the positions we already used
    non_used_str = "The positons unused: " # the positions still unused

    #throwing an error and telling the user to take any value from the non used
    print(f"The number have already been choosen once, choose a different number from unused positions to assign value")
    
    index_list.sort()
    # to print what has been used already
    for i in index_list:
        # for the last one we don't want any commas at the end
        if i == index_list[-1] or len(index_list) == 1:
            index = str(i)
            used_str += index
        # here we are taking the used str and adding the values with commas and space between them
        else:
            index = str(i)
            used_str += index + "," + " "
         
    # to print what has not been used already   
    for i in index_list_full:
            
        # here we are checking if i is in the used list, then we will avoid it
        if i not in index_list:
             # for the last one we don't want any commas at the end
            if i == index_list_full[-1] or len(index_list_full) == 1:
                index = str(i)
                non_used_str += index
            # here we are taking the used str and adding the values with commas and space between them
            else:
                index = str(i)
                non_used_str += index + "," + " " 
    print(used_str)
    print(non_used_str)     

# placing the marker on board       
def place_marker(game_list, xo_times_list):
    
    xo_index = 0 # this is the index of the x_o list we created above
    global player_index
    global game_on
    global game_continue
    
    # cannot exceed more than 9 cause there are 9 houses in the board
    while len(index_list) < 9:
        
        # user gives a number as input
        print("  ")
        print(f"{player_names[0]} is {marker_list[0]}")
        print(f"{player_names[1]} is {marker_list[1]}")
        print(" ")
        index_input = input(f"{player_times_list[player_index]}'s turn \nPlease choose a position number from 1 to 9: ")
        index = index_input.strip()
        print(" ")
        
        if index.lower() == "quit":
            game_on = False
            game_continue = False
            print("Game quitted")
            return game_on, game_continue
        # if user gives a string or nothing then we throw an error at them and tell them to give the right one
        elif index.isdigit() == False:
            print("Sorry that's not a digit, enter a digit form 1 to 9")
            
        # checking if the number that is given by user was already given once
        elif int(index) in index_list:
            space_check() # check if the space is already occupied
        # if user gives something outside of 1 to 9
        elif int(index) not in range(1,10):
            print("Sorry number not in range, enter a digit form 1 to 9")
        else:
            int_index = int(index) # turn it to an integer
            game_list[int_index] = xo_times_list[xo_index] # assign the marker choosen by user before to the given position
            index_list.append(int_index) # to make sure all the numbers are given and to end the loop at a certain point
            display_game(game_list) # prints the game board and format
            win_check(game_list) # checks if the game is won
            # when won game is true or the length of index list is 9 the loop breaks
            if won_game == True or len(index_list) == 9:
                break
            xo_index += 1 # increment
            player_index += 1 # increment
          
    return game_list

# function to check if the user has won
def win_check(game_list):
    
    global won_game
    
    def win_condition():
        
        global game_played
        
        for i in player_names:
            if i == player_times_list[player_index]:
                index = player_names.index(i)
                score_board[index] += 1

        # make the won game true essentially breaking the game
        game_played += 1
        
        print(" ")
        print(f"{player_times_list[player_index]} have won the game")
        print(" ")
        print(f"Games played: {game_played}")
        print(f"{player_names[0]}'s score: {score_board[0]}")
        print(f"{player_names[1]}'s score: {score_board[1]}")
        
        return game_played, score_board
    
    column_index = 1 # for columns
    
    # condition so that column index dont go above 3 (more on that on next comment)
    while column_index < 4:
        
        # here checking if position 1, position 4 and position 7 has the same value, this is for the column check
        # if same value we let the player win and checks that no spaces left in the positions
        if (game_list[column_index] == game_list[column_index + 3] == game_list[column_index + 6]
            and " " not in [game_list[column_index], game_list[column_index + 3], game_list[column_index + 6]]):
            win_condition()
            won_game = True
            return won_game
            
        # if no condition met we just keep adding 1 to go from positon 1 to 2 and at certain point to end the loop
        else:
            column_index += 1
            
    row_index = 1 # for columns
    
    # condition so that column index dont go above 8 (more on that on next comment)
    while row_index < 8:
        # here checking if position 1, position 2 and position 3 has the same value, this is for the row check
        # if same value we let the player win and checks that no spaces left in the positions
        if (game_list[row_index] == game_list[row_index + 1] == game_list[row_index + 2]
            and " " not in [game_list[row_index], game_list[row_index + 1], game_list[row_index + 2]]):
            win_condition()
            won_game = True
            return won_game
        
        # if no condition met we just keep adding 3 to go from positon 1 to 4 and at certain point to end the loop
        else:
            row_index += 3
            
    diagonal_index = 1 # for columns
    
    # condition so that column index dont go above 4 (more on that on next comment) 
    while diagonal_index < 4:
        
        if diagonal_index == 1: # for first diagonal
            
            # here checking if position 1, position 5 and position 9 has the same value, this is for the diagonal 1 check
            # if same value we let the player win and checks that no spaces left in the positions
            if (game_list[diagonal_index] == game_list[diagonal_index + 4] == game_list[diagonal_index + 8]
                and " " not in [game_list[diagonal_index], game_list[diagonal_index + 4], game_list[diagonal_index + 8]]):
                win_condition()
                won_game = True
                return won_game
                
            else:
                diagonal_index += 2 #we go to the next diagonal
                
        if diagonal_index == 3: # for second diagonal
            
            # here checking if position 1, position 5 and position 9 has the same value, this is for the diagonal 1 check
            # if same value we let the player win and checks that no spaces left in the positions
            if (game_list[diagonal_index] == game_list[diagonal_index + 2] == game_list[diagonal_index + 4]
                and " " not in [game_list[diagonal_index], game_list[diagonal_index + 2], game_list[diagonal_index + 4]]):
                win_condition()
                won_game = True
                return won_game
            else:
                diagonal_index += 2 #we end the loop but making it false
    
    else:
        full_board_check()     

# cheing if the board is full         
def full_board_check():
    
    global game_played
    # checks if the board is full, if full it says the game is tie
    if len(index_list) == 9:
        print(" ")
        print("It's a tie")
        game_played += 1
        print(" ")
        print(f"Games played: {game_played}")
        print(" ")
        print(f"{player_names[0]}'s score: {score_board[0]}")
        print(f"{player_names[1]}'s score: {score_board[1]}")
        return game_list, game_played
    
# function for replaying the game
def replay():
    
    choice = "Wrong"
    # getting all the global variables
    global game_list
    global marker_list
    global player_names
    global xo_times_list
    global player_times_list
    global index_list
    global won_game
    global player_index
    global game_on
    global game_continue
    global score_board
    global game_played
    
    if game_on == True:
        # telling user to choose Yes or No
        while choice not in ["YES", "NO", "F"]:
        
            print(" ")
            # choice for either playing the same game or starting it fresh
            choice_input = input("Game Over. Would you guys like to play another round (type capital YES or NO) \nOr would you guys want to start a fresh game (type capital F): ")
            choice = choice_input.strip()
            # if user gives something else 
            if choice not in ["YES", "NO", "F"]:
                print("I don't understand, please say capital YES or NO")
    
        # if user wants to continue reset everything   
        if choice == "F":
            print(" ")
            print("Let's start fresh then")
            game_list = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            marker_list = []
            player_names = []
            score_board = [0,0]
            xo_times_list = []
            player_times_list = []
            index_list = []
            won_game = False
            player_index = 0
            game_on = True
            game_continue = False 
            # making it false so that the game don't continue on the same memory later made it true so that the next step runs
            game_played = 0
            return game_on, game_continue, game_played
        elif choice == "YES":
            print(" ")
            print("Let's continue then")
            print(" ")
            game_list = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            xo_times_list = []
            player_times_list = []
            index_list = []
            won_game = False
            player_index = 0
            game_on = True
            game_continue = True
            return game_on, game_continue
    
        # otherwise just end the game
        else:
            print(" ")
            print("Thanks for playing, hope to see you guys again")
            game_on = False
            game_continue = False
            return game_on, game_continue

# main game    
def tic_tac_toe():
    
    global game_on
    "Welcome to Tic tac toe"
    while game_on:
        
        display_format()
        
        player_name()
        
        if game_on == True:
            xory()
        
        while game_continue == True: 
            choose_first()
        
            place_marker(game_list, xo_times_list)
        
            replay()
    
tic_tac_toe()

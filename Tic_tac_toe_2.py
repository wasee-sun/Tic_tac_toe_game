import random


class TicTacToe: #Using 2D list / Matrix
    def __init__(self, *players):
        self.board = [ # the board
            {"A": " ", "B": " ", "C": " "},
            {"D": " ", "E": " ", "F": " "},
            {"G": " ", "H": " ", "I": " "}
        ]
        self.turn = 0 # player turn
        self.players = players # player list
        self.markers = [] # X and O markers
        
    def get_pl_name(self): # return the name of the player
        return self.players[self.turn].name
        
    def input_check(self, pos_input): # checks whether the position is valid
        valid = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] 
        if pos_input not in valid: # if position not in the list
            print("Not a valid position, choose from the valid positions")
            return False
        else: # if position is already taken
            for ind, row in enumerate(self.board):
                if pos_input in row.keys():
                    if self.board[ind][pos_input] != " ":
                        print("Position already filled")
                        return False
        return True
        
    def set_marker(self): # sets the marker
        marker = ["X", "O"]
        choice = random.choice(marker) # chooses a random marker
        self.markers.append(choice) # first player marker
        marker.remove(choice)
        self.markers.append(marker[0]) # second player marker
        for ind, mark in enumerate(self.markers, start=1): # print the marker
            print(f"Player {ind}: {mark}")
        
    def move(self, pos): # inputs the marker of the player in a designated position
        for ind, row in enumerate(self.board):
            if pos in row.keys(): # if position in the row
                if self.turn == 0: # player 1
                    marker = self.markers[self.turn]
                    self.turn = 1
                else: #player 2
                    marker = self.markers[self.turn]
                    self.turn = 0
                self.board[ind][pos] = marker # input the marker
                return 
                
    def win_check(self): # checking if the player won
        for ind, row in enumerate(self.board): # row check
            key_lst = []
            for key in row.keys(): # finding the keys
                key_lst.append(key)
            if self.board[ind][key_lst[0]] == self.board[ind][key_lst[1]] == self.board[ind][key_lst[2]] != " ": # checking whether the row matches and values are not " "
                win_marker = self.board[ind][key_lst[0]]
                return win_marker
        
        for i in range(3): # column check
            k_lst = []
            for row in self.board: # going into the rows
                index = 0
                for key in row.keys():
                    if index == i: # if the column number matches
                        k_lst.append(key)
                        break
                    index += 1
            if self.board[0][k_lst[0]] == self.board[1][k_lst[1]] == self.board[2][k_lst[2]] != " ": # checking whether the column matches and values are not " "
                win_marker = self.board[0][k_lst[0]]
                return win_marker
        
        #diagonal check, checks whether both diagonal matches and not " "
        if (self.board[0]["A"] == self.board[1]["E"] == self.board[2]["I"] != " "):
            win_marker = self.board[0]["A"]
            return win_marker
        
        if (self.board[0]["C"] == self.board[1]["E"] == self.board[2]["G"] != " "):
            win_marker = self.board[0]["C"]
            return win_marker
        
        draw = "draw"
        for row in self.board: # if no winner checks for draw
            if " " in row.values():  # if space found, then we break from the loop as the game is not over
                draw = False
                break
        return draw # returns false of draw
            
    def winner(self):
        marker = self.win_check() # gets the marker
        if marker:
            if marker == "draw": # checks if it is a marker or draw string
                print("Draw")
            else: # for marker
                ind = self.markers.index(marker) # gets the index of the player
                self.players[ind].score += 1
                self.players[ind].win_str() # winner player string
            for player in self.players: # prints player score
                print(f"{player.name}: {player.score}")
            for ind, row in enumerate(self.board): # clears the board
                for key in row.keys():
                    self.board[ind][key] = " "
            return True
        else:
            return False
            
    def printBoard(self): # prints the board
        print("  Board         Position", end="      ")
        print(f"Player 1: {self.players[0].name} | Score: {self.players[0].score} | Marker: {self.markers[0]}")
        print("---------", end="     ")
        print("-----------", end="     ")
        print(f"Player 2: {self.players[1].name} | Score: {self.players[1].score} | Marker: {self.markers[1]}")
        for row in self.board:
            b_str = "" # board string
            pos_str = "" # position string
            for pos, x_o in row.items():
                pos_str += pos + " | "
                b_str += x_o + " | "
            print(b_str[:-2], end="     ")
            print(pos_str[:-2])
            print("---------", end="     ")
            print("-----------")
        
class Player: # player class
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def win_str(self):
        print(f"Winner: {self.name}")
    
if __name__ == "__main__":
    
    running = True
    while running: # while game is running
        print("Welcome to TicTacToe")
        name1 = input("Player 1: ")
        name2 = input("Player 2: ")
        p1 = Player(name1) # create player object
        p2 = Player(name2)
        t_t_t = TicTacToe(p1, p2)
        t_t_t.set_marker() # sets the marker
        t_t_t.printBoard() # prints the board
        
        playing = True
        while playing:
            print("Choose your position from the position table")
            player_move = input(f"Player {t_t_t.get_pl_name()}: ").upper() # gets postition input from the user
            valid = t_t_t.input_check(player_move)
            if valid: # if player move is valid
                t_t_t.move(player_move) # inputs the marker of player in the position
                t_t_t.printBoard() 
                win = t_t_t.winner() # checks for winners or draw
                if win: # if a player wins or draws
                    prompt = True
                    while prompt: # prompt appears whether player want to continue, new game or exit game
                        play_again = input(f"Do you want to continue playing (Y), New game (N) or Exit (E)").upper()
                        if play_again == "Y": # continue
                            t_t_t.printBoard()
                            prompt = False
                        elif play_again == "N": # new game
                            prompt = False
                            playing = False
                        elif play_again == "E": # exit application
                            prompt = False
                            playing = False
                            running = False
                        else:
                            print("Not a valid input, choose Y, N or E")
        
        
        
    
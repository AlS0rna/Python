class Board:
    
    #Konstruktor
    def __init__(self):
        self.state =[ [" "," "," "],
                      [" "," "," "],
                      [" "," "," "] ]
        
        self.gameOn=True
        self.player=False
       

    #Ausgabe Spielbrett
    def print_board(self):
        print("----------")
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if j<=1:
                    print(self.state[i][j],"|",end=" ")
                else:
                    print(self.state[i][j],end=" ")
                
            print()
        print("----------")
    
        


    def turn(self):

        print("Geben Sie eine Zeile und eine Spalte ein")
        z=input("In welcher Zeile? ")
        s=input("In welcher Spalte? ")

        #Anpassung der Werte fürs Array 
        z= int(z)-1
        s= int(s)-1

        if self.state[int(z)][int(s)] != " ":
            print("\n" "Feld ist bereits belegt. Wählen Sie ein anderes Feld\n")
            z=input("In welcher Zeile? ")
            s=input("In welcher Spalte? ")
            z= int(z)-1
            s= int(s)-1

        if self.player == False:
           self.state[int(z)][int(s)]="X"    
           self.player = True
        else:
            self.state[int(z)][int(s)]="O"
            self.player = False    
        
        self.gameOver()


    def gameOver(self):
        #Waagerecht
        if self.state[int(0)][int(0)] == "X" and  self.state[int(0)][int(1)] == "X" and self.state[int(0)][int(2)] == "X":
            print("Player X hat gewonnen!")
            exit()

        elif self.state[int(2)][int(0)] == "X" and self.state[int(2)][int(1)] == "X" and self.state[int(2)][int(2)] == "X":
            print("Player X hat gewonnen!")
            exit()

        elif self.state[int(1)][int(0)] == "X" and self.state[int(1)][int(1)] == "X" and self.state[int(1)][int(2)] == "X":
            print("Player X hat gewonnen!")
            exit()

        #Senkrecht 
        elif self.state[int(0)][int(0)] == "X" and self.state[int(1)][int(0)] == "X" and self.state[int(2)][int(0)] == "X":
            print("Player X hat gewonnen!")
            exit()

        elif self.state[int(0)][int(1)] == "X" and self.state[int(1)][int(1)] == "X" and self.state[int(2)][int(1)] == "X":
            print("Player X hat gewonnen!")
            exit()

        elif self.state[int(0)][int(2)] == "X" and self.state[int(1)][int(2)] == "X" and self.state[int(2)][int(2)] == "X":
            print("Player X hat gewonnen!")
            exit()

        #Diagonal 
        elif self.state[int(0)][int(0)] == "X" and self.state[int(1)][int(1)] == "X" and self.state[int(2)][int(2)] == "X":
            print("Player X hat gewonnen!")
            exit()

        elif self.state[int(0)][int(2)] == "X" and self.state[int(1)][int(1)] == "X" and self.state[int(2)][int(0)] == "X":
            print("Player X hat gewonnen!")
            exit()

        #Waagerecht        
        if self.state[int(0)][int(0)] == "O" and self.state[int(0)][int(1)] == "O" and self.state[int(0)][int(2)] == "O": 
            print("Player O hat gewonnen!") 
            exit()

        elif self.state[int(2)][int(0)] == "O" and self.state[int(2)][int(1)] == "O" and self.state[int(2)][int(2)] == "O":
            print("Player O hat gewonnen!") 
            exit()

        elif self.state[int(1)][int(0)] == "O" and self.state[int(1)][int(1)] == "O" and self.state[int(1)][int(2)] == "O":
            print("Player O hat gewonnen!") 
            exit()

        #Senkrecht
        elif self.state[int(0)][int(0)] == "O" and self.state[int(1)][int(0)] == "O" and self.state[int(2)][int(0)] == "O":
            print("Player O hat gewonnen!") 
            exit()

        elif self.state[int(0)][int(1)] == "O" and self.state[int(1)][int(1)] == "O" and self.state[int(2)][int(1)] == "O":
            print("Player O hat gewonnen!") 
            exit()

        elif self.state[int(0)][int(2)] == "O" and self.state[int(1)][int(2)] == "O" and self.state[int(2)][int(2)] == "O":
            print("Player O hat gewonnen!") 
            exit()
         
        #Diagonal 
        elif self.state[int(0)][int(0)] == "O" and self.state[int(1)][int(1)] == "O" and self.state[int(2)][int(2)] == "O":
            print("Player O hat gewonnen!") 
            exit()

        elif self.state[int(0)][int(2)] == "O" and self.state[int(1)][int(1)] == "O" and self.state[int(2)][int(0)] == "O":
            print("Player O hat gewonnen!") 
            exit()


if __name__ == "__main__":
    
    game = Board()
    while game.gameOn==True:
        game.turn()
        game.print_board()
        
    
        
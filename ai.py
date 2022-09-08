#!/usr/bin/env python3
import rotarequests

FORESIGHT = 10 #aka depth of search
#some thoughts on improvements:
#getting rid of len methods (this is because board is static size and i'm wasting time with function lookup)

class Piece:
    def __init__(self, allegiance, location):
        self.allegiance = allegiance #either a piece is an adversary or an ally
        self.location = location #location on the board
    def update(self, destination):
        self.location = destination

class Board:
    def __init__(self):
        self.state = []

    def add(self, piece):
        self.state.append(piece)

    def remove(self, piece):
        self.state.remove(piece)

    def validateMove(self, location, destination):
        hash = self.getHash()
        if location == -1:
            if self.state.len() >= 6:
                return False
            elif hash[destination - 1] == 0:
                return True
            else:
                return False
        else:
            if self.state.len() < 6:
                return False
            elif hash[location - 1] != 2:
                return False
            else:
                if hash[destination - 1] == 0:
                    return True
                else:
                    return False



    def __str__(self):
        board = "-" * 9
        if self.state.len() != 0:
            for i in self.state:
                board[i.location - 1] = i.allegiance

        return board[0:2] + "\n" + board[3:5] + "\n" + board[6:8] + "\n"

    def getHash(self):
        hash = "0" * 9
        for i in self.state:
            base3 = 0
            if i.allegiance = "c":
                base3 = 1
            elif i.allegiance = "p":
                base3 = 2

            board[i.location - 1] = base3

        return hash


    def isthree(self):
        #check last piece's location and its' corresponding "lines"
        #we want to avoid the n^2 solution (zzz boring)
        #there are not that many tictactoe states so we can just hash them as base 3

        hash = self.getHash()
        wins =
        [hash[0][0], hash[0][1], hash[0][2]],
        [hash[1][0], hash[1][1], hash[1][2]],
        [hash[2][0], hash[2][1], hash[2][2]],
        [hash[0][0], hash[1][0], hash[2][0]],
        [hash[0][1], hash[1][1], hash[2][1]],
        [hash[0][2], hash[1][2], hash[2][2]],
        [hash[0][0], hash[1][1], hash[2][2]],
        [hash[2][0], hash[1][1], hash[0][2]],
        ]

        if [2, 2, 2] in wins:
            return 2
        elif [1, 1, 1] in wins:
            return 1
        else:
            return 0

def minimax(movetype, turn):

    alpha = float('-inf')
    beta = float('inf')

    if board.isthree() != 0:
        return board.isthree()


def move():



def rota_ai(board):
    #static first move because we already know best move
    #no need to compute large tree
    if board.state.len() == 0:
        piece = Piece("p", 5)
        board.add(piece)
        return ("place", -1, 5)
    elif board.state.len() < 6:
        #decide placement


        #adjust board

        piece = Piece("p", bestMove[1])
        board.add(piece)
        return ("place", -1, destination)
        #return instructions for web
    else:
        #decide move


        #adjust board

        for piece in board:
            if piece.location == bestMove[0]:
                piece.update(bestMove[1])
        #return instructions for web
        return ("move", location, destination)


def play(start):
    state = start
    board = Board()


    def resolve():
        for i in range(state.len() - 1):
            if state[i] not "-":
                piece = Piece(state[i], i + 1)
                board.add(piece)

    while True:
        resolve()
        ai_move = rota_ai(board)
        if ai_move[0] == "move":
            state = rotarequests.move(ai_move[1], ai_move[2])
        elif ai_move[0] == "place":
            state = rotarequests.place(ai_move[2])
        else:
            state = rotarequests.next()
        board = Board()



if __name__ == "__main__":
    print("Starting ROTA ai...")
    print("Communicating with server...")
    x = rotarequests.newgame()
    play(x)

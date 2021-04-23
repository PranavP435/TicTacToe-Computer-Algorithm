from random import choice

'''Coded by Pranav P - 24 - 04 - 2021'''

class TTTComputer:

    def __init__(self, peg : "str", board: "list[str]" = [""]*9):

        if len(board) is not 9:
            raise IncorrectBoard("The Board input does not have 9 elements.")
        
        if peg.upper() not in ["X", "O"]:
            raise IncorrectBoard("The pegs can only be X or O")

        self.board = board
        self.peg = peg.upper()
        self.opponent = "O" if self.peg == "X" else "X"

    def __calculate_possible_moves(self, board):
        empty_spaces = []
        for space in range(len(board)):
            if board[space].upper() not in ["X","O"]:
                empty_spaces.append(space)
        return empty_spaces
    
    def __isWinner(self,peg, board):
        return ((board[0] == peg and board[1] == peg and board[2] == peg) or
            (board[3] == peg and board[4] == peg and board[5] == peg) or
            (board[6] == peg and board[7] == peg and board[8] == peg) or
            (board[0] == peg and board[3] == peg and board[6] == peg) or
            (board[1] == peg and board[4] == peg and board[7] == peg) or
            (board[2] == peg and board[5] == peg and board[8] == peg) or
            (board[0] == peg and board[4] == peg and board[8] == peg) or
            (board[2] == peg and board[4] == peg and board[6] == peg))

    def move(self, board: list[str]) -> int:
        '''This algorithm sees the board in the following manner:
    0 1 2
    3 4 5
    6 7 8

    So input the board accordingly
    '''
        boardcopy = board[:]
        # To avoid both variables pointing to same memory location; change to boardcopy
        # will lead to change in board also, so list slicing is used here to make two different memory locations for both.
        possible_moves = self.__calculate_possible_moves(board)

        if self.opponent not in board and any(square.isalpha() for square in board): # self.moves is not equal to zero
            raise IncorrectBoard("The pegs can only be X or O")

        for peg in [self.opponent, self.peg]: #Check if any of the next possible moves can lead to a win for computer, or for the player
            for move in possible_moves:
                boardcopy[move] = peg
                if self.__isWinner(peg,boardcopy):
                    return move # if yes, play that move, either to win or to prevent the player from winning.
                boardcopy = board[:]

        if 4 in possible_moves:
            return 4 # The middle square 

        return choice(possible_moves)

class IncorrectBoard(Exception):
    '''Raised when the board input is not in the correct form:
        1. Length should be 9
        2. The board cannot contain any other letter from the English alphabet, other than X and O.    
    '''

    def __init__(self,message):
        self.message = message

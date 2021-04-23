from random import choice

'''Coded by Pranav P - 24 - 04 - 2021'''

class TTTComputer:

    def __init__(self, peg : "str", board: "list[str]" = [""]*9):
        if peg.lower() not in ["x", "o"]:
            print("Invalid peg input")
            return
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

        for peg in [self.opponent, self.peg]:
            for move in possible_moves:
                boardcopy[move] = peg
                if self.__isWinner(peg,boardcopy):
                    return move
                boardcopy = board[:]

        if 4 in possible_moves:
            return 4 # The middle square 

        return choice(possible_moves)


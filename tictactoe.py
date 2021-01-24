import board
import player
from copy import deepcopy

class TicTacToe:
    def __init__(self):
        self.num_players = int(input('0, 1, or 2 players: '))
        if self.num_players == 0:
            self.px = player.Player('x', True)
            self.po = player.Player('o', True)
        elif self.num_players == 1:
            self.human = input('choose x or o: ')
            if self.human == 'x':
                self.px = player.Player('x', False)
                self.po = player.Player('o', True)
            else:
                self.px = player.Player('x', True)
                self.po = player.Player('o', False)
        else:
            self.px = player.Player('x', False)
            self.po = player.Player('o', False)


        self.game_board = board.Board()
        print(self.game_board)
        self.player = self.px # x goes first


    def make_move(self, board, player):
        self.move = self.get_move(board, player)
        board.update(player.symbol, self.move)


    def get_move(self, board, player):
        if player.ai:
            print('determining ', player.symbol, "'s move...", sep='')
            self.mm = self.minimax(board, player)
            for square in range(board.square_range):
                self.new_board = deepcopy(board)
                if self.new_board.legal_move(square):
                    self.new_board.update(player.symbol, square)
                    if self.mm == self.minimax(self.new_board, self.po if player == self.px else self.px):
                        return square
        else: # human player
            while True:
                self.move = int(input('next move (0-8) for ' + player.symbol + ': '))
                if (board.legal_move(self.move)):
                    return self.move
                else:
                    print('illegal')


    def minimax(self, board, player): # player's turn to move
        self.winner = board.won()
        if self.winner == 'x':
            return 1 + board.count_empties() # reward fast wins
        elif self.winner == 'o':
            return -1 * (1 + board.count_empties())

        if board.is_full():
            return 0 # draw

        self.next_boards = []
        for square in range(board.square_range):
            self.new_board = deepcopy(board)
            if self.new_board.legal_move(square):
                self.new_board.update(player.symbol, square)
                self.next_boards.append(self.new_board)

        if player == self.px:
            return max(self.minimax(children, self.po) for children in self.next_boards)
        else:
            return min(self.minimax(children, self.px) for children in self.next_boards)


    def play(self):
        while True:
            self.make_move(self.game_board, self.player)
            print(self.game_board)

            if (self.game_board.won()):
                print(self.game_board.won() + ' won!')
                exit()

            if (self.game_board.is_full()):
                print('no winner')
                exit()

            self.player = self.po if self.player == self.px else self.px


if __name__ == '__main__':
    t = TicTacToe()
    t.play()

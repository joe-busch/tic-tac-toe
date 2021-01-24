class Board:
    def __init__(self):
        self.square_range = 9
        self.b = [' ' for square in range(self.square_range)]


    def __str__(self):
        disp =  ' ' + self.b[0] + ' | ' + self.b[1] + ' | ' + self.b[2] + '\n'
        disp += '-' * 11 + '\n'
        disp += ' ' + self.b[3] + ' | ' + self.b[4] + ' | ' + self.b[5] + '\n'
        disp += '-' * 11 + '\n'
        disp += ' ' + self.b[6] + ' | ' + self.b[7] + ' | ' + self.b[8] + '\n'

        return disp


    def legal_move(self, square):
        return True if self.b[square] == ' ' else False


    def update(self, player_symbol, square):
        self.b[square] = player_symbol


    def won(self):
        # check rows
        for row in range(3):
            if (self.b[3*row] == self.b[3*row + 1] == self.b[3*row + 2] != ' '):
                return self.b[3*row]

        # check columns
        for col in range(3):
            if (self.b[col] == self.b[col + 3] == self.b[col + 6] != ' '):
                return self.b[col]

        # check diagonals
        if (self.b[0] == self.b[4] == self.b[8] != ' '):
            return self.b[0]
        if (self.b[2] == self.b[4] == self.b[6] != ' '):
            return self.b[2]

        return False


    def is_full(self):
        return all([self.b[square] != ' ' for square in range(self.square_range)])


    def count_empties(self):
        return len([1 for square in range(self.square_range) if self.b[square] == ' '])

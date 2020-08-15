
class Board:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.b = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    def __str__(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(f"|{self.b[i][j]}", end="")
            print('|')
        print(" _ _ _ _ _ _ _")
        return ''
    
    def make_move(self, player, col):
        for i in reversed(range(self.rows)):
            if self.b[i][col] == ' ':
                self.b[i][col] = player.val
                return True
        return False
    
    def horizontal_win_helper(self, i, j, val):
        return self.b[i][j] == val and self.b[i][j+1] == val and self.b[i][j+2] == val and self.b[i][j+3] == val
    
    def vertical_win_helper(self, i, j, val):
        return self.b[i][j] == val and self.b[i + 1][j] == val and self.b[i + 2][j] == val and self.b[i+3][j] == val
    
    def check_horizontal_win(self, val):
        for i in range(self.rows):
            for j in range(self.cols - 3):
                if self.horizontal_win_helper(i, j, val):
                    return True
        return False
    
    def check_vertical_win(self, val):
        for j in range(self.cols):
            for i in range(self.rows - 3):
                if self.vertical_win_helper(i, j, val):
                    return True
        return False
    
    def forward_diagonal_win_helper(self, i, j, val):
        return self.b[i][j] == val and self.b[i+1][j-1] == val and self.b[i+2][j-2] == val and self.b[i+3][j-3] == val

    def backward_diagonal_win_helper(self, i, j, val):
        return self.b[i][j] == val and self.b[i+1][j+1] == val and self.b[i+2][j+2] == val and self.b[i+3][j+3] == val

    def check_forward_diagonal(self, val):
        for i in range(self.rows - 3):
            for j in reversed(range(3, self.cols)):
                if self.forward_diagonal_win_helper(i, j, val):
                    return True
        return False
    
    def check_backward_diagonal(self, val):
        for i in range(self.rows - 3):
            for j in range(self.cols - 3):
                if self.backward_diagonal_win_helper(i, j, val):
                    return True
        return False
    
    def game_is_won(self, val):
        vertical = self.check_vertical_win(val)
        horizontal = self.check_horizontal_win(val)
        diagonal = self.check_backward_diagonal(val)
        anti_diagonal = self.check_forward_diagonal(val)

        return vertical or horizontal or diagonal or anti_diagonal
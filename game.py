# ---
# Title: Python Tic-Tac-Toe Game
# Author: Harsh Sharma
# ---

import tkinter


class Board:
    def __init__(self, canvas, rows, cols, tile_size):
        self.canvas = canvas
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'
        self.winner = None

    def draw_board(self):
        for i in range(1, self.rows):
            self.canvas.create_line(i * self.tile_size, 0, i * self.tile_size, wind_height, fill="white", width=3)
        for i in range(1, self.cols):
            self.canvas.create_line(0, i * self.tile_size, wind_width, i * self.tile_size, fill="white", width=3)

    def make_move(self, row, col):
        if self.board[row][col] == ' ' and not self.winner:
            self.board[row][col] = self.current_player
            self.draw_symbol(row, col, self.current_player)
            self.check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def draw_symbol(self, row, col, symbol):
        x = col * self.tile_size + self.tile_size // 2
        y = row * self.tile_size + self.tile_size // 2
        if symbol == "X":
            self.canvas.create_text(x, y, text=symbol, font=('Arial', 50), fill='yellow')
        if symbol == "O":
            self.canvas.create_text(x, y, text=symbol, font=('Arial', 50), fill='orange')

    def check_winner(self):
        for row in range(self.rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                self.declare_winner(self.board[row][0])
                return
        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.declare_winner(self.board[0][col])
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.declare_winner(self.board[0][0])
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.declare_winner(self.board[0][2])
            return
        if all(self.board[row][col] != ' ' for row in range(self.rows) for col in range(self.cols)):
            self.declare_winner('Draw')

    def declare_winner(self, winner):
        self.winner = winner
        if winner == 'Draw':
            message = "It's a draw!"
        else:
            message = f"Player {winner} wins!"
        x = wind_width // 2
        y = wind_height // 2
        rect_width = 300
        rect_height = 100
        if self.winner == "X":
            self.canvas.create_rectangle(x - rect_width // 2, y - rect_height // 2, x + rect_width // 2, y + rect_height // 2, outline="yellow", fill="black")
            self.canvas.create_text(x, y, text=message, font=('Arial', 30), fill='yellow')
        if self.winner == "O":
            self.canvas.create_rectangle(x - rect_width // 2, y - rect_height // 2, x + rect_width // 2, y + rect_height // 2, outline="orange", fill="black")
            self.canvas.create_text(x, y, text=message, font=('Arial', 30), fill='orange')


class Game:
    def __init__(self, window, board):
        self.window = window
        self.board = board
        self.setup_game()

    def setup_game(self):
        self.board.draw_board()
        self.board.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        if not self.board.winner:
            col = event.x // (wind_width // cols)
            row = event.y // (wind_height // rows)
            self.board.make_move(row, col)


rows = 3
cols = 3
tile_size = 125

wind_width = rows * tile_size
wind_height = cols * tile_size

window = tkinter.Tk()
window.title("TIC-TAC-TOE")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=wind_width, height=wind_height, borderwidth=0, highlightthickness=0)
canvas.pack()
canvas.update()

board = Board(canvas, rows, cols, tile_size)
game = Game(window, board)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - wind_width) // 2
y = (screen_height - wind_height) // 2

window.geometry(f"{wind_width}x{wind_height}+{x}+{y}")

window.mainloop()
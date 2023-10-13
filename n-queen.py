
import tkinter as tk
from tkinter import ANCHOR, ttk

class App(ttk.Frame):
    def __init__(board, parent):
        ttk.Frame.__init__(board)

        # Make the app responsive
        for index in [0, 1, 2]:
            board.columnconfigure(index=index, weight=1)
            board.rowconfigure(index=index, weight=1)
        
        # Create widgets :)
        board.setup_widgets()

    def setup_widgets(board):
        # Create a Frame for the Checkbuttons
        board.check_frame = ttk.LabelFrame(board, text="Checkbuttons", padding=(20, 10))
        board.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )
        
        
            
            
            
            
            
def is_safe(board, row, col, N):
    # Check if no queen can attack this cell
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def display_solution(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0, N):
        return None
    return board

def update_display(board, canvas):
    N = len(board)
    cell_size = 40
    canvas.delete("all")
    for row in range(N):
        for col in range(N):
            color = "white" if (row + col) % 2 == 0 else "black"
            canvas.create_rectangle(col * cell_size, row * cell_size,
                                    (col + 1) * cell_size, (row + 1) * cell_size,
                                    fill=color)
            if board[row][col] == 1:
                canvas.create_text(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2, text="Q", fill="red")

def solve_and_display():
    N = int(spinbox.get())
    board = display_solution(N)
    if board:
        update_display(board, canvas)
    
    

# Create the GUI
window = tk.Tk()
window.title("N-Queens")

 # Simply set the theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

label = tk.Label(window, text="Enter Board Size:")
label.pack()

# entry = tk.Entry(window)
# entry.pack()

# Spinbox
spinbox = ttk.Spinbox(window, from_=0, to=100, increment=1)
spinbox.insert(1, "1")
# spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
spinbox.pack()

solve_button = tk.Button(window, text="Solve", command=solve_and_display)
solve_button.pack()

canvas = tk.Canvas(window, width=400, height=400,relief=
"solid")
canvas.pack()

window.resizable(False,True)
window.mainloop()

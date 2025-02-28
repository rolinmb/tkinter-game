import tkinter as tk
import random

GRID_SIZE = 10
CELL_SIZE = 40
BOARD_WIDTH, BOARD_HEIGHT = 15, 10
KEY_MAP = {
    "w": (0, -1), "Up": (0, -1),
    "s": (0, 1), "Down": (0, 1),
    "a": (-1, 0), "Left": (-1, 0),
    "d": (1, 0), "Right": (1, 0)
}

# Generate a random BOARD (1 = wall, 0 = empty space)
GAME_BOARD = [[random.choice([0, 1]) if (x > 0 and y > 0 and x < BOARD_WIDTH-1 and y < BOARD_HEIGHT-1) else 1 
             for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

GAME_BOARD[1][1] = 0 # ensure start position is walkable

player_x, player_y = 1, 1 # player state

root = tk.Tk()
root.title("tkinter-game")

canvas = tk.Canvas(root, width=BOARD_WIDTH * CELL_SIZE, height=BOARD_HEIGHT * CELL_SIZE, bg="black")
canvas.pack()

def draw_board():
    canvas.delete("all")
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            color = "gray" if GAME_BOARD[y][x] == 1 else "white"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, 
                                    fill=color, outline="black")
    # Draw player
    canvas.create_oval(player_x * CELL_SIZE + 10, player_y * CELL_SIZE + 10,
                        player_x * CELL_SIZE + 30, player_y * CELL_SIZE + 30,
                        fill="red")

def move_player(dx, dy):
    global player_x, player_y
    new_x, new_y = player_x + dx, player_y + dy
    if 0 <= new_x < BOARD_WIDTH and 0 <= new_y < BOARD_HEIGHT and GAME_BOARD[new_y][new_x] == 0:
        player_x, player_y = new_x, new_y
    draw_board()

def on_key_press(event):
    if event.keysym in KEY_MAP:
        move_player(*KEY_MAP[event.keysym])

root.bind("<Key>", on_key_press)

if __name__ == "__main__":
    draw_board()
    root.mainloop()
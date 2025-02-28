from consts import BOARD_HEIGHT, BOARD_WIDTH, CELL_SIZE, KEY_MAP, N_ROOMS
from gen import generate_board, find_random_start
import tkinter as tk

GAME_BOARD = generate_board(N_ROOMS)

player_x, player_y = find_random_start(GAME_BOARD)

root = tk.Tk()
root.title("tkinter-game")

canvas = tk.Canvas(root, width=BOARD_WIDTH * CELL_SIZE, height=BOARD_HEIGHT * CELL_SIZE, bg="black")
canvas.pack()

def draw_board():
    canvas.delete("all")
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            cell_color = "gray" if GAME_BOARD[y][x] == 1 else "white"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, 
                                    fill=cell_color, outline="black")
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
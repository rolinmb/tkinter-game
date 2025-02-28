import tkinter as tk
import random

GRID_SIZE = 10
CELL_SIZE = 40
MAP_WIDTH, MAP_HEIGHT = 15, 10

# Generate a random map (1 = wall, 0 = empty space)
game_map = [[random.choice([0, 1]) if (x > 0 and y > 0 and x < MAP_WIDTH-1 and y < MAP_HEIGHT-1) else 1 
             for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

game_map[1][1] = 0 # ensure start position is walkable

player_x, player_y = 1, 1 # player state

root = tk.Tk()
root.title("tkinter-game")

canvas = tk.Canvas(root, width=MAP_WIDTH * CELL_SIZE, height=MAP_HEIGHT * CELL_SIZE, bg="black")
canvas.pack()

def draw_map():
    canvas.delete("all")
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            color = "gray" if game_map[y][x] == 1 else "white"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, 
                                    fill=color, outline="black")
    # Draw player
    canvas.create_oval(player_x * CELL_SIZE + 10, player_y * CELL_SIZE + 10,
                        player_x * CELL_SIZE + 30, player_y * CELL_SIZE + 30,
                        fill="red")

def move(dx, dy):
    global player_x, player_y
    new_x, new_y = player_x + dx, player_y + dy
    if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT and game_map[new_y][new_x] == 0:
        player_x, player_y = new_x, new_y
    draw_map()

def on_key_press(event):
    key_map = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
    if event.keysym in key_map:
        move(*key_map[event.keysym])

root.bind("<KeyPress>", on_key_press)

if __name__ == "__main__":
    draw_map()
    root.mainloop()
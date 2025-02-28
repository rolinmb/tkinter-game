from consts import BOARD_HEIGHT, BOARD_WIDTH, DIRECTIONS
import random

def generate_board(n_rooms):
    board = [[1 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)] # start with all walls
    
    def carve_passages(x, y):
        """ Recursively carves passages in a depth-first manner. """
        board[y][x] = 0  # Make current cell walkable
        random.shuffle(DIRECTIONS)  # Randomize movement order
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2  # Check two steps ahead
            
            if 1 <= nx < BOARD_WIDTH - 1 and 1 <= ny < BOARD_HEIGHT - 1 and board[ny][nx] == 1:
                board[y + dy][x + dx] = 0  # Open passage
                carve_passages(nx, ny)  # Recursive step

    # Start carving from a random odd position inside the grid
    start_x, start_y = random.choice(range(1, BOARD_WIDTH, 2)), random.choice(range(1, BOARD_HEIGHT, 2))
    carve_passages(start_x, start_y)

    # Add random rooms
    num_rooms = random.randint(1, n_rooms)  # Number of rooms
    for _ in range(num_rooms):
        room_w, room_h = random.randint(2, 4), random.randint(2, 4)  # Room dimensions
        room_x, room_y = random.randint(1, BOARD_WIDTH - room_w - 1), random.randint(1, BOARD_HEIGHT - room_h - 1)
        
        for i in range(room_y, room_y + room_h):
            for j in range(room_x, room_x + room_w):
                board[i][j] = 0  # Make the room walkable

    return board

def find_random_start(board):
    walkable_positions = [(x, y) for y in range(BOARD_HEIGHT) for x in range(BOARD_WIDTH) if board[y][x] == 0]
    return random.choice(walkable_positions) if walkable_positions else (1, 1)
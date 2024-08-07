import tkinter as tk
import random
from tkinter import messagebox


master = tk.Tk()
master.geometry('595x700')
master.title("SUDOKU")

home_frame = tk.Frame(master)
home_frame.grid(row = 0, column = 0)
home_frame.tkraise()

mode_numbers = 0 # no. of initial values insert to the game
modes = {'Easy': 50, 'Medium': 35, 'Hard': 25}

grid = [[None for _ in range(9)] for _ in range(9)] # stores the buttons of the puzzles
numbers_buttons = [None for i in range(1, 10)] # stores the buttons 1 to 9
number_selected = None

mistake_count = 0
filled_array = [[None for _ in range(9)] for _ in range(9)] # stores the filled blocks of the puzzle (includes the inserted numbers too)
length_filled_array = 0


def initialize_puzzles(): # initializes 'three' different solved sudoku puzzles and takes one random puzzle for the game
    puzzle_1 = [
        [4,3,5,  2,6,9,  7,8,1],
        [6,8,2,  5,7,1,  4,9,3],
        [1,9,7,  8,3,4,  5,6,2],

        [8,2,6,  1,9,5,  3,4,7],
        [3,7,4,  6,8,2,  9,1,5],
        [9,5,1,  7,4,3,  6,2,8],

        [5,1,9,  3,2,6,  8,7,4],
        [2,4,8,  9,5,7,  1,3,6],
        [7,6,3,  4,1,8,  2,5,9],
    ]

    puzzle_2 = [
        [8,2,7,  1,5,4,  3,9,6],
        [9,6,5,  3,2,7,  1,4,8],
        [3,4,1,  6,8,9,  7,5,2],

        [5,9,3,  4,6,8,  2,7,1],
        [4,7,2,  5,1,3,  6,8,9],
        [6,1,8,  9,7,2,  4,3,5],

        [7,8,6,  2,3,5,  9,1,4],
        [1,5,4,  7,9,6,  8,2,3],
        [2,3,9,  8,4,1,  5,6,7],
    ]

    puzzle_3 = [
        [5,3,4,  6,7,8,  9,1,2],
        [6,7,2,  1,9,5,  3,4,8],
        [1,9,8,  3,4,2,  5,6,7],

        [8,5,9,  7,6,1,  4,2,3],
        [4,2,6,  8,5,3,  7,9,1],
        [7,1,3,  9,2,4,  8,5,6],

        [9,6,1,  5,3,7,  2,8,4],
        [2,8,7,  4,1,9,  6,3,5],
        [3,4,5,  2,8,6,  1,7,9],
    ]

    global answers_arr_arr
    answers_arr_arr = random.choice([puzzle_1, puzzle_2, puzzle_3])

    ans_dict_temp = {}
    for r in range(1, 10):
        for c in range(1, 10):
            ans_dict_temp["r" + str(r) + "c" + str(c)] = answers_arr_arr[r - 1][c - 1]

    global random_keys_initial # for taking no of random values from the dictionary according to the game mode
    random_keys_initial = random.sample(list(ans_dict_temp.keys()), mode_numbers)


def initialize_random_numbers(): # for inserting no of 'random values' from the puzzle 'initially' to the game based on the 'mode' 
    global  random_keys_initial_new
    random_keys_initial_new = []
    for i in random_keys_initial:
        val = i.replace('r', '').replace('c', '')
        random_keys_initial_new.append(val)

    for i in random_keys_initial_new:
        r, c = int(i[0]) - 1, int(i[-1]) - 1
        button = grid[r][c]
        filled_array[r][c] = answers_arr_arr[r][c]
        button['text'] = answers_arr_arr[r][c] # insertion of the numbers by changing button['text']
        button['state'] = "disabled"


def on_grid_click(r, c): # 'button click' event for 'inserting' the 'selected button' into the puzzle
    grid_selected_button = grid[r][c]

    if number_selected != None: grid_selected_button["text"] = number_selected
    else: 
        messagebox.showwarning("Choose a Number", "Select a Number from the buttons below 1 - 9 to insert the number into the puzzle")
        return

    global mistake_count
    global length_filled_array

    
    if mistake_count < 4:
        length_filled_array = 0
        if str(answers_arr_arr[r][c]) != str(number_selected):
            grid_selected_button['fg'] = 'red' # Displays a 'red' foregrounded number if the number is not placed in the correct position
            mistake_count += 1
            game_mistake_label['text'] = "Mistakes = " + str(mistake_count) + "/5"
        else: 
            grid_selected_button['fg'] = 'blue' # Displays a 'blue' foregrounded number if the number is not placed in the correct position
            filled_array[r][c] = answers_arr_arr[r][c]
            for i in range(9): 
                    for j in range(9):
                        if filled_array[i][j] != None: length_filled_array += 1 # Checks the no. of filled boxes so that it can display 'Solved' messagebox after finishing the puzzle
            if length_filled_array == 81: messagebox.showinfo("Solved", "Congrats! you've Solved the puzzle")
    else:
        grid_selected_button['fg'] = 'red'
        messagebox.showwarning("Sudoku Closing...", "You've exceeded the no. of mistakes(=5)\nPlease re-launch the Game")
        master.destroy()


def initialize_game_sudoku_grid(game_frame): # Displaying the puzzle buttons in the grid
    y, z = 0, 0
    list_gaps = [4, 7, 10]

    for r in range(1, 10):
        if r in list_gaps: y += 1
        for c in range(1, 10):
            button = tk.Button(game_frame, borderwidth=1, relief ="solid", font="Arial", width=5, height=2, command=lambda row=r - 1, col=c - 1: on_grid_click(row, col))
            if c in list_gaps: z += 1

            button.grid(row=r + y, column=c+z)
            grid[r - 1][c - 1] = button
        z = 0


def initialize_gaps_sudoku_grid(game_frame): # Leaves a 'gap' between every 9 blocks of the grid (for user simplicity)
    space, gap = 2.5, 0
    list_gaps = [0, 4, 8, 12]
    for i in list_gaps:
        canvasR = tk.Canvas(game_frame, width=gap, height=space)
        canvasR.grid(row = i, columnspan = 15)

        canvasC = tk.Canvas(game_frame, height=gap, width=space)
        canvasC.grid(column=i, rowspan=15)


def initialize_game_label(game_frame): # Shows no. of 'mistakes' done in 'label'
    global game_mistake_label
    game_mistake_label = tk.Label(game_frame, text = "Mistakes = 0/5", font = 'Arial 16')
    game_mistake_label.grid(row = 14, columnspan=15)


def on_number_click(index_number_selected): # button click event for buttons(numbers 1 to 9)
    global number_selected
    number_selected = range(1, 10)[index_number_selected]
    for i in range(1, 10):
        button = numbers_buttons[i - 1]
        if i != number_selected: button["bg"] = "white"
        else: button["bg"] = "green" # for highlighting the selected number


def initialize_input_buttons(game_frame): # initializes input buttons 1 - 9
    z = 0
    for c in range(1, 10):
        if c in [4, 7, 10]:
            z += 1
        btn = tk.Button(game_frame, text = str(c), relief="raised", padx = 4, pady=0.5, command=lambda index = c: on_number_click(index - 1), font='Arial 20')
        numbers_buttons[c - 1] = btn
        btn.grid(row=15, column = c+z, pady = (10, 20))


def game_FRAME(game_frame): # Contains all the functions involving 'game_frame'
    initialize_puzzles()
    initialize_game_sudoku_grid(game_frame)
    initialize_gaps_sudoku_grid(game_frame)
    initialize_game_label(game_frame)
    initialize_input_buttons(game_frame)
    initialize_random_numbers()


def initialize_home_labels(): # Initializes labels in the 'home_frame'
    intro_label = tk.Label(master, text="Welcome to SUDOKU!", font='Arial 24', anchor='center')
    intro_label.place(x=130, y=150)

    intro_label = tk.Label(master, text="Select a Mode to play", font='Arial 16', anchor='center')
    intro_label.place(x=180, y=300)


def mode(index): # Button click event for selecting game-mode level
    game_frame = tk.Frame(master)
    global mode_numbers
    mode_numbers = list(modes.values())[index]

    game_FRAME(game_frame)

    game_frame.grid(row=0, column=0)
    game_frame.tkraise()


def initialize_home_buttons(): # Initializes buttons in the 'home_frame'
    mode_buttons = [None for i in range(3)]
    placeX, placeY = 150, 350

    for i in range(3):
        button = tk.Button(master, text=list(modes.keys())[i], width=10, height=2, command=lambda index=i: mode(index))
        button.place(x=placeX, y=placeY)
        mode_buttons[i] = button
        placeX += 100


initialize_home_labels()
initialize_home_buttons()

master.mainloop()
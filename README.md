# Sudoku Game

This is a Sudoku game implemented using Python and Tkinter. The game allows users to select different difficulty levels and play Sudoku with a graphical user interface.

## Features

- **Three Difficulty Levels**: Easy, Medium, and Hard.
- **Graphical User Interface**: Built using Tkinter.
- **Mistake Counter**: Tracks the number of mistakes made by the player.
- **Random Puzzle Generation**: Initializes different Sudoku puzzles for each game.

## Project Structure

## Key Components

- **[`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\tendu\Desktop\Chandu Files\Programming\Python\Sudoku\main.py")**: The main script that initializes and runs the Sudoku game.
  - [`initialize_puzzles()`](command:_github.copilot.openSymbolFromReferences?%5B%22initialize_puzzles()%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A25%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Initializes three different solved Sudoku puzzles and selects one randomly for the game.
  - [`initialize_random_numbers()`](command:_github.copilot.openSymbolFromReferences?%5B%22initialize_random_numbers()%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A80%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Inserts a number of random values into the puzzle based on the selected mode.
  - [`initialize_game_sudoku_grid(game_frame)`](command:_github.copilot.openSymbolFromReferences?%5B%22initialize_game_sudoku_grid(game_frame)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A126%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Displays the puzzle buttons in the grid.
  - [`initialize_gaps_sudoku_grid(game_frame)`](command:_github.copilot.openSymbolFromReferences?%5B%22initialize_gaps_sudoku_grid(game_frame)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A141%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Leaves gaps between every 9 blocks of the grid for user simplicity.
  - [`initialize_game_label(game_frame)`](command:_github.copilot.openSymbolFromReferences?%5B%22initialize_game_label(game_frame)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A152%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Shows the number of mistakes made by the player.
  - [`game_FRAME(game_frame)`](command:_github.copilot.openSymbolFromReferences?%5B%22game_FRAME(game_frame)%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A177%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Contains all the functions involving the game frame.
  - [`initialize_home_labels()`](command:_github.copilot.openSymbolFromReferences?%5B%22initialize_home_labels()%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Ctendu%5C%5CDesktop%5C%5CChandu%20Files%5C%5CProgramming%5C%5CPython%5C%5CSudoku%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Ftendu%2FDesktop%2FChandu%2520Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ftendu%2FDesktop%2FChandu%20Files%2FProgramming%2FPython%2FSudoku%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A186%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Initializes labels in the home frame.

## How to Run

1. Ensure you have Python installed on your system.
2. Install Tkinter if not already installed:
   ```sh
   sudo apt-get install python3-tk

python main.py
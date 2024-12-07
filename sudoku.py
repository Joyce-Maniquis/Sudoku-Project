import sys
import pygame
from Cell import *
from sudoku_generator import *
from Board import *
from sudoku_ui import *

def begin(screen):
    # Allows the user to choose game difficulty and assigns the number of blank cells
    diff = draw_game_start(screen)
    if diff == "easy":
        sudoku_list = generate_sudoku(9, 30)
    elif diff == "med":
        sudoku_list = generate_sudoku(9, 40)
    elif diff == "hard":
        sudoku_list = generate_sudoku(9, 50)

    # Draws sudoku board according difficulty
    screen.fill(WHITE)
    board = Board(540, 540, screen, diff, sudoku_list)
    board.draw()
    menu(screen)

    return sudoku_list, board

def main():
    # Initializes the game and starting screen
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))

    # Moves onto the main sudoku board screen
    sudoku_list, board = begin(screen)
    pygame.display.flip()
    playing = True

    # Implements main game mechanics of sudoku
    while playing:
        for event in pygame.event.get():

            # Safely exits the program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Gets the coordinates of the mouse click
                screen.fill(WHITE)
                x, y = event.pos
                coord = board.click(x, y)

                # Outlines the current cell with red if the click was on the board
                if coord is not None:
                    x, y = coord
                    board.select(x,y)
                    board.draw()
                    menu(screen, coord)

                # Checks if a UI button was pressed
                button_check = menu(screen, event.pos)

                # Resets the sudoku board to its original state
                if button_check == "reset":
                    board.reset_to_original()
                    board.draw()

                # Goes back to the game start screen
                elif button_check == "restart":
                    sudoku_list, board = begin(screen)
                pygame.display.flip()

            elif event.type == pygame.KEYDOWN:
                if board.selected_cell is not None:

                    # Gets the row and column of the current selected cell
                    original_pos = board.inv_cells[board.selected_cell]
                    r, c = original_pos

                    # Changes the selected cell if the user uses the arrow keys
                    if event.key == pygame.K_DOWN and r != 9:
                        r += 1
                    elif event.key == pygame.K_UP and r != 1:
                        r -= 1
                    elif event.key == pygame.K_LEFT and c != 1:
                        c -= 1
                    elif event.key == pygame.K_RIGHT and c != 9:
                        c += 1

                    # Sketches numbers at the top left of the selected cell
                    elif event.unicode.isdigit() and int(event.unicode) > 0 and board.selected_cell.original == False:
                        board.sketch(event.unicode)

                    # Solidifies a sketch when the enter key is pressed and checks if the board is full for a win
                    elif event.key == pygame.K_RETURN:
                        board.place_number()
                        done = board.is_full()
                        if done:
                            win = board.check_board()
                            playing = False

                    # Erases a sketch or solidified value if the cell was not part of the original board
                    elif event.key == pygame.K_BACKSPACE:
                        board.clear()

                    # Updates the board
                    screen.fill(WHITE)
                    board.select(r, c)
                    board.draw()
                    menu(screen)
                    pygame.display.flip()

    while not playing:

        # Loads one of two ending screens
        if win:
            load_win(screen)
        else:
            load_game_over(screen)
        pygame.display.flip()

        # Allows the user to exit or restart the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if win:
                    load_win(screen, event.pos)
                else:
                    button_check = load_game_over(screen, event.pos)
                    if button_check == "restart":
                        main()

if __name__ == "__main__":
    main()
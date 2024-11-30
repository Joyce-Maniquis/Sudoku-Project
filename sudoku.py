from Cell import *
from sudoku_generator import *
from Board import *
from sudoku_ui import *

def main():
    # Initializes screen
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))
    diff = draw_game_start(screen)

    # Generates a sudoku board according to the player's chosen difficulty
    if diff == "easy":
        sudoku_list = generate_sudoku(9, 30)
    elif diff == "med":
        sudoku_list = generate_sudoku(9, 40)
    elif diff == "hard":
        sudoku_list = generate_sudoku(9, 50)

    # Sets the screen for the main portion of the game
    screen.fill((WHITE))
    board = Board(540, 540, screen, diff)
    board.draw()
    menu(screen)

    '''
    board.select(3, 2)
    pygame.display.flip()
    
    for i in range(9):
        for j in range(9):
            board.select(i, j)
            board.place_number(sudoku_list[i][j])
            board.update_board()
    pygame.display.flip()

    '''

    '''
    #using own code
    screen.fill((WHITE))
    for i in range(9):
        for j in range(9):
            cur = Cell(sudoku_list[i][j], i, j, screen)
            cur.draw()
    pygame.display.flip()
    pygame.time.delay(8000)

    continue_game = True
    while continue_game:
        reset = False

        if reset:

        elif restart:

        elif exit:
            continue_game = False
        else:

    '''

if __name__ == "__main__":
    main()
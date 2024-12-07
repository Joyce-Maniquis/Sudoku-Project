import pygame
from Cell import *


class Board:
    def __init__(self, width, height, screen, difficulty, sudoku_list):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.sudoku_list = sudoku_list
        self.cells = {}
        self.inv_cells = {}
        self.selected_cell = None
        for i in range(9):
            for j in range(9):
                value = self.sudoku_list[i][j]
                cell = Cell(value, i, j, self.screen)
                self.cells[(i + 1, j + 1)] = cell

        for i in self.cells:
            self.inv_cells[self.cells[i]] = i

    # draws the board and updates cells
    def draw(self):
        size = 60
        pygame.draw.line(self.screen, "black", (0, 0), (540, 0), 5)
        pygame.draw.line(self.screen, "black", (0, 0), (0, 540), 5)
        for i in range(9):
            if i == 2 or i == 5 or i == 8:
                w = 5
            else:
                w = 2
            pygame.draw.line(self.screen, "black", (size, 0), (size, 540), w)
            pygame.draw.line(self.screen, "black", (0, size), (540, size), w)
            size += 60

        for cell in self.cells.values():
            cell.draw()

    # turns a cell into a selected cell and then updates the selected cell using cell.draw()
    def select(self, row, col):
        if self.selected_cell is not None:
            self.selected_cell.selected = False
        self.selected_cell = self.cells.get((row, col))
        self.selected_cell.selected = True
        #self.selected_cell.draw()

    # returns the row and column of a cell given the pixel coordinates
    def click(self, x, y):
        if 0 < x < self.width and 0 < y < self.height:
            row = y // (60) + 1
            col = x // (60) + 1
            return (row, col)
        return None

    # clears the selected cells value and sketched value
    def clear(self):
        for cell in self.cells.values():
            if cell.selected:
                cell.set_cell_value(0)
                cell.set_sketch_value(0)
                cell.draw()

    # sketches the given value into the selected cell
    def sketch(self, value):
        for cell in self.cells.values():
            if cell.selected:
                cell.set_sketch_value(value)
                cell.draw()

    # sets the cell value to the value provided
    def place_number(self, value):
        for cell in self.cells.values():
            if cell.selected:
                cell.set_cell_value(value)

    # sets all sketch values to 0
    def reset_to_original(self):
        for cell in self.cells.values():
            cell.set_sketch_value(0)

    # checks if there are any cells with value 0
    def is_full(self):
        for cell in self.cells.values():
            if cell.value == 0:
                return False
            return True

    # draws every cell to update them
    def update_board(self):
        for cell in self.cells.values():
            cell.draw()

    # returns the row and column of the first cell with value 0
    def find_empty(self):
        for i in self.cells:
            if self.cells[i].value == 0:
                return i

    # checks to see if the sudoku is correctly filled in
    def check_board(self):
        line = set()
        for y in range(1, 10):
            for x in range(1, 10):
                if self.cells[(x, y)].value not in line:
                    line.add(self.cells[(x, y)].value)
                else:
                    return False
            line = set()

        for x in range(1, 10):
            for y in range(1, 10):
                if self.cells[(x, y)].value not in line:
                    line.add(self.cells[(x, y)].value)
                else:
                    return False
            line = set()

        box = set()

        for outer_x in range(3):
            for outer_y in range(3):
                for dx in range(3):
                    for dy in range(3):
                        x = (outer_x * 3 + dx) + 1
                        y = (outer_y * 3 + dy) + 1
                        if self.cells[(x, y)].value not in box:
                            box.add(self.cells[(x, y)].value)
                        else:
                            return False
                box = set()

        return True

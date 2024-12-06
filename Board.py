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
        self.selected_cell = None

    #draws the board and updates cells
    def draw(self):
        size = 60
        pygame.draw.line(self.screen, "black", (0, 0), (540, 0), 5)
        pygame.draw.line(self.screen, "black", (0, 0), (0, 540), 5)
        for i in range(9):
            if i == 2 or i == 5 or i ==8:
                w=5
            else:
                w=2
            pygame.draw.line(self.screen, "black", (size , 0), (size, 540), w)
            pygame.draw.line(self.screen, "black", (0, size), (540, size), w)
            size += 60
        n = 1
        for i in range(9):
            for j in range(9):
                x = i+1
                y = j+1
                self.cells[n] = Cell(0,x,y,self.screen)
                self.cells[n+1] = (x,y)
                self.cells[n].draw()
                n += 2
        n = 1
        for i in range(9):
            for j in range(9):
                x, y = i * 60, j * 60
                value = self.sudoku_list[i][j]
                cell = Cell(value, i, j, self.screen)
                self.cells[(i + 1, j + 1)] = cell
                cell.draw()

    #turns a cell into a selected cell and then updates the selected cell using cell.draw()
    def select(self, row, col):
        if selected_cell is not None:
            selected_cell.selected = False
        selected_cell = self.cells.get(((row), (col)))
        selected_cell.selected = True
        selected_cell.draw()

    #returns the row and column of a cell given the pixel coordinates
    def click(self, x, y):
        if 0 < x < self.width and 0 < y < self.height:
            row = y // (60) + 1
            col = x // (60) + 1
            return (row, col)
        return None

    #clears the selected cells value and sketched value
    def clear(self):
        for i in range(1,162,2):
            if self.cells[i].selected is True:
                self.cells[i].set_cell_value(0)
                self.cells[i].set_sketch_value(0)
                self.cells[i].draw()

    #sketches the given value into the selected cell
    def sketch(self, value):
        for i in range(1,162,2):
            if self.cells[i].selected is True:
                self.cells[i].set_sketch_value(value)
                self.cells[i].draw()

    #sets the cell value to the value provided
    def place_number(self,value):
        for i in range(1,162,2):
            if self.cells[i].selected is True:
                self.cells[i].set_cell_value(value)

    #sets all sketch values to 0
    def reset_to_original(self):
        for i in range(1, 162, 2):
            self.cells[i].set_sketch_value(0)

    #checks if there are any cells with value 0
    def is_full(self):
        for i in range(1, 162, 2):
            if self.cells[i].value == 0:
                return False
            return True

    #draws every cell to update them
    def update_board(self):
        for i in range(1, 162, 2):
            self.cells[i].draw()

    #returns the row and column of the first cell with value 0
    def find_empty(self):
        for i in range(1, 162, 2):
            if self.cells[i].value == 0:
                return self.cells[i+1]

    #checks to see if the sudoku is correctly filled in
    def check_board(self):
        row = []
        for i in range(1,146,18):
            for j in range(i,17+i, 2):
                if self.cells[j].value not in row:
                    row.append(self.cells[j].value)
                else:
                    return False
            row = []
        col = []
        for i in range (1,18,2):
            for j in range(i, 1 + i+18*8,18):
                if self.cells[j].value not in col:
                    col.append(self.cells[j].value)
                else:
                    return False
            col = []
        box = []
        for l in range (1,14, 6):
            for k in range (l, 1 + l+18*8, 18):
                for i in range (k,k+37,18):
                    for j in range(i, i+5,2):
                        if self.cells[j].value not in box:
                            box.append(self.cells[j].value)
                        else:
                            return False
                box = []
        return True


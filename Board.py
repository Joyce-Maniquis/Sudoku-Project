import pygame

from Cell import Cell
from Cell import Cell_size

cells = {}
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    #draws the board and updates cells
    def draw(self):
        size = 60
        for i in range(9):
            if i == 2 or i == 5:
                w=5
            else:
                w=3
            pygame.draw.line(self.screen, "black", (size , 0), (size, 540), w)
            pygame.draw.line(self.screen, "black", (0, size), (540, size), w)
            size+= 60
        n = 1
        for i in range(9):
            for j in range(9):
                x = i+1
                y = j+1
                cells[n] = Cell(0,x,y,self.screen)
                cells[n+1] = (x,y)
                cells[n].draw()
                n += 2

    #turns a cell into a selected cell and then updates the selected cell using cell.draw()
    def select(self, row, col):
        for i in range(1,162,2):
            cells[i+1].selected = False
        cell_num = list(cells.values()).index((row, col))
        selected_cell = cells[cell_num]
        selected_cell.selected = True
        selected_cell.draw()

    #returns the row and column of a cell given the pixel coordinates
    def click(self, row, col):
        if 0 < row < self.width and 0 < col <self.height:
            pos = (row,col)
            clicked_cell = [i for i in cells if i.rect.collidepoint(pos)]
            for key, value in cells.items():
               if value == clicked_cell:
                  place = key
                  return cells[place + 1]
        return None

    #clears the selected cells value and sketched value
    def clear(self):
        for i in range(1,162,2):
            if cells[i].selected is True:
                cells[i].set_cell_value(0)
                cells[i].set_sketch_value(0)
                cells[i].draw()

    #sketches the given value into the selected cell
    def sketch(self, value):
        for i in range(1,162,2):
            if cells[i].selected is True:
                cells[i].set_sketch_value(value)
                cells[i].draw()

    #sets the cell value to the value provided
    def place_number(self,value):
        for i in range(1,162,2):
            if cells[i].selected is True:
                cells[i].set_cell_value(value)

    #sets all sketch values to 0
    def reset_to_original(self):
        for i in range(1, 162, 2):
            cells[i].set_sketch_value(0)

    #checks if there are any cells with value 0
    def is_full(self):
        for i in range(1, 162, 2):
            if cells[i].value == 0:
                return False
            return True

    #draws every cell to update them
    def update_board(self):
        for i in range(1, 162, 2):
            cells[i].draw()

    #returns the row and column of the first cell with value 0
    def find_empty(self):
        for i in range(1, 162, 2):
            if cells[i].value == 0:
                return cells[i+1]

    #checks to see if the sudoku is correctly filled in
    def check_board(self):
        row = []
        for i in range(1,146,18):
            for j in range(i,17+i, 2):
                if cells[j].value not in row:
                    row.append(cells[j].value)
                else:
                    return False
            row = []
        col = []
        for i in range (1,18,2):
            for j in range(i, 1 + i+18*8,18):
                if cells[j].value not in col:
                    col.append(cells[j].value)
                else:
                    return False
            col = []
        box = []
        for l in range (1,14, 6):
            for k in range (l, 1 + l+18*8, 18):
                for i in range (k,k+37,18):
                    for j in range(i, i+5,2):
                        if cells[j].value not in box:
                            box.append(cells[j].value)
                        else:
                            return False
                box = []
        return True

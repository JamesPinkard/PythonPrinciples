"""
Clone of 2048 game.
"""

import poc_2048_gui
from random import randint

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

def merge(line):
    '''
    Function to merge cells that are equal.
    '''
    my_cell = 0
    result_list = [my_cell for cell in line]
    my_index = 0
    merge_flag = False
    check_cell = 0
    for cell in line:
        if cell != 0:
            if cell == check_cell:
                if merge_flag == False:
                    result_list[my_index-1] += cell
                    merge_flag = True
                elif merge_flag == True:
                    result_list[my_index] = cell
                    check_cell = cell
                    my_index += 1
                    merge_flag = False
            else:
                result_list[my_index] = cell
                check_cell = cell
                my_index += 1
                merge_flag = False
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        
        row_indexes = range(0, grid_height)
        col_indexes = range(0, grid_width)
        
        up_initial_cells = [(0,col) for col in col_indexes]
        down_initial_cells = [(grid_height -1, col) for col in col_indexes]
        left_initial_cells = [(row, 0) for row in row_indexes]
        right_initial_cells = [(row, grid_width - 1) for row in row_indexes]
        
        self._move_dict = {UP: up_initial_cells,
                    DOWN: down_initial_cells,
                    LEFT: left_initial_cells,
                    RIGHT: right_initial_cells}
        self.reset()
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        my_row = 0 
        my_column = 0
        self._grid = [[my_column for cell in range(self._grid_width)] 
                     for cell in range(self._grid_height)]
            
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        txt = ""
        for row in self._grid:
            txt += str(row) + "\n"
        return txt
        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        
        return self._grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_tiles = self._move_dict[direction]
        offset = OFFSETS[direction]
        tile_moved = False
        
            
        for tile in initial_tiles:
            
            initial_row = tile[0]
            initial_column = tile[1]
            
            temp_list = []
            temp_indices = []
            
            if direction == UP or DOWN:
                range_field = self._grid_height
            elif direction == LEFT or RIGHT:
                range_field = self._grid_width
                
            for tile in range(range_field):
                temp_indices.append((initial_row,initial_column))
                
                offset_value = self._grid[initial_row][initial_column]
                temp_list.append(offset_value)
            
                initial_row+= offset[0]
                initial_column+= offset[1]
                
            merged_list = merge(temp_list)
            
            temporary_index = 0
            for initial_row,initial_column in temp_indices:
                self._grid[initial_row][initial_column] = merged_list[temporary_index]
                temporary_index += 1
            
            for temp, merged in zip(temp_list, merged_list):
                if temp != merged:
                    tile_moved = True
        
        if tile_moved ==True:
            self.new_tile()
                
            
            
                
            
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        index_row = randint(0,self._grid_height - 1)
        index_col = randint(0,self._grid_width - 1)
        current_cell = self._grid[index_row][index_col]
        
        if current_cell == 0:
            two_or_four = randint(1,10)
            if two_or_four != 10:
                self._grid[index_row][index_col] = 2
            elif two_or_four == 10:
                self._grid[index_row][index_col] = 4
            else:
                print("New Tile Error")
        else:
            self.new_tile()
            

        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self._grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self._grid[row][col]
                
                
                
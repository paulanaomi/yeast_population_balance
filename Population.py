import math
import pandas as pd
from Cell import *

class Population:
    def __init__(self, num_cells, mu = 5.1, sigma = 0.7):
        self.num_cells = num_cells
        self.mu = mu
        self.sigma = sigma
        self.cells = []

        max_cell_size = math.ceil(mu+2*sigma)
        self.max_axis_value = max_cell_size * num_cells + 1

        for _ in range(self.num_cells):
            self.cells.append(Cell(self.mu, self.sigma, self.max_axis_value))

    def get_num_cells(self):
        return self.num_cells

    def return_df(self):
        data = []
        for cell in self.cells:
            data.append({"size":cell.size, "x":cell.x, "y":cell.y})
        df = pd.DataFrame(data)
        return df

    def calc_distance(self,ia,ib):
        a = self.cells[ia]
        b = self.cells[ib]
        return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

    def print_cell(self, cell_idx):
        cell = self.cells[cell_idx]
        print("Cell {}: size = {}, x = {}, y = {}".format(cell_idx, cell.size, cell.x, cell.y))

    def find_close_pairs(self):
        df = self.return_df()
        df2 = pd.DataFrame(np.sqrt(df["x"] * df["x"] + df["y"] * df["y"]), columns=['distance'])
        df2.sort_values('distance', inplace=True)
        distances = df2.diff()
        short_distances = list(distances[distances['distance'] < 14].index)

        close_tuples = []
        for r1 in short_distances:
            row_number = df2.index.get_loc(r1)
            r2 = int(df2.iloc[row_number - 1].name)
            result = self.calc_distance(r1, r2) < self.cells[r1].size + self.cells[r2].size
            if result:
                close_tuples.append((r1, r2))

        return close_tuples
import random
import numpy as np

class Cell:
    def __init__(self, mean, stddev,max_axis_value):
        self.size = round(float(np.random.normal(mean, stddev)),1)
        self.x = random.randint(0,max_axis_value)
        self.y = random.randint(0,max_axis_value)
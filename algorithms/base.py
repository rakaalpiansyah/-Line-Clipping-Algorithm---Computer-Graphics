from abc import ABC, abstractmethod

class LineClipper(ABC):
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    @abstractmethod
    def clip(self, x1, y1, x2, y2):
        pass
import math
from typing import Self


class Punto():
    def __init__(self, x: float, y:float):
        # _x, _y son atributos privados.
        self._x:float = x
        self._y:float = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y,'punto'))

    def __sub__(self, other: Self) -> Self:
        """
        Vector como resta de puntos
        """
        return Vector(self.x - other.x, self.y - other.y)

    def distance(self, other: Self) -> float
        """
        Distancia entre dos puntos
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self) -> str:
        return f'P({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x:.4f}, {self.y:.4f})'

    
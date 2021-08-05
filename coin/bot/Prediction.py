from enum import Enum


class Prediction(Enum):
    STRONG_UP = 2
    UP = 1
    NOTHING = 0
    DOWN = -1
    STRONG_DOWN = -2

from enum import IntEnum, EnumMeta, auto

CELLSIZE = 32


class ConstantsEnumMeta(EnumMeta):
    def __contains__(cls, item):
        return item in cls.__members__.values()


class MOVES(IntEnum, metaclass=ConstantsEnumMeta):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class CELL(IntEnum):
    EMPTY = auto()
    WALL = auto()
    UNKNOWN = auto()
    PLAYER = auto()

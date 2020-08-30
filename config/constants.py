from enum import IntEnum, EnumMeta, auto, Enum

CELLSIZE = 32
QUIT = -1


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


class COLORS(Enum):
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    MEDIUM_GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)

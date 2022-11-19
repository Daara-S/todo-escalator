from enum import IntEnum


class Priority(IntEnum):
    must = 4
    should = 3
    could = 2
    default = 1
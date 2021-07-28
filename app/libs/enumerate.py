from enum import Enum, auto


class ContestType(Enum):
    ACM = 1


class ContestState(Enum):
    BEFORE_START = 1
    RUNNING = 2
    ENDED = 3


class ScoreboardState(Enum):
    NORMAL = 1
    FROZEN = 2


class UserPermission(Enum):
    NORMAL = 0
    ADMIN = 1


class JudgeResult(Enum):
    PENDING = auto()
    RUNNING = auto()
    AC = auto()  # accepted
    WA = auto()  # wrong answer
    TLE = auto()  # time limit exceed
    MLE = auto()  # memory limit exceed
    CE = auto()  # compilation error
    RE = auto()  # runtime error
    PE = auto()  # presentation error
    SE = auto()  # system error
    SpiderError = auto() # spider error
    UNKNOWN = auto()


class QuestStatus(Enum):
    INQUEUE = auto()
    RUNNING = auto()
    FINISHED = auto()
    FAILED = auto()


class CodeLanguage(Enum):
    C = auto()
    CPP = auto()
    JAVA = auto()
    PYTHON3 = auto()
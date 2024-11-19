import datetime
from dataclasses import dataclass, field
from enum import Enum


class LogType(Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class LogContent:
    log_type: LogType
    msg: str
    traceback: str = ""
    cur_time: datetime.datetime = field(default_factory=datetime.datetime.now)

    def __str__(self):
        result = f"Log type: {self.log_type.value}, Time: {self.cur_time}, Message: {self.msg}"
        if self.traceback:
            result += f", Traceback: {self.traceback}"
        return result

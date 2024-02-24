from . import mkdir
from . import ls
from . import cat
from . import tail

COMMANDS = {
    "cat": cat.handle,
    "ls": ls.handle,
    "mkdir": mkdir.handle,
    "tail": tail.handle
}

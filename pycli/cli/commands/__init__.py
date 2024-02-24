from . import mkdir
from . import ls
from . import cat

COMMANDS = {
    "cat": cat.handle,
    "ls": ls.handle,
    "mkdir": mkdir.handle
}

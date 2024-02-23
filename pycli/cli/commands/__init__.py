from . import mkdir
from . import ls

COMMANDS = {
    "mkdir": mkdir.handle,
    "ls": ls.handle
}

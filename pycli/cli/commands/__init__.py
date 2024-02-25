from . import mkdir
from . import ls
from . import cat
from . import tail
from . import less
from . import wc

COMMANDS = {
    "cat": cat.handle,
    "less": less.handle,
    "ls": ls.handle,
    "mkdir": mkdir.handle,
    "tail": tail.handle,
    "wc": wc.handle
}

from . import hello_world
from . import ls

COMMANDS = {
    "hello-world": hello_world.handle,
    "ls": ls.handle
}

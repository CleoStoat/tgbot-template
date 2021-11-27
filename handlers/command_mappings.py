from handlers.command_handlers import help as help_cmd
from handlers.command_handlers import start
from handlers.command_handlers import settings


COMMAND_MAPPINGS = {
    "help": help_cmd.cmd,
    "start": start.cmd,
    "settings": settings.cmd,
}
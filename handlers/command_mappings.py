from handlers.command_handlers import help as help_cmd
from handlers.command_handlers import start
from handlers.command_handlers import settings
from handlers.command_handlers import new_code


COMMAND_MAPPINGS = {
    "help": help_cmd.cmd,
    "start": start.cmd,
    "settings": settings.cmd,
    "new_code": new_code.cmd,
}
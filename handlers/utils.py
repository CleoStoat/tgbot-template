from functools import partial
from typing import Tuple

from telegram.botcommand import BotCommand
from telegram.botcommandscope import BotCommandScope
from telegram.ext import Updater
from telegram.ext.commandhandler import CommandHandler

from handlers.handler_model import CommandModel
from db.unit_of_work import AbstractUnitOfWork
import config


def set_bot_commands(
    commands: list[CommandModel], updater: Updater, uow: AbstractUnitOfWork
) -> None:
    command_handlers: list[CommandHandler] = []
    bot_commands: list[BotCommand | Tuple[str, str]] = []

    dispatcher = updater.dispatcher

    for cmd in commands:
        handler = CommandHandler(
                command=cmd.name,
                callback=partial(cmd.callback, uow=uow),
        )
        dispatcher.add_handler(handler, group=cmd.priority)
        

    bot_commands = [
        BotCommand(
                    command=cmd.name,
                    description=cmd.description,
        )
        for cmd in sorted(commands, key=lambda c: c.priority)
        if not cmd.hidden
    ]
    
    scope_type = config.get_command_scope()
    scope = None

    if scope_type:
        scope = BotCommandScope(type=scope_type)

    updater.bot.setMyCommands(commands=bot_commands, scope=scope)

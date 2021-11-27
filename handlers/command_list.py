from handlers.handler_model import CommandModel


COMMANDS = [
    CommandModel(
        priority=200,
        callback=lambda x: None,
        name="command_name",
        description="The description of the command",
        hidden=True,
    ),
]

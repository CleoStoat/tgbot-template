from handlers.handler_model import CommandModel


COMMANDS = [
    CommandModel(
        priority=200,
        name="help",
        description="Get help",
        hidden=True,
    ),
    CommandModel(
        priority=200,
        name="start",
        description="Start the bot",
        hidden=True,
    ),
    CommandModel(
        priority=200,
        name="settings",
        description="Settings for this bot",
        hidden=True,
    ),
]

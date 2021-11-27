from handlers.handler_model import CommandModel


COMMANDS = [
    CommandModel(
        priority=200,
        name="help",
        description="Get help",
    ),
    CommandModel(
        priority=200,
        name="start",
        description="Start the bot",
    ),
    CommandModel(
        priority=200,
        name="settings",
        description="Settings for this bot",
    ),
]

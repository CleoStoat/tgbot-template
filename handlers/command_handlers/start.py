from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
from db.unit_of_work import AbstractUnitOfWork

def start_cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    text = f"You started the template bot!"
    update.effective_message.reply_text(text=text, quote=True)

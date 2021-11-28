from datetime import datetime
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
from db.model import UserCode, UserInfo

from db.unit_of_work import AbstractUnitOfWork


def cmd(
    update: Update, context: CallbackContext, uow: AbstractUnitOfWork
) -> None:
    user_id = update.effective_user.id

    with uow:
        user_info = uow.repo.find_user_info(user_id)
        if user_info is None:
            user_info = UserInfo(
                user_id=user_id,
                first_name=update.effective_user.first_name,
                last_name=update.effective_user.last_name,
                username=update.effective_user.username,
                money=0.0,
                last_updated=datetime.now(),
                active=True,
            )
            uow.repo.add_user_info(user_info)

        uow.repo.set_user_active(user_id, not user_info.active)
        uow.repo.update_user_info_last_updated(user_id, datetime.now())

        active_str = "active" if user_info.active else "inactive"
        text = f"You're now {active_str}"
        update.effective_message.reply_text(text=text, quote=True)
        uow.commit()

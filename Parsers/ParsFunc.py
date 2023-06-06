from pyrogram import Client


async def get_account_dialogs(app):
    dialogs = []
    async for dialog in app.get_dialogs(limit=17):
        # print(dialog.unread_messages_count)
        if dialog.unread_messages_count != 0:
            dialogs.append(dialog.chat.username)



    user_answer = await get_count_message_for_dialog(app, dialogs)
    # print(user_answer)

    return user_answer


async def get_count_message_for_dialog(app, dialogs):
    first_mes_answer_user = []
    for dialog in dialogs:
        mes_count = await app.get_chat_history_count(dialog)

        if mes_count > 1 and mes_count < 13:
            # print(mes_count)
            first_mes_answer_user.append(dialog)

    return first_mes_answer_user

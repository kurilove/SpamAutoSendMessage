import asyncio
import random

import pyrogram.errors
import pyrogram.types

from Parsers.ParsFunc import *
from Data.DataFunc import *
from Mains.config import condition_text, me_account_text, condition_entyties, me_account_text_entyties

count_send_condition = 0
count_send_voice = 0
count_send_spam_voice = 0


async def main_send(app):
    global count_send_condition, count_send_voice,count_send_spam_voice
    async with app:
        users = await get_account_dialogs(app)
        # use_spam_mes = get_use_username_data_for_spam_mes()
        use_first_mes = get_use_username_data_for_first_mes()
        use_second_mes = get_use_username_data_for_second_mes()

        print(len(users), "непрочитанных юзеров")

        for user in users:

            # if user not in use_spam_mes and user not in use_first_mes:
            #     await app.read_chat_history(user)
            #     await asyncio.sleep(5)
            #     await send_spam_voice_mes(app, user)
            #     set_username_for_spam_mes(user)
            #     count_send_spam_voice += 1
            #     await asyncio.sleep(3)
            #     try:
            #         await app.send_message(chat_id="voice_counter",
            #                                text=f"Спам голосовое номер {count_send_spam_voice}")
            #         print(f"отправлены войсы {user}")
            #     except pyrogram.errors.PeerFlood:
            #         await send_message_SpamBot(app)
            #         await app.send_message(chat_id="voice_counter",
            #                                text=f"Спам голосовое номер {count_send_spam_voice}")
            #         print(f"отправлены войсы после спамблока {user}")

            if user not in use_first_mes and user not in use_second_mes:
                await app.read_chat_history(user)
                await asyncio.sleep(5)
                await send_voice_first_mes(app, user)
                set_username_for_first_mes(user)
                count_send_voice += 1
                await asyncio.sleep(3)
                try:
                    await app.send_message(chat_id="voice_counter",
                                           text=f"отправлено войсов {count_send_voice}")
                    print(f"отправлены войсы {user}")
                except pyrogram.errors.PeerFlood:
                    await send_message_SpamBot(app)
                    await app.send_message(chat_id="voice_counter",
                                           text=f"отправлено войсов {count_send_voice}")
                    print(f"отправлены войсы после спамблока {user}")

            if user in use_first_mes and user not in use_second_mes:
                await app.read_chat_history(user)
                await asyncio.sleep(5)
                await send_conditions(app, user)
                set_username_for_second_mes(user)
                count_send_condition += 1
                await asyncio.sleep(3)
                try:
                    await app.send_message(chat_id="uslovia_counter",
                                           text=f"отправлено условий {count_send_condition}")
                    print(f"отправлены условия {user}")
                except pyrogram.errors.PeerFlood:
                    await send_message_SpamBot(app)
                    await app.send_message(chat_id="uslovia_counter",
                                           text=f"отправлено условий {count_send_condition}")
                    print(f"отправлены условия после спамблока {user}")

            # if user in use_second_mes:
            #
            #     try:
            #         await app.send_message(chat_id="kurilove_CRT", text=f"Че то ему надо бля @{user}")
            #         print(f"Уже всё ему отправили {user}")
            #     except pyrogram.errors.PeerFlood:
            #         await send_message_SpamBot(app)
            #         await app.send_message(chat_id="kurilove_CRT", text=f"Че то ему надо бля спамблок @{user}")
            #         print(f"Уже всё ему отправили после спамблока {user}")


async def send_spam_voice_mes(app, user):
    voice_list = ("https://t.me/shalto_balto/381", "https://t.me/shalto_balto/382", "https://t.me/shalto_balto/383",
                  "https://t.me/shalto_balto/384")
    await app.send_voice(chat_id=user, voice=voice_list[random.randint(0, 3)])
    await asyncio.sleep(2)


async def send_voice_first_mes(app, user):
    await app.send_voice(chat_id=user, voice="https://t.me/shalto_balto/342")
    await asyncio.sleep(2)
    await app.send_voice(chat_id=user, voice="https://t.me/shalto_balto/345")


async def send_conditions(app, user):
    await app.send_message(chat_id=user, text=condition_text, entities=pyrogram.types.List(condition_entyties))
    await app.send_message(chat_id=user, text=me_account_text, entities=pyrogram.types.List(me_account_text_entyties))


async def send_message_SpamBot(app):
    await asyncio.sleep(5)
    await app.send_message("SpamBot", text="/start")
    await asyncio.sleep(3)
    await app.send_message("SpamBot", text="/start")
    await asyncio.sleep(3)

from pyrogram import Client,types
import asyncio
import glob

glob_ses = (sorted(glob.glob("E:/pythonProject/SpamAutoSendMessage/Data/sessions/*.session")))
ses = [ses.split("\\")[1].split(".")[0] for ses in glob_ses]

from config import *
from Sends.SendFunc import *

scroll_number = 0
while True:
    number_proxy = -1

    for one_ses in ses:
        try:
            number_proxy += 1


            async def main():

                app = Client(road_to_ses(one_ses), app_version=App_version, api_id=Api_id, api_hash=Api_hash,
                             proxy=get_proxy(number_proxy), system_version=System_version, lang_code="en")

                async with app:
                    me = await app.get_me()
                    print(me.first_name, me.last_name, me.phone_number)


                await main_send(app)

                await async_progres_bar(5)


            if __name__ == "__main__":
                asyncio.run(main())

        except Exception as ex:
            print(ex)
    scroll_number += 1
    print_progress_bar(150)
    print(
        f"scroll_number,{count_send_voice}/{count_send_condition}-------------------------------------SCROLL NUMBER------------------------------------")

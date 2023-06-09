from tqdm import tqdm
import asyncio
import time

path = "E:/pythonProject/SpamAutoSendMessage/"
def get_proxy(proxy_num):
    with open(f"{path}Data/proxy", "r", encoding="utf-8") as proxy_file:
        all_proxy = proxy_file.read().split("\n")
        proxy_data = all_proxy[proxy_num].split(":")
        ip = proxy_data[0]
        port = proxy_data[1]
        username = proxy_data[2]
        password = proxy_data[3]
        return dict(scheme="socks5", hostname=ip, port=int(port), username=username, password=password)


async def async_progres_bar(num_sec):
    for i in tqdm(range(num_sec), colour="blue"):
        await asyncio.sleep(1)

def print_progress_bar(num_sec):
    for i in tqdm(range(num_sec)):
        time.sleep(1)


def set_username_for_spam_mes(user):
    with open(f'{path}Data/SpamVoiceSend.txt', "a", encoding="utf-8") as file:
        try:
            file.write(f'{user}\n')
        except Exception as ex:
            print(ex)
def set_username_for_first_mes(user):
    with open(f'{path}Data/FirstMessageSend.txt', "a", encoding="utf-8") as file:
        try:
            file.write(f'{user}\n')
        except Exception as ex:
            print(ex)

def set_username_for_second_mes(user):
    with open(f'{path}Data/SecondMessageSend.txt', "a", encoding="utf-8") as file:
        try:
            file.write(f'{user}\n')
        except Exception as ex:
            print(ex)


def get_use_username_data_for_spam_mes() -> list:
    username_data = []
    with open(f"{path}Data/SpamVoiceSend.txt", "r", encoding="utf-8") as file:
        for username in file.read().split("\n"):
            username_data.append(username)
    # print(username_data, "им отправлено 2 сообщение")
    return list(username_data)

def get_use_username_data_for_first_mes() -> list:
    username_data = []
    with open(f"{path}Data/FirstMessageSend.txt", "r", encoding="utf-8") as file:
        for username in file.read().split("\n"):
            username_data.append(username)
    # print(username_data, "им отправлено 1 сообщение")
    return list(username_data)


def get_use_username_data_for_second_mes() -> list:
    username_data = []
    with open(f"{path}Data/SecondMessageSend.txt", "r", encoding="utf-8") as file:
        for username in file.read().split("\n"):
            username_data.append(username)
    # print(username_data, "им отправлено 2 сообщение")
    return list(username_data)


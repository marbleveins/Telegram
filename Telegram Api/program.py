from telethon import TelegramClient, sync, events
import asyncio
import logging

import littleThings, cwHelper

logging.basicConfig(level=logging.ERROR)


api_id = 519113#519113
api_hash = '58733b74f65c4af4de950b15eafa7e39'#58733b74f65c4af4de950b15eafa7e39


loop = asyncio.get_event_loop()


chatWarsHelper: cwHelper.ChatWarsHelper


class TelegramInfo(dict):
    api_id = 519113#519113
    api_hash = '58733b74f65c4af4de950b15eafa7e39'#58733b74f65c4af4de950b15eafa7e39
    session = 'telegram_api_2'
    telegramClient: TelegramClient


telegramInfo = TelegramInfo()

def Main():
    littleThings.SaySlowly('🦅🦅 Hola 🦅🦅!\n', 0.2)
    StartTelegram()
    RunClock()
    print('End Main')

def StartTelegram():
    global telegramInfo
    global loop
    with TelegramClient('telegram_api_2', api_id, api_hash) as client:
        #me = client.get_me()
        telegramInfo.telegramClient = client.start()
        print('=> PrepareTelegram... client: ' + str(telegramInfo.telegramClient))
        telegramInfo.telegramClient.send_message('self', 'starting telegram client')
        
        AddTelegramNewMessageHandler(TelegramNewMessageHandler, telegramInfo.telegramClient)
        StartChatWarsHelper(telegramInfo)

        #loop.create_task(TelegramDisconnected(telegramInfo))
        resp = loop.run_until_complete(littleThings.runAsyncEvery(5, PrintClient))
        telegramInfo.telegramClient.run_until_disconnected()
    print('=> PrepareTelegram End')
    loop.create_task(TelegramDisconnected(telegramInfo))


async def TelegramDisconnected(telegramInfo):
    try:
        await telegramInfo.telegramClient.run_until_disconnected()
    except Exception as err:
        print(str(err))
    print('TelegramDisconnected')
    StartTelegram()

async def PrintClient():
    global telegramInfo
    print('client connected: ' + str(telegramInfo.telegramClient.is_connected()))


def StartChatWarsHelper(telegramInfo):
    global chatWarsHelper
    try:
        chatWarsHelper = cwHelper.ChatWarsHelper(telegramInfo.telegramClient)
        AddTelegramNewMessageHandler(chatWarsHelper.testMessageAboutCW, telegramInfo.telegramClient)
        print('StartChatWarsHelper started..........')
    except Exception as err:
        print('Error en StartChatWarsHelper: ' + str(err))


async def TelegramNewMessageHandler(event: events.NewMessage.Event):
    try:
        print('TelegramNewMessageHandler: ' + str(event))
    except Exception as e:
            print('Error in TelegramNewMessageHandler')
            print(str(e))

def AddTelegramNewMessageHandler(function, telegramClient):
    telegramClient.add_event_handler(function, events.NewMessage)
    print('AddTelegramNewMessageHandler: ' + str(function))

def RunClock():
    loop.run_until_complete(littleThings.runAsyncEvery(30, littleThings.printClock))


#### Start ####
def Start():
    Main()
Start()



### TODO: va a tener un grupo donde guardar info en mensajes?
### TODO: lista diccionario de id y chats donde guardar algo sobre ese chat, ultima fecha y ultimo mensaje
### TODO: lista de ignorados y lista de reservados, modo reservado o no (default todos le hablan),  
### TODO: metodo para preguntar grupos activos en la semana tira consulta? (quizas evitar consultas de bot)
### TODO: 
### TODO: 
### TODO: 

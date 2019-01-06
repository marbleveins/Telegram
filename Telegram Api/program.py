from telethon import TelegramClient, sync, events
import asyncio
import logging

import littleThings, cwHelper

logging.basicConfig(level=logging.ERROR)


api_id = 519113#519113
api_hash = '58733b74f65c4af4de950b15eafa7e39'#58733b74f65c4af4de950b15eafa7e39


loop = asyncio.get_event_loop()


telegramClient: TelegramClient
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

async def StartTelegramAsync(telegramInfo):
    await PrepareTelegramAsync(telegramInfo)

def StartTelegram():
    PrepareTelegram(telegramInfo)
    #telegramInfo.telegramClient = loop.create_task(PrepareTelegramAsync(telegramInfo))

async def PrepareTelegramAsync(telegramInfo):
    async with TelegramClient('telegram_api_2', api_id, api_hash) as client:
        telegramInfo.telegramClient = await client.start()
        print('=> PrepareTelegram... client: ' + str(telegramInfo.telegramClient))
        #me = client.get_me()
        await telegramInfo.telegramClient.send_message('self', 'starting telegram client')
        AddTelegramNewMessageHandler(TelegramNewMessageHandler, telegramInfo.telegramClient)
        StartChatWarsHelper(telegramInfo)
        loop.create_task(TelegramDisconnected(telegramInfo))
    print('=> PrepareTelegram End')
    return telegramInfo

def PrepareTelegram(telegramInfo):
    with TelegramClient('telegram_api_2', api_id, api_hash) as client:
        telegramInfo.telegramClient = client.start()
        print('=> PrepareTelegram... client: ' + str(telegramInfo.telegramClient))
        #me = client.get_me()
        telegramInfo.telegramClient.send_message('self', 'starting telegram client')
        
        AddTelegramNewMessageHandler(TelegramNewMessageHandler, telegramInfo.telegramClient)
        StartChatWarsHelper(telegramInfo)

        loop.create_task(TelegramDisconnected(telegramInfo))
    print('=> PrepareTelegram End')

async def TelegramDisconnected(telegramInfo):
    try:
        await telegramInfo.telegramClient.run_until_disconnected()
    except Exception as err:
        print(str(err))
    print('TelegramDisconnected')
    StartTelegram()


def StartChatWarsHelper(telegramInfo):
    try:
        print('StartChatWarsHelper')
        print('telegramClient: ' + str(telegramInfo.telegramClient))
        chatWarsHelper = cwHelper.ChatWarsHelper(telegramInfo.telegramClient)
        AddTelegramNewMessageHandler(chatWarsHelper.testMessageAboutCW, telegramInfo.telegramClient)
        print('StartChatWarsHelper End')
    except Exception as err:
        print('Error en StartChatWarsHelper: ' + str(err))


def TelegramNewMessageHandler(event: events.NewMessage.Event):
    loop.create_task(print('TelegramNewMessageHandler: ' + str(event)))
    #loop.create_task(task)

def AddTelegramNewMessageHandler(function, telegramClient):
    telegramClient.add_event_handler(function, events.NewMessage)
    print('AddTelegramNewMessageHandler: ' + str(function))

def RunClock():
    loop.run_until_complete(littleThings.runAsyncEvery(30, littleThings.printClock))#repite las task?


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

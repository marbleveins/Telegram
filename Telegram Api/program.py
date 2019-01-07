from telethon import TelegramClient, sync, events
from random import randint
import asyncio
import logging
import time

import littleThings, cwHelper

logging.basicConfig(level=logging.ERROR)


api_id = 519113#519113
api_hash = '58733b74f65c4af4de950b15eafa7e39'#58733b74f65c4af4de950b15eafa7e39


loop = asyncio.get_event_loop()




class TelegramInfo(dict):
    api_id = 519113#519113
    api_hash = '58733b74f65c4af4de950b15eafa7e39'#58733b74f65c4af4de950b15eafa7e39
    session = 'telegram_api_2'
    telegramClient = None


telegramInfo = TelegramInfo()
chatWarsHelper: cwHelper.ChatWarsHelper

def Main():
    littleThings.SaySlowly('🦅  🦅  Hola    🦅  🦅!\n', 0.2)
    TelegramClientLoop()
    print('-TelegramClientLoop.')
    RunClock()
    print('Program End')

def TelegramClientLoop():
    while True:
        if IsTelegramConnected() == False:
            print('starting Telegram client')
            with TelegramClient('telegram_api_2', api_id, api_hash) as client:
                telegramInfo.telegramClient = client.start()
                telegramInfo.telegramClient.send_message('self', 'starting telegram client')

                AddTelegramNewMessageHandler(TelegramNewMessageHandler, telegramInfo.telegramClient)
                StartChatWarsHelper(telegramInfo)

                resp = loop.run_until_complete(TelegramProcess())
                telegramInfo.telegramClient.run_until_disconnected()
            print('Telegram client disconnected. resp: ' + str(resp))


async def TelegramProcess():
    while True:
        await asyncio.sleep(5)



def IsTelegramConnected():
    global telegramInfo
    print('client connected: ' + str(hasattr(telegramInfo, 'telegramClient') and telegramInfo.telegramClient != None and telegramInfo.telegramClient.is_connected() == True))
    return hasattr(telegramInfo, 'telegramClient') and telegramInfo.telegramClient != None and telegramInfo.telegramClient.is_connected() == True


def StartChatWarsHelper(telegramInfo):
    global chatWarsHelper
    chatWarsHelper = cwHelper.ChatWarsHelper(telegramInfo.telegramClient)
    chatWarsHelper.on = True
    AddTelegramNewMessageHandler(chatWarsHelper.testMessageAboutCW, telegramInfo.telegramClient)
    print('ChatWarsHelper started..........')


async def TelegramNewMessageHandler(event: events.NewMessage.Event):
    try:
        testNewTelegramMessage(event)
    except Exception as e:
            print('Error in TelegramNewMessageHandler: ')
            print(str(e))

def AddTelegramNewMessageHandler(function, telegramClient):
    telegramClient.add_event_handler(function, events.NewMessage)
    print('AddTelegramNewMessageHandler: ' + str(function))

def RunClock():
    loop.run_until_complete(littleThings.runAsyncEvery(30, littleThings.printClock))

def testNewTelegramMessage(event: events.NewMessage.Event):
    global chatWarsHelper
    if 'program start cwh' in event.raw_text:
        chatWarsHelper.on = True
        print('chatWarsHelper - ON')
    if 'program end cwh' in event.raw_text:
        chatWarsHelper.on = False
        print('chatWarsHelper - OFF')





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

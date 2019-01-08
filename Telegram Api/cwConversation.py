from telethon import TelegramClient, sync, events
from telethon.tl.custom.conversation import Conversation
from random import randint
import asyncio


# 🏰Castle   ⚖Exchange  📦Stock  70 x 1000💰 [selling] 
class ChatWarsConversation(dict):
    listeningCallBack:callable
    listening = False
    def __init__(self, client:TelegramClient, target:str):
        dict.__init__(self, client=client, target=target)
        self.client = client
        self.target = target
        self.conversation = self.client.conversation(self.target)
    
    
    @property
    def conversation(self):
        return self._conversation
    @conversation.setter
    def conversation(self, value):
        self._conversation = value
    


    def Close(self):
        self.StopListening()
        self.conversation.cancel()
    
    def SendMessage(self, message):
        print('SendMessage')
        with self.conversation:
            self.conversation.send_message(message)
            response = self.conversation.get_response()
        return response
    async def SendMessageAsync(self, message):
        print('SendMessageAsync')
        async with self.conversation:
            await self.conversation.send_message(message)
            response = await self.conversation.get_response()
        return response
    
    def StartListening(self, function=None):
        self.client.add_event_handler(self.NewMessageArrived, events.NewMessage)
        self.listening = True
        if function is not None and function is callable:
            self.SetListeningCallBack(function)
        self.listening = True
    
    def StopListening(self, function=None):
        self.client.remove_event_handler(self.NewMessageArrived, events.NewMessage)
        self.listening = False
        self.SetListeningCallBack(None)
    
    def SetListeningCallBack(self, function):
        self.listeningCallBack = function

    
    async def NewMessageArrived(self, event: events.NewMessage.Event):
        if self.listening:
            await self.listeningCallBack()


    
    async def sayBack(self):
        await self.SendMessageAsync(':arrow_left:Back')
    async def sayCastle(self):
        await self.SendMessageAsync('🏰Castle')
    async def sayExchange(self):
        await self.SendMessageAsync('⚖Exchange')
    async def sayStock(self):
        await self.SendMessageAsync('/stock')
    async def sayMe(self):
        await self.SendMessageAsync('/me')
    


    #






### TODO: cuando lee un 404 Not Found o el ¯\_(ツ)_/¯ en el chtwrsbot intenta corregir?
### TODO:   -.,(@)-·¯
### TODO: 
### TODO: 
### TODO: 
from telethon import TelegramClient, sync, events
from telethon.tl.custom.conversation import Conversation
from random import randint
import asyncio
import cwCommonUtils

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
        await asyncio.sleep(randint(1,2))
        async with self.conversation:
            response = self.conversation.wait_event(events.NewMessage(incoming=True))
            await self.conversation.send_message(message)
        return await response
    
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
        await self.SendMessageAsync(cwCommonUtils.GetCommand("back"))
    async def sayCastle(self):
        await self.SendMessageAsync(cwCommonUtils.GetCommand("castle"))
    async def sayExchange(self):
        await self.SendMessageAsync(cwCommonUtils.GetCommand("exchange"))
    async def sayStock(self):
        await self.SendMessageAsync(cwCommonUtils.GetCommand("stock"))
    async def sayMe(self):
        await self.SendMessageAsync(cwCommonUtils.GetCommand("me"))
    async def sayRemoveHash(self, remove_hash):
        await self.SendMessageAsync(remove_hash)
    async def saySell(self, command):
        await self.SendMessageAsync(command)

    async def GetItemQuantity(self, item_name):
        stock = (await self.sayStock()).raw_text
        return cwCommonUtils.GetItemAmountFromStock(item_name, stock)

    async def GetItemQuantityInExchange(self, item_name):
        await self.sayMe()
        await self.sayCastle()
        exchange = (await self.sayExchange()).raw_text
        return cwCommonUtils.GetItemAmountFromExchange(item_name, exchange)
    
    async def GetRemoveHashFromExchange(self, item_name):
        await self.sayMe()
        await self.sayCastle()
        exchange = (await self.sayExchange()).raw_text
        return cwCommonUtils.GetRemoveHashFromExchange(item_name, exchange)
    
    async def RemoveItemFromExchange(self, remove_hash):
        #ensure able to send? maybe be in castle/exchange
        response = (await self.sayRemoveHash(remove_hash)).raw_text
        if "Cancelling order" in response:
            return True
        else:
            return False
    
    async def TryToSell(self, command):
        retries = 3
        while retries > 0:
            response = (await self.saySell(command)).raw_text
            if 'You are selling:' in response and 'Cancel trade' in response:
                return True
            else:
                retries = retries - 1
                await asyncio.sleep(2)
        return False

    

    #






### TODO: cuando lee un 404 Not Found o el ¯\_(ツ)_/¯ en el chtwrsbot intenta corregir?
### TODO:   -.,(@)-·¯
### TODO: 
### TODO: 
### TODO: 
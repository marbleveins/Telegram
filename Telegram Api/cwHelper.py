from telethon import TelegramClient, sync, events
from telethon.tl.custom.conversation import Conversation
from random import randint
import asyncio

import cwCommonUtils
from cwConversation import ChatWarsConversation

# 🏰Castle   ⚖Exchange  📦Stock  70 x 1000💰 [selling] 

class ChatWarsHelper(dict):
    chat_me = 'self'
    chat_apronhammer = 'apronhammer_bot'
    chat_chatwars = 'chtwrsbot'
    chat_api_testing = -329868035
    on = False
    def __init__(self, client):
        dict.__init__(self, client=client)
        self.client = client
        self.conversation = ChatWarsConversation(self.client, self.chat_chatwars)
    
    async def Hide(self, item_name):
        print('=> hiding: ' + item_name)
        item_quantity = await self.conversation.GetItemQuantity(item_name)
        print(item_name + ' to hide: ' + str(item_quantity))
        if item_quantity > 0:
            remove_hash = await self.conversation.GetRemoveHashFromExchange(item_name)
            if remove_hash != None:#ir una sola vez al exchange y obtener hidden_quantity y remove hash
                hidden_quantity = await self.conversation.GetItemQuantityInExchange(item_name)
                print(item_name + ' already in exchange: ' + str(hidden_quantity))
                removed = await self.conversation.RemoveItemFromExchange(remove_hash)
                if removed:
                    total_quantity = item_quantity + hidden_quantity
                    print(str('new total ' + item_name + ' to hide: ' + str(total_quantity)))
                    await asyncio.sleep(2)
                    await self.conversation.TryToSell('/wts_01_' + str(total_quantity) + '_1000')

    async def cwNewMessageHandler(self, event: events.NewMessage.Event):
        if self.on == False:
            return
        try:
            if event and event.chat:
                print('=> cwNewMessageHandler message from "' + str(event.chat.title) + '" :' + str(event.raw_text))
            if self.TestHideItem('thread', str(event.raw_text)):
                await self.HideItem('thread')

            
        except Exception as e:
            print('Error in cwNewMessageHandler: ')
            print(str(e))
    
    #async def HideHiddenItems(self):


    def TestHideItem(self, item_name, text):
        return cwCommonUtils.TestFollowingWords(['agus','cwh','hide', item_name], text.lower())
    
    async def HideItem(self, item_name):
        await self.Hide(item_name)







### TODO: cuando lee un 404 Not Found o el ¯\_(ツ)_/¯ en el chtwrsbot intenta corregir?
### TODO:   -.,(@)-·¯
### TODO: 
### TODO: 
### TODO: 
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
    
    #async def Deposit?
        
    async def CraftRecursive(self, item_name):
        try:
            requiered = (await self.conversation.sayCraft(item_name)).raw_text
            await asyncio.sleep(2)
            if isinstance(requiered, str):
                first_item_requiered = await self.conversation.GetFirstItemNameFromCraftResult(requiered)
                return await self.CraftRecursive(first_item_requiered)
            else:
                return True
        except Exception as err:
            print('Error in CraftRecursive: ')
            print(str(err))

    async def Hide(self, item_name):
        try:
            print('=> hiding: ' + item_name)
            item_quantity = await self.conversation.GetItemQuantity(item_name)
            print(item_name + ' to hide: ' + str(item_quantity))
            if item_quantity > 0:
                exchange = await self.conversation.GetExchange()
                remove_hash = await self.conversation.GetRemoveHashFromExchange(item_name, exchange)
                if remove_hash != None:#ir una sola vez al exchange y obtener hidden_quantity y remove hash
                    hidden_quantity = await self.conversation.GetItemQuantityFromExchange(item_name, exchange)
                    print(item_name + ' already in exchange: ' + str(hidden_quantity))
                    removed = await self.conversation.RemoveItemFromExchange(remove_hash)
                    if removed:
                        total_quantity = item_quantity + hidden_quantity
                else:
                    print('no' + item_name + ' in exchange: ')
                    total_quantity = item_quantity
                await asyncio.sleep(2)
                await self.conversation.TryToSell(item_name, total_quantity)
        except Exception as err:
            print('Error in Hide: ')
            print(str(err))

    async def cwNewMessageHandler(self, event: events.NewMessage.Event):
        if self.on == False:
            return
        try:
            if event and event.chat:
                chat_name = event.chat.title if hasattr(event.chat, 'title') else event.chat.username
                print('=> cwNewMessageHandler message from "' + str(chat_name) + '" :' + str(event.raw_text))
            if self.TestHideItem(str(event.raw_text), 'thread'):
                await self.HideItem('thread')
            if self.TestCraftItem(str(event.raw_text), 'coke'):
                item_name = self.GetItemNameFromOrder(event.raw_text)
                await self.CraftRecursive('coke')
            if self.TestPota(str(event.raw_text), None):
                await self.conversation.sayPota('/use_p13')#mana

            
        except Exception as err:
            print('Error in cwNewMessageHandler: ')
            print(str(err))
    
    #async def HideHiddenItems(self):


    def TestHideItem(self, text, item_name):
        return cwCommonUtils.TestFollowingWords(['agusbot','cwh','hide', item_name], text.lower())
    def TestChangeItem(self, text, item_name):
        return cwCommonUtils.TestFollowingWords(['agusbot','cwh','shop', 'change',item_name], text.lower())
    def TestCraftItem(self, text, item_name):
        return cwCommonUtils.TestFollowingWords(['agusbot','cwh','craft', 'recursive', item_name], text.lower())
    def TestPota(self, text, item_name=None):
        return cwCommonUtils.TestFollowingWords(['agusbot','cwh','use', 'pota', item_name], text.lower())
    
    def GetItemNameFromOrder(self, order):
        #
        return ''
    
    async def HideItem(self, item_name):
        await self.Hide(item_name)







### TODO: cuando lee un 404 Not Found o el ¯\_(ツ)_/¯ en el chtwrsbot intenta corregir?
### TODO:   -.,(@)-·¯
### TODO: 
### TODO: 
### TODO: 
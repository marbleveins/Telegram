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
    
    async def Craft(self, item_name, qtty):
        item_id = cwCommonUtils.GetItemId(item_name)
        result = await self.CraftRecursive(item_id, str(qtty))
        if result is True:
            print('Crafted: ' + item_name + ' x ' + str(qtty))
        else:
            print('NO PUDE CRAFTEAR')

    async def CraftRecursive(self, item_id, qtty):
        try:
            response = (await self.conversation.sayCraft(item_id, qtty)).raw_text
            await asyncio.sleep(2)
            if cwCommonUtils.TestCraftResult(response) == 'REQUIRED':
                response = cwCommonUtils.GetRequiredItemsFromCraftResult(response, ' ')
                for requiered_item in response:
                    item_requiered_id = cwCommonUtils.GetItemIdFromCraftOrder(requiered_item)
                    item_requiered_qtty = cwCommonUtils.GetItemQttyFromCraftOrder(requiered_item)
                    required_craft_result = await self.CraftRecursive(item_requiered_id, item_requiered_qtty)
                    if required_craft_result == False: return False
                return True
            elif cwCommonUtils.TestCraftResult(response) == 'MANA':
                return False
            elif cwCommonUtils.TestCraftResult(response) == 'CRAFTED':
                return True
            return False
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

            if self.TestCraftRecursive(str(event.raw_text)):
                order = cwCommonUtils.GetItemFromOrder(str(event.raw_text), 'recursive')
                item_id = cwCommonUtils.GetItemIdFromCraftOrder(order)
                item_qtty = cwCommonUtils.GetItemQttyFromCraftOrder(order)
                item_name = cwCommonUtils.GetItemName(item_id)
                await self.Craft(item_name, item_qtty)

            if self.TestPota(str(event.raw_text), None):
                await self.conversation.sayPota('/use_p13')#mana

            
        except Exception as err:
            print('Error in cwNewMessageHandler: ')
            print(str(err))
    
    #async def HideHiddenItems(self):


    def TestHideItem(self, text, item_name):
        return cwCommonUtils.TestCommandInText(cwCommonUtils.startingCall + ['hide', item_name], text)
    def TestChangeItem(self, text, item_name):
        return cwCommonUtils.TestCommandInText(cwCommonUtils.startingCall + ['shop', 'change', item_name], text)
    def TestCraftRecursive(self, text):
        return cwCommonUtils.TestCommandInText(cwCommonUtils.startingCall + ['craft', 'recursive'], text)
    def TestPota(self, text, item_name=None):
        if isinstance(item_name, str):
            return cwCommonUtils.TestCommandInText(cwCommonUtils.startingCall + ['pota', item_name], text)
        else:
            return cwCommonUtils.TestCommandInText(cwCommonUtils.startingCall + ['pota'], text)
    
    async def HideItem(self, item_name):
        await self.Hide(item_name)







### TODO: cuando lee un 404 Not Found o el ¯\_(ツ)_/¯ en el chtwrsbot intenta corregir?
### TODO:   -.,(@)-·¯
### TODO: 
### TODO: 
### TODO: 
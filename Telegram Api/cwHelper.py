from telethon import TelegramClient, sync, events
import asyncio

import cwCommonUtils

# 🏰Castle   ⚖Exchange 

class ChatWarsHelper(dict):
    chat_me = 'self'
    chat_apronhammer = 'apronhammer_bot'
    chat_chatwars = 'chtwrsbot'
    chat_api_testing = -329868035
    def __init__(self, client):
        dict.__init__(self, client=client)
        self.client = client
    
    async def Hide(self, item_name=str):
        await self.client.send_message(self.chat_me, 'hiding' + item_name + ', make sure to check time')
        async with self.client.conversation(self.chat_chatwars) as conv:
            await conv.send_message('/stock')
            stock = await conv.get_response().raw_text
            print('printing stock: ' + stock)
            item_amount = cwCommonUtils.GetItemAmountFromStock(item_name, stock)
            print('item amount to hide: ' + item_amount)
            if item_amount > 0:
                await conv.send_message('🏰Castle')
                #castle = await conv.get_response().raw_text
                await conv.send_message('⚖Exchange')
                exchange = await conv.get_response().raw_text
                removeItem = cwCommonUtils.GetRemoveHashFromExchange(item_name, exchange)
                if removeItem != None:
                    await conv.send_message(removeItem)
                    item_amount = item_amount + cwCommonUtils.GetItemAmountFromExchange(item_name,exchange)
                
                await asyncio.sleep(2)
                await self.TryToSell('/wts_01_' + item_amount + '_1000', conv)

    async def TryToSell(self, command, conv):
        retries = 3
        while retries > 0:
            await conv.send_message(command)
            response = await conv.get_response().raw_text
            if 'You are selling:' in response and 'Cancel trade' in response:
                return
            else:
                retries = retries - 1
                await asyncio.sleep(2)
    
    async def testMessageAboutCW(self, event: events.NewMessage.Event):
        try:
            print('testMessageAboutCW')
            '''
            if 'agus' in event.raw_text:
                if 'spawn miracle' in event.raw_text:
                    print('-sending message... raw_text: ' + event.raw_text)
                    await self.client.send_message(event.input_chat, 'hmmm_newMessage_Handler')
                    print('-message sent.')
                if 'Hide' in event.raw_text:
                    print('hiding. raw_text: ' + event.raw_text)
                    await self.Hide('thread')
            '''
        except Exception as e:
            print('Error in testMessageAboutCW')
            print(str(e))



### TODO: cuando lee un 404 Not Found o el en el chtwrsbot intenta corregir?
### TODO:   -.,(@)-.-
### TODO: 
### TODO: 
### TODO: 
from telethon import TelegramClient, sync, events
import asyncio
import logging


logging.basicConfig(level=logging.ERROR)


api_id = 519113#519113
api_hash = '58733b74f65c4af4de950b15eafa7e39'#58733b74f65c4af4de950b15eafa7e39

loop = asyncio.get_event_loop()

username_me = 'self'


async def main():
    for char in 'Hello, world!\n':
        print(char, end='', flush=True)
        await asyncio.sleep(0.2)


async def newMessage_Handler(event: events.NewMessage.Event):
    try:
        if 'agus' in event.raw_text:
            print('-sending message... agus in raw_text:' + event.raw_text)
            await client.send_message(username_me, 'hmmm_newMessage_Handler')
            print('-message sent.')
        
    except Exception as e:
        print(str(e))



with TelegramClient('telegram_api_2', api_id, api_hash) as client:
    client.start()
    me = client.get_me()
    client.send_message('self', 'start')

    client.add_event_handler(newMessage_Handler, events.NewMessage)
    loop.create_task(main())
    client.run_until_disconnected()






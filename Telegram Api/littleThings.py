import datetime
import time
import asyncio


async def printClock():
    print('UTC time:', datetime.datetime.utcnow())
    print('local time:', datetime.datetime.now())

async def runAsyncEvery(seconds, callback):
    while True:
        await callback()
        await asyncio.sleep(seconds)


def SaySlowly(text, seconds):
    #         Hi !
    for char in text:
        print(char, end='', flush=True)
        time.sleep(seconds)
    

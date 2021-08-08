import asyncio
import websockets


async def time(websocket, path):
    file = open("log.txt", "r")
    while True:
        now = file.readline()
        if len(now) > 1:
            await websocket.send(now)
        await asyncio.sleep(1)


start_server = websockets.serve(time, "127.0.0.1", 7000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

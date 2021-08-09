import asyncio

import websockets
from file_read_backwards import FileReadBackwards

with FileReadBackwards("log.txt") as file_read:
    count = 0
    lines_list = []
    while count < 10:
        curr_line = file_read.readline()
        if not curr_line:
            break
        lines_list.append(curr_line)
        count = count + 1


async def time(websocket, path):
    file = open("log.txt", "r")
    file.seek(0, 2)
    log_count = 0
    lines_list.reverse()
    while True:
        if log_count < 10 and log_count < len(lines_list):
            now = lines_list[log_count]
        else:
            now = file.readline()
        if len(now) > 1:
            await websocket.send(now)
        await asyncio.sleep(1)
        log_count = log_count + 1


start_server = websockets.serve(time, "127.0.0.1", 7000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

import asyncio
import time

def coro_print():
    thinker = asyncio.async(coro_think('1'))
    for i in range(10):
    # while True:
        print("Printing:"+str(i))
        # asyncio.sleep(0.2)
        # yield
        yield from asyncio.sleep(0.2)
    thinker.cancel()
    return 42

def coro_think(msg):
    i = 0
    while True:
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError:
            print("\t"*3 + "   Thinking"+ msg + ":canclled")
            break
        else:
            if i > 30:
                break
            print("\tThinking"+ msg + ":"+str(i))
            i += 1

def run_sync(coro_or_future):
    loop = asyncio.get_event_loop()
    thinker = asyncio.async(coro_think('2'))
    thinker = asyncio.async(coro_think('3'))
    # time.sleep(5)
    # asyncio.sleep(5)
    # thinker.cancel()
    res =  loop.run_until_complete(coro_or_future)
    # thinker.cancel()
    return res


# print(coro_print)
# print(coro_print())
# a = run_sync(asyncio.sleep(2))

a = run_sync(coro_print())
print(a)
print("completed")

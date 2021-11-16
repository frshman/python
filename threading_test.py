from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import asyncio


async def f_url(url):
    print(url)

async def main():
    cors = [f_url(url) for url in range(10)]
    await asyncio.wait(cors)
    
    

def task():
    ##在子线程中加入协程的关键就在这里，子线程中的loop必须新建
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)  

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


if __name__ == '__main__':
    t = Thread(target=task)
    t.start()
    # t.join()
    print('这是主线程')
        
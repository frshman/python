# 使用aiohttp异步下载

import aiohttp
import asyncio

# 一次请求
# async def test():
#     async with aiohttp.request('GET','https://api.github.com/events') as resp:
#         resp_json =await resp.json()
#         print(resp_json)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())

# 同时处理多个任务，使用asyncio.wait处理协程
# async def main():
#     tasks = []
#     [tasks.append(fetch('https://api.github.com/events?a={}'.format(i))) for i in range(10)]
#     await asyncio.wait(tasks)

# async def fetch(url):
#     async with aiohttp.request('GET', url) as resp:
#         json = await resp.json()
#         print(json)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())  //loop对象是启动协程的关键，由它来返回结果，保存协程状态

# 限制 "同时请求" 的数量,降低了并发量

# async def main(pool):  # aiohttp必须放在异步函数中使用
#     tasks = []
#     sem = asyncio.Semaphore(pool)  # 限制同时请求的数量
#     [tasks.append(control_sem(sem, 'https://api.github.com/events?a={}'.format(i)))
#      for i in range(10)]  # 十次请求
#     await asyncio.wait(tasks)


# async def control_sem(sem, url):  # 限制信号量
#     async with sem:
#         await fetch(url)


# async def fetch(url):
#     async with aiohttp.request('GET', url) as resp:
#         json = await resp.json()
#         print(json)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(pool=2))

#官方推荐使用ClientSession请求
##基本使用如下
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.github.com/events') as resp:
#             print(resp.status)
#             print(await resp.text())

##不要为每次的连接都创建一次session,一般情况下只需要创建一个session，然后使用这个session执行所有的请求。
##每个session对象，内部包含了一个连接池，并且将会保持连接和连接复用（默认开启）可以加快整体的性能。

# async def main(pool):#启动
#     sem = asyncio.Semaphore(pool)
#     async with aiohttp.ClientSession() as session:#给所有的请求，创建同一个session
#         tasks = []
#         [tasks.append(control_sem(sem, 'https://api.github.com/events?a={}'.format(i), session)) for i in range(10)]#十次请求
#         await asyncio.wait(tasks)

# async def control_sem(sem, url, session):#限制信号量
#     async with sem:
#         await fetch(url, session)

# async def fetch(url, session):#开启异步请求
#     async with session.get(url) as resp:
#         json = await resp.json()
#         print(json)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(pool=2))


## 支持传请求头，post数据.
# import json
# async def fetch(url, session,payload,headers):
#     await session.post(url,\
#     data=json.dumps(payload),\
#     headers=headers)


##url 传参 ==》params
# params = {'key1': 'value1', 'key2': 'value2'}
# # params = [('key', 'value1'), ('key', 'value2')]
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://httpbin.org/get',params=params) as resp:
#             assert resp.url =='http://httpbin.org/get?key2=value2&key1=value1'

##关于响应的api
# assert resp.status == 200
# resp.headers

# await resp.text()
# await resp.text(encoding=‘gb2312’)
# await resp.read()
# await resp.json()
# await resp.content.read(10) #读取前10个字节

##文件保存
# async def write_file(filename,chunk_size):
#     async with open(filename, 'wb') as fd:
#         while True:
#             chunk = await resp.content.read(chunk_size) //这里await相当于一直在读取数据，等待fd拿去写入。
#             if not chunk:
#                 break
#             fd.write(chunk)

##cookies设置

# url = 'http://httpbin.org/cookies'
# cookies = {'cookies_are': 'working'}
# async def test_cookie():
#     async with aiohttp.ClientSession(cookies=cookies) as session:
#         async with session.get(url) as resp:
#             assert await resp.json() == {
#                 "cookies": {"cookies_are": "working"}}

##传文件，指定文件名和content-type
# url = 'http://httpbin.org/post'
# data = aiohttp.FormData()
# data.add_field('file',
# open('report.xls', 'rb'),
# filename='report.xls',
# content_type='application/vnd.ms-excel')

# await session.post(url, data=data)

##tcp连接的限制  暂时不知道作用
# conn = aiohttp.TCPConnector(limit=30)#同时最大进行连接的连接数为30，默认是100，limit=0的时候是无限制

# conn = aiohttp.TCPConnector(limit_per_host=30)#默认是0


##自己指定域名解析  不太理解
# from aiohttp.resolver import AsyncResolver

# resolver = AsyncResolver(nameservers=["8.8.8.8", "8.8.4.4"])
# conn = aiohttp.TCPConnector(resolver=resolver)

##普通代理
# async with aiohttp.ClientSession() as session:
#     async with session.get("http://python.org",
#         proxy="http://some.proxy.com") as resp:
#         print(resp.status)


##需要验证的代理，关键在于auth认证账号密码
# async with aiohttp.ClientSession() as session:
# proxy_auth = aiohttp.BasicAuth('user', 'pass')
# async with session.get("http://python.org",
# proxy="http://some.proxy.com",
# proxy_auth=proxy_auth) as resp:
# print(resp.status)

##代理验证也可以直接在写在请求中
# session.get("http://python.org",
# proxy="http://user:pass@some.proxy.com")
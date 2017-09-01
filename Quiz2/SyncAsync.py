import requests
import asyncio



def sync_operation(url):
    r=requests.get(url)
    status_code = r.status_code
    print(status_code)
    print(r)


async def slow_operation(future, id=None):
    print("waiting ... ", id)
    await asyncio.sleep(1)
    future.set_result('Future ' + str(id) + '  is already done')
    

urls = ["https://httpbin.org/status/200", "https://httpbin.org/status/204"]


loop = asyncio.get_event_loop()


sync_operations = [
    asyncio.ensure_future(sync_operation(urls[0])),
    asyncio.ensure_future(sync_operation(urls[1]))
    ]
loop.run_until_complete(asyncio.wait(sync_operations))

loop.close()






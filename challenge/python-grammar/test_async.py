import asyncio 

"""
# 비동기 함수 실행 : asyncio.run

async def my_async_func():
    print("Start Job!")
    await asyncio.sleep(1)
    print("Done Job!")

asyncio.run(my_async_func())

"""
async def fetch_data(): # coroutine 반환 
    print("Fetching data...")
    await asyncio.sleep(2) # 2초 대기하지만, CPU 는 다른 작업을 수행할 수 있음.
    print("Data Fetched!")
    return {"data":"test"}

async def another_task():
    print("Performing another task...")
    await asyncio.sleep(1)
    print("Another task done!")

async def main():
    # 두개의 비동기 작업 동시에 실행 
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(another_task())

    await task1 
    await task2 
  
asyncio.run(main())

"""
fetch_data()의 실행이 끝날 때까지 다른 비동기 작업이 없다면 기다리게 됩니다.
그러나 다른 비동기 작업이 있는 경우, 
그 작업이 실행되면서 효율적으로 리소스를 사용할 수 있습니다.
"""
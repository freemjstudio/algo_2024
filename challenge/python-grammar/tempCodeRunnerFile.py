async def fetch_data(): # coroutine 반환 
    print("Fetching data...")
    await asyncio.sleep(2) 
    print("Data Fetched!")
    return {"data":"test"}

async def main():
    result = await fetch_data() # 비동기 함수의 실행을 중단하고 해당 작업 완료시까지 기다림. 
    print(result) 
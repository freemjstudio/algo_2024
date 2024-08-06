import asyncio

async def read_file():
    print("read file")
    await asyncio.sleep(1)  # 비동기 작업을 시뮬레이션 (예: I/O 작업)
    return "file content"

async def main():
    print("start code")
    data = await read_file()  # read_file 함수가 완료될 때까지 대기
    print(data)

asyncio.run(main())
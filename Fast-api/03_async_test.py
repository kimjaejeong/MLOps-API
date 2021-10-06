#https://www.daleseo.com/python-asyncio/
import time
import asyncio

def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')

def process_sync():
    start_time = time.time()
    find_users_sync(3)
    find_users_sync(2)
    find_users_sync(1)
    end_time = time.time() - start_time
    print(f"비동기 처리 시간: {end_time}")

async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        await asyncio.sleep(1)
    print(f'> 총 {n} 명 사용자 비동기 조회 완료!')

async def process_async():
    start_time = time.time()
    await asyncio.wait([
        find_users_async(3),
        find_users_async(2),
        find_users_async(1),
    ])
    end_time = time.time() - start_time
    print(f"비동기 처리 시간: {end_time}")



if __name__ == "__main__":
    # 동기 프로그램
    # process_sync()
    # 비동기 프로그램
    # asyncio.run(process_async()) -> 3.7부터 허용
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_async())
    


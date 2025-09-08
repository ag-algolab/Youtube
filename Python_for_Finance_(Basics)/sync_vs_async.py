import time
import asyncio

# --- Synchronous version ---
def sync_demo():
    print("=== Synchronous demo ===")
    start = time.time()
    for i in range(5):
        print(f"Start task {i}")
        time.sleep(1)  # blocks everything for 1s
        print(f"End task {i}")
    end = time.time()
    print(f"Total time (sync): {end - start:.2f} seconds\n")


# --- Asynchronous version ---
async def async_task(i: int):
    print(f"Start task {i}")
    await asyncio.sleep(1)  # as time is not awaitable, we use asyncio
    print(f"End task {i}")

# With .gather
async def async_demo_1(): # Coroutine Object
    print("=== Asynchronous demo ===")
    start = time.time()
    tasks = [async_task(i) for i in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    print(f"Total time (async): {end - start:.2f} seconds\n")

# With .create_task
async def async_demo_2(): # Coroutine Object
    print("=== Asynchronous demo ===")
    start = time.time()
    task0 =  asyncio.create_task(async_task(0))
    task1 =  asyncio.create_task(async_task(1))
    task2 =  asyncio.create_task(async_task(2))
    task3 =  asyncio.create_task(async_task(3))
    await task0
    await task1
    await task2
    await task3
    end = time.time()
    print(f"Total time (async): {end - start:.2f} seconds\n")


sync_demo()
asyncio.run(async_demo_1())
asyncio.run(async_demo_2())

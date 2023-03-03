import asyncio
import time


# 调用一个async function 会返回一个coroutine object
async def say_after(what: str, delay: int):
    print(what)
    await asyncio.sleep(delay)


async def main():
    # 将coroutine object放进create task里，会返回一个task
    # create_task 函数将coroutine object放进event loop里
    # 此时程序控制权依然在main函数里，因此这段程序最先打印 start at ...
    task_1 = asyncio.create_task(say_after('hello', 1))
    task_2 = asyncio.create_task(say_after('world', 2))

    print(f"start at {time.strftime('%X')}")

    await task_1
    await task_2

    # await asyncio.gather(task_1, task_2)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

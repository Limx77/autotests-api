import asyncio

async def test1():
    print("Start test1")
    mess = await asyncio.to_thread(input, "Enter value:\n")
    print(mess)
    await asyncio.sleep(3)
    print("End test1")

async def test2():
    print("Start test2")
    for _ in range(5):
        await asyncio.sleep(3)
        print(f"left {4-_} iter")
    print("End test2")


asyncio.run(test1())
asyncio.run(test2())



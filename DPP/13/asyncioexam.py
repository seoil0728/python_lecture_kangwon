import asyncio


async def average(a):
    await asyncio.sleep(2)
    return sum(a) / len(a)


async def printAvg(a):
    await average(a)
    avg = await average(a)
    print('Average for {} is {}'.format(a, avg))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(printAvg([10, 50, 40, 100, 80]))
    loop.close()


if __name__ == '__main__':
    main()

import asyncio
from pyhon import Hon

async def devices_example():
    async with Hon("EMAIL", "PASSWORD") as hon:
        for appliance in hon.appliances:
            print(appliance.nick_name)

asyncio.run(devices_example())
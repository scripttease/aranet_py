import asyncio
import struct
from bleak import BleakScanner
from bleak import BleakClient
import os


async def main():
    devices = await BleakScanner.discover()
    for device in devices:
        print(device.address, device.name)


asyncio.run(main())

import asyncio
import struct
from bleak import BleakScanner
from bleak import BleakClient
from dotenv import load_dotenv
import os

load_dotenv()

# From GATT directory here: https://gist.github.com/ariccio/2882a435c79da28ba6035a14c5c65f22
CURRENT_READING = "f0cd3001-95da-4f4b-9ac8-aa55d312af0c"
# From `.env` file
UUID_address = os.getenv("ARANET_UUID")


async def main(address):
    async with BleakClient(address) as client:
        print(client.is_connected)
        # data = await client.read_gatt_char(CURRENT_READING)
        # readings = struct.unpack('<HHHBBBHH', data)
        # print(f'co2: {readings[0]}ppm')
        # print(f'temperature: {readings[1]/20}C')
        # print(f'pressure: {readings[2]/10}hPa')
        # print(f'humidity: {readings[3]}%')
        # print(f'battery: {readings[4]}%')
        # print(f'status: {readings[5]}')
        # print(f'interval: {readings[6]}s')
        # print(f'age: {readings[7]}s')


asyncio.run(main(UUID_address))

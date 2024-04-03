import time
from govee_btled_windows import BluetoothLED
import asyncio
import numpy as np

async def main():
    # Replace this with your LED's MAC address
    # led = BluetoothLED('74209773-2F79-D43E-5EE9-AEF071CEA34C') # bulb
    led = BluetoothLED('EA5D5E0C-AD67-8D3D-2ABE-501A97DA4077') # bar
    # led = BluetoothLED('46A48234-B7BF-80C1-8A7F-F66A3FA977B5') # lightbar2
    await led.init_and_connect()
    print("connected")
    
    # await led.set_state(False) # off
    # time.sleep(1.5)
    # await led.set_state(True) # on
    # await led.set_brightness(0.25)
    # time.sleep(1.5)
    # await led.set_brightness(0.1)

    # for i in range(5):
    #     for b in np.linspace(0.0, 1.0, 30):
    #         await led.set_brightness(b)

    #     for b in np.linspace(1.0, 0.0, 30):
    #         await led.set_brightness(b)

    # for b in np.linspace(1.0, 0.0, 6):
    #     await led.set_brightness(b)
    #     time.sleep(5)


    await led.set_color_bar('orangered')
    await led.set_brightness(0.25)

    # await led.test_bar()
    # await led._send(0x09, [0x0c, 0x2a, 0x01, 0x02, 0x01, 0xf9])
    # await led._send(0x05, [0x15, 0x05, 0x03, 0x55])
    # await led._send(0x05, [0x15, 0x05, 0x03, 0x64])
    # await led._send(0x05, [0x15, 0x05, 0x03, 0x01])
    # await led._send(0x05, [0x15, 0x05, 0x03, 0x64])
    # await led._send(0x05, [0x15, 0x01, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x0f])

    # Works
    # await led._send_aa(0x11, [0x00, 0x1e, 0x0f, 0x0f])
    # await led._send(0x05, [0x15, 0x01, 0x00, 0x1e, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x0f])
    # time.sleep(2)
    # await led._send(0x05, [0x15, 0x01, 0xff, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x0f])
    
    # await led._send(0x05, [0x15, 0x05, 0x03, 0x01]) # not sure (log13)

    # await led.set_brightness(0.5)

    await led.set_color_white_bar(-1.0)
    time.sleep(1.5)
    await led.set_color_white_bar(1.0)
    time.sleep(1.5)
    # await led.set_color_white(0)

    time.sleep(2)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
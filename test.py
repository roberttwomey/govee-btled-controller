import time
from govee_btled_windows import BluetoothLED
import asyncio
import numpy as np

async def main():
    # Replace this with your LED's MAC address
    led = BluetoothLED('74209773-2F79-D43E-5EE9-AEF071CEA34C')
    await led.init_and_connect()
    print("connected")
    
    # await led.set_state(False) # off
    # time.sleep(1.5)
    # await led.set_state(True) # on
    # await led.set_brightness(0.25)

    # for i in range(5):
    #     for b in np.linspace(0.0, 1.0, 30):
    #         await led.set_brightness(b)

    #     for b in np.linspace(1.0, 0.0, 30):
    #         await led.set_brightness(b)

    # await led.set_color('orangered')

    # OCEAN DESCENT
    # colors https://www.w3.org/TR/css-color-3/#svg-color
    # await led.set_brightness(1.0)
    # await led.set_color('cyan')
    # time.sleep(1.5)
    # await led.set_color('blue')
    # time.sleep(1.5)
    # await led.set_color('darkblue')
    # time.sleep(1.5)
    # await led.set_color('navy')
    # time.sleep(1.5)
    # await led.set_color('midnightblue')
    # await led.set_brightness(0.1)
    
    # await led.test_white()
    # time.sleep(1.5)
    # await led.test_white2()    
    # time.sleep(1.5)

    await led.set_color_white(-1.0)
    time.sleep(1.5)
    await led.set_color_white(1.0)

    # NOT WORKING
    # await led.set_scene(0x08)    
    time.sleep(2)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
import time
from govee_btled_windows import BluetoothLED
import asyncio

async def main():
    # Replace this with your LED's MAC address
    led = BluetoothLED('74209773-2F79-D43E-5EE9-AEF071CEA34C')
    await led.init_and_connect()
    print("connected")
    
    # await led.set_state(False) # off
    # await led.set_state(True) # on
    await led.set_brightness(1.0)
    


    # await led.test_brightness(0x88)
    # await led.set_color('red')
    # await led.set_color('#ff0000')
    # await led.set_brightness(0.9)
    

    # await led.set_color_white(-.55)
    # time.sleep(.5)
    # print("white")
    # await led.set_color('orangered')
    # await led.set_brightness(.7)
    # print("orangered")
    time.sleep(2)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
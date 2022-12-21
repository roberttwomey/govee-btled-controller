# govee_btled_windows
A re-implementation of [Christian Volkmann's govee_btled wrapper](https://github.com/chvolkmann/govee_btled) but with Windows compatibility.

This wrapper supports controlling the Govee/Minger H6001 Smart LED Light Bulb.

# Installation
Use pip to install:
```
pip install -U git+https://github.com/kabyru/govee_btled_windows
```

# Platform Support
This wrapper accomplishes Windows compatibility by re-implementing the ```govee_btled``` package to use the [Bleak](https://github.com/hbldh/bleak) GATT client software. PyGATT is not compatible with most Windows machines' Bluetooth interfaces, and requires an external BGAPI compatible device. Bleak is platform-agnostic and can use any Windows Bluetooth interface as it uses the UWP Bluetooth Stack.

This software should be compatible with any platform that supports Bleak, which are listed by Bleak as:
* Supports Windows 10, version 16299 (Fall Creators Update) or greater
* Supports Linux distributions with BlueZ >= 5.43
* OS X/macOS support via Core Bluetooth API, from at least OS X version 10.11
* Android backend compatible with python-for-android

# Usage
See `__main__.py` for a full example in action.

```python
import time
from govee_btled_windows import BluetoothLED

led = BluetoothLED('<your MAC here>')
led.set_state(True)
led.set_color('blue')
time.sleep(1)
led.set_color('#facd03')
time.sleep(1)
# The bulb seems to have a white-mode which uses cold/warm white LEDs instead of the RGB LEDs.
# Supply a value between -1 (warm) and 1 (cold)
led.set_color_white(-0.4)
```

# Also included...
On the root of the repo, there are two additional Python scripts:
* ```govee_payload_generator.py``` generates the 20 bytes long payload that would be sent to the bulb via BLE. Useful for troubleshooting.
* ```search_btle.py``` returns a ```dict``` of MAC Addresses and Device Names of the devices of interest given a search phrase. Useful to integrate into programs where you do not know the MAC Address of the BLE devices you want to interact with (e.g. a room full of Govee bulbs...)

# Reverse Engineering of H6001 BLE Packets
[Have a look here for how the BLE packets that control the state of the LED bulb were reverse engineered. ](https://github.com/egold555/Govee-Reverse-Engineering/blob/master/Products/H6127.md)

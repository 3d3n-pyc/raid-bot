import pystyle
import time

LocheMan_WaterMark = ['\n  ╔╗           ╔╗      ╔═╗╔═╗         ', '  ║║           ║║      ║║╚╝║║         ', '  ║║   ╔══╗╔══╗║╚═╗╔══╗║╔╗╔╗║╔══╗ ╔═╗ '\
                      , '  ║║ ╔╗║╔╗║║╔═╝║╔╗║║╔╗║║║║║║║╚ ╗║ ║╔╗╗', '  ║╚═╝║║╚╝║║╚═╗║║║║║║═╣║║║║║║║╚╝╚╗║║║║', '  ╚═══╝╚══╝╚══╝╚╝╚╝╚══╝╚╝╚╝╚╝╚═══╝╚╝╚╝']

def watermark():
    for part in LocheMan_WaterMark:
        print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_red, part, 1))
        time.sleep(0.05)
    print()
import os
import time

from compal import Compal, WifiSettings

modem = Compal(os.environ['router_IP'], os.environ['router_ACCESS'])
modem.login()
# restore_wifi_settings(modem)
wifi = WifiSettings(modem)
wifi.turn_off()

# Wait for 8h
time.sleep(5 * 60)
wifi.turn_on_2g()

import os
import sys
import time

sys.path.append(os.getcwd())
from compal import Compal, WifiSettings

modem = Compal(os.environ['router_IP'], os.environ['router_ACCESS'])
modem.login()

print("Succesful logged into router")
# restore_wifi_settings(modem)
wifi = WifiSettings(modem)
wifi.turn_off()
print("Turned off both wifi")

# Wait for 8h
time.sleep(5 * 60)
wifi.turn_on_2g()
print("Turned on 2g")

from wakeonlan import send_magic_packet
import os
import time
from tcping import Ping

# packetto in Broadcast su port 9


#katia
print("Katia-pc ... ",end="")
send_magic_packet('1C.B7.2C.38.D8.EE', ip_address='255.255.255.255',port=9)
print('OK')

time.sleep(6)

filepath = 'connection.rdp'
os.startfile(filepath)

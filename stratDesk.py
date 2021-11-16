


from  configparser import ConfigParser
from wakeonlan import send_magic_packet
import os
import time
#from tcping import Ping

# read configurations
config = ConfigParser()
config.read('settings.ini')
print(config['pc']['name'])
print(config['pc']['mac'])


# packetto in Broadcast su port 9
print("Pc in accensione ... ",end="")
send_magic_packet('1C.B7.2C.38.D8.EE', ip_address='255.255.255.255',port=9)

time.sleep(6)
print('OK')


filepath = 'connection.rdp'
os.startfile(filepath)

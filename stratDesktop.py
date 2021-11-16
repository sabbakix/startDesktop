
from  configparser import ConfigParser
from wakeonlan import send_magic_packet
import os
import time
#from tcping import Ping

# clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# read configurations
config = ConfigParser()
config.read('settings.ini')
#print(config['pcRemoto']['name'])

#send_magic_packet(config['pcRemoto']['mac'], ip_address='255.255.255.255',port=9)
send_magic_packet(config['pcRemoto']['mac'])
#send_magic_packet(config['pcRemoto']['mac'], interface=config['pcLocale']['ip'])

for x in range(0,21):
    cls()
    print("Pc in accensione "+str(20-x))
    time.sleep(1)

print('OK')

filepath = config['pcRemoto']['rdpfile']
os.startfile(filepath)

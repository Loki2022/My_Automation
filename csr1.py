from netmiko import ConnectHandler
from getpass import getpass
csr1 =ConnectHandler(ip = '192.168.1.101' , username = 'admin', password = getpass('Enter passwrod: '), device_type ='cisco_xe')

send_cmd = ['int gi1' , 'no shut', 'ip add 10.1.12.1 255.255.255.0']
output = csr1.send_config_set(send_cmd)
print(output)
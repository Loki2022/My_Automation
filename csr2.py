from netmiko import ConnectHandler
from getpass import getpass 
csr2 = ConnectHandler( ip = '192.168.1.102', username = 'admin', password = getpass('enter password: '), device_type = 'cisco_ios')
send_cmd = ['int g1', 'no shut', 'ip address 10.1.12.2 255.255.255.0'] 
output = csr2.send_config_set(send_cmd)
print(output)

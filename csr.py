from netmiko import ConnectHandler
csr5 = {'ip':'192.168.1.75','username':'admin', 'password': 'cisco', 'device_type': 'cisco_ios'}
csr6 = {'ip':'192.168.1.76','username':'admin', 'password': 'cisco', 'device_type': 'cisco_ios'}
csr7 = {'ip':'192.168.1.77','username':'admin', 'password': 'cisco', 'device_type': 'cisco_ios'}

lst = [csr5,csr6,csr7]

for csr in lst:
    print('connecting to csr' + csr['ip'])
    connect = ConnectHandler(**csr)
    send = ["do sh ip int brie"]
    output =connect.send_config_set(send)
    print(output)

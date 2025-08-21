from netmiko import ConnectHandler

csr1 = {'ip':'192.168.1.101', 'username': 'admin', 'password': 'cisco','device_type':'cisco_xe'}
csr2 = {'ip':'192.168.1.102', 'username': 'admin', 'password': 'cisco','device_type':'cisco_xe'}
csrs = [csr1]

with open('csr1') as f:
    lines=(f.read().splitlines())
print(lines)

for csr in csrs:
    print('connecting to csr1' + csr['ip'])
    connect = ConnectHandler(**csr)
    output = connect.send_config_set(lines)
    print(output)

csrs = [csr2]
with open ('csr2') as f:
    lines = (f.read().splitlines())
print(lines)

for csr in csrs:
    print ('connecting to csr2' + csr['ip'])
    connect = ConnectHandler(**csr)
    output = connect.send_config_set(lines)
    print(output)
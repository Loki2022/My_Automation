from netmiko import ConnectHandler

sw1 = { 'ip' : '192.168.1.61', 'username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}
sw2 = { 'ip' : '192.168.1.62', 'username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}
sw3 = { 'ip' : '192.168.1.63', 'username':'admin', 'password':'cisco', 'device_type':'cisco_ios'}

switches = [sw1]
with open('sw1') as f:
    lines=(f.read().splitlines())
print(lines)

for sw in switches:
    print('connecting to sw1 ' + sw['ip'])
    connect = ConnectHandler(**sw)
    output = connect.send_config_set(lines)
    print(output)

switches = [sw2]
with open('sw2') as f:
    lines=(f.read().splitlines())
print(lines)

for sw in switches:
    print('connecting to sw2 ' + sw['ip'])
    connect = ConnectHandler(**sw)
    output = connect.send_config_set(lines)
    print(output)
    
switches = [sw3]
with open('sw3') as f:
    lines=(f.read().splitlines())
print(lines)

for sw in switches:
    print('connecting to sw3 ' + sw['ip'])
    connect = ConnectHandler(**sw)
    output =connect.send_config_set(lines)
    print(output)



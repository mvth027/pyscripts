import re

dhcpPool = '''
!
ip dhcp pool POOL0
 network 172.16.0.0/24
 domain-name cisco.com
 dns-server 172.16.1.102 172.16.2.102
 netbios-name-server 172.16.1.103 172.16.2.103 
 netbios-node-type h-node
!
ip dhcp pool POOL1
 network 172.16.1.0/24
 default-router 172.16.1.100 172.16.1.101 
 lease 30 
!
ip dhcp pool POOL2
 network 172.16.2.0/24
 default-router 172.16.2.100 172.16.2.101 
 lease 30
'''

regex = ('ip dhcp pool (\w+)')
regexX = ('network \w+.\w+.\w+.\w+/\w+')

m = re.findall(regex, dhcpPool)
n = re.findall(regexX, dhcpPool)

x = dict(zip(m,n))

for key, value in x.items():
        print(key, value)


























#print (dhcpPool)

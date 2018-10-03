import re

dhcpPool = '''
ip dhcp pool HEX_WIFI.KIROV.KB.HLYNOV.Urickogo40
 vrf HEX-WIFI
 network 100.68.3.0 255.255.255.224
 dns-server 213.87.2.88 213.87.2.89 
 default-router 100.68.3.1 
 lease 0 0 8
ip dhcp pool HEX_WIFI.KIROV.KB.HLYNOV.Vorovskogo135
 vrf HEX-WIFI
 network 100.68.2.192 255.255.255.224
 dns-server 213.87.2.88 213.87.2.89 
 default-router 100.68.2.193 
 lease 0 0 8
ip dhcp pool HEX_WIFI.KIROV.KB.HLYNOV.Oktyabskiy155
 vrf HEX-WIFI
 network 100.68.3.64 255.255.255.224
 dns-server 213.87.2.88 213.87.2.89 
 default-router 100.68.3.65 
 lease 0 0 8
'''

interfaces = '''
Port-channel1.15201401 100.68.3.129    YES manual up                    up      
Port-channel1.15201409 100.68.3.33     YES manual up                    up      
Port-channel1.15201413 100.68.3.225    YES manual up                    up      
Port-channel1.15201447 100.68.3.161    YES manual up                    up      
Port-channel1.15201456 100.68.3.193    YES manual up                    up      
Port-channel1.15201701 100.68.3.97     YES manual up                    up      
Port-channel1.15203454 100.68.3.1      YES manual up                    up      
Port-channel1.15203496 100.68.3.65     YES manual up                    up
Port-channel1.15201465 100.68.2.97     YES NVRAM  up                    up      
Port-channel1.15201493 100.68.2.65     YES manual up                    up      
Port-channel1.15201704 100.68.2.1      YES NVRAM  up                    up      
Port-channel1.15201712 100.68.2.225    YES manual up                    up      
Port-channel1.15201716 100.68.2.129    YES NVRAM  up                    up      
Port-channel1.15203495 100.68.2.193    YES manual up                    up
'''

poolNameFind = ('ip dhcp pool (\S+)')
networkFind = ('network \w+.\w+.\w+.\w+ \w+.\w+.\w+.\w+')
defaultRouterFind = ('default-router (\w+.\w+.\w+.\w+)')
portChannelFind = ('Port-channel1.\d+')
IPinterfacesFind = ('100.\d+.\d+.\d+')
poolName = re.findall(poolNameFind, dhcpPool)
network = re.findall(networkFind, dhcpPool)
defaultRouter = re.findall(defaultRouterFind, dhcpPool)
portChannel = re.findall(portChannelFind, interfaces)
IPinterface = re.findall(IPinterfacesFind, interfaces)
intDict = dict(zip(IPinterface,portChannel,))
try:   
 i = 0
 while i <= len(poolName):
     print (str(poolName[i]))
     print (str(network[i]))
     print ("default-router " + str(defaultRouter[i]))
     print (str(intDict[defaultRouter[i]]))
     print ("")
     i += 1
except IndexError:
    print ('')

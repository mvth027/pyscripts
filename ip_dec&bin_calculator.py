r_input = input("Enter IPv4 CIDR address [x.x.x.x/xx]: ")
IP = r_input
IP = IP.split("/")


def ip_split(ipaddr):
  ip = ipaddr.split(".")
  ipl = []
  for i in ip:
    if int(i) < 256:
      ipl.append(int(i))
    else:
      pass
  return ipl


def ip2bin(ipaddr):
  binIp = []
  for i in ipaddr:
    integ = int(i)
    binary = bin(integ)
    binIp.append(binary.replace("0b",""))
  binIpNew = [str(binIp[0]).rjust(8,"0"),str(binIp[1]).rjust(8,"0"),str(binIp[2]).rjust(8,"0"),str(binIp[3]).rjust(8,"0")]
  return binIpNew

def mask_validator(mask):
  m = int(mask)
  if m < 33:
    return m
  else:
    pass


def mask2bin(mask):
  bin_mask = int(mask)*"1"
  bitmask = bin_mask.ljust(32,"0")
  bitmask = [bitmask[0:8],bitmask[8:16],bitmask[16:24],bitmask[24:32]]
  return bitmask


def mask255(binaryMask):
  a = binaryMask
  mask = [int(a[0],2),int(a[1],2),int(a[2],2),int(a[3],2)]
  return mask

def wildcard_maker(binaryMask):
  a = binaryMask
  mask = [255 - int(a[0],2),255 - int(a[1],2),255 - int(a[2],2),255 - int(a[3],2)]
  return mask


def networkCalc(binaryIP,binaryMask):
  a = binaryIP
  b = binaryMask
  network = [int(a[0],2) & int(b[0],2),int(a[1],2) & int(b[1],2),int(a[2],2) & int(b[2],2),int(a[3],2) & int(b[3],2)]
  return network


def broadcast_counter(ntCalc,wildMask):
  a = ntCalc
  b = wildMask
  counter = [a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]]
  return counter


def maxhost_counter(broadcast):
  a = broadcast
  max_host = [a[0],a[1],a[2],(a[3]-1)]
  return max_host


def minhost_counter(network):
  a = network
  min_host = [a[0],a[1],a[2],(a[3]+1)]
  return min_host


def total_hosts(mask):
  a = int(mask)
  if a == 31:
    return 2
  elif a == 32:
    return 0
  else:
    total = 2 ** (32-a)-2
    return total

# variables here:
try:
 source_ip = ip_split(IP[0])
 binIpAddr = ip2bin(source_ip)
 mask = mask_validator(IP[1])
 binMask = mask2bin(mask)
 decMask = mask255(binMask)
 wildMask = wildcard_maker(binMask)
 ntCalc = networkCalc(binIpAddr,binMask)
 broadcast = broadcast_counter(ntCalc,wildMask)
 max_host = maxhost_counter(broadcast)
 min_host = minhost_counter(ntCalc)
 hosts = total_hosts(mask)
except IndexError:
  print ("You entered wrong IP address. Check your input and try again")
except TypeError:
  print ("You entered wrong IP address. Check your input and try again")
except ValueError:
  print ("You entered wrong IP address. Check your input and try again")
except NameError:
  print ("You entered wrong IP address. Check your input and try again")
# /variables -----------

def ipCalculator():
  print ("IP address: " + str(source_ip[0]) + "." + str(source_ip[1]) + "." + str(source_ip[2]) + "." + str(source_ip[3]))
  print ("Network:")
  print (str(ntCalc[0]).ljust(8),str(ntCalc[1]).ljust(8),str(ntCalc[2]).ljust(8),str(ntCalc[3]).ljust(8))
  print (binIpAddr[0],binIpAddr[1],binIpAddr[2],binIpAddr[3]+"\n")
  print ("Mask:")
  print ("/" + str(mask))
  print (str(decMask[0]).ljust(8),str(decMask[1]).ljust(8),str(decMask[2]).ljust(8),str(decMask[3]).ljust(8))
  print (binMask[0],binMask[1],binMask[2],binMask[3]+"\n")
  if mask == 32:
    pass
  elif mask == 31:
    print ("First host: " + str(min_host[0]) + "." + str(min_host[1]) + "." + str(min_host[2]) + "." + str(min_host[3]-1))
    print ("Last host:  " + str(max_host[0]) + "." + str(max_host[1]) + "." + str(max_host[2]) + "." + str(max_host[3]+1))
    print ("Broadcast:  " + str(broadcast[0]) + "." + str(broadcast[1]) + "." + str(broadcast[2]) + "." + str(broadcast[3]))
    print ("Maximum hosts: " + str(hosts))    
  else:
    print ("First host: " + str(min_host[0]) + "." + str(min_host[1]) + "." + str(min_host[2]) + "." + str(min_host[3]))
    print ("Last host:  " + str(max_host[0]) + "." + str(max_host[1]) + "." + str(max_host[2]) + "." + str(max_host[3]))
    print ("Broadcast:  " + str(broadcast[0]) + "." + str(broadcast[1]) + "." + str(broadcast[2]) + "." + str(broadcast[3]))
    print ("Maximum hosts: " + str(hosts))
  return 

ipCalculator()

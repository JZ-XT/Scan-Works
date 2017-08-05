import layer4


class scanner(object):
    def __init__(self):  
        self.rand = True
        self.toFind = 10
        self.startIP = ''
        self.endIP = ''
        self.port = 22
    
    def scan(self):
        ips = []
        if self.rand:
            found = 0
            while (found <= self.toFind):
                ip = layer4.gen()
                if (layer4.hostAlive(ip)):
                    if (layer4.portCheck(ip, self.port)):
                        ips.append(ip)
                        found += 1
            return ips
        else:
            iprange = layer4.genRange(self.startIP, self.endIP)
            for ip in iprange:
                if (layer4.hostAlive(ip)):
                    if (layer4.portCheck(ip, self.port)):
                        ips.append(ip)
            return ips



s = scanner()
s.toFind = 1
ips = s.scan()
print(ips)

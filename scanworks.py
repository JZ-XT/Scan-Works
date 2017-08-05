import layer4


class scanner(object):
    def __init__(self):  
        self.rand = True
        self.toFind = 10
        self.startIP = ''
        self.endIP = ''
        self.port = 22 # Set To 0 to find only alive ips
    
    def scan(self):
        ips = []
        if self.rand:
            found = 0
            while (found <= self.toFind - 1):
                ip = layer4.gen()
                if (layer4.hostAlive(ip)):
                    if (self.port == 0):
                        ips.append(ip)
                        found += 1
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

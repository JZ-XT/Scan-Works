import layer4, proto

while (True):
    ip = layer4.gen()
    if (layer4.hostAlive(ip)):
        if (layer4.portCheck(ip, 22)):
            if (proto.ssh.checkKippo(ip)):
                 print '[-] Kippo Running on\t:\t'+ip
         else:
            print '[-] SSH Not Running on\t:\t'+ip
    else:
        pass

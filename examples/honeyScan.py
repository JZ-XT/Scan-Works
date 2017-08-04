import layer4, proto

while (True):
    ip = layer4.gen()
    if (layer4.hostAlive(ip)):
        if (layer4.portCheck(ip, 22)):
            proto.ssh.checkKippo(ip)

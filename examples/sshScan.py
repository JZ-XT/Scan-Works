import layer4, proto

while (True):
    ip = layer4.gen()
    if (layer4.hostAlive(ip)):
        if (layer4.portCheck(ip, 22)):
            print '[+] SSH Is Running On\t:\t'+ip
            with open("sshOpen.txt", "a") as myfile:
                myfile.write(ip + '\n')
        else:
            print '[-] SSH Not Running on\t:\t'+ip
    else:
        pass

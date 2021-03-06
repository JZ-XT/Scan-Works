import socket, struct, random, os
#from subprocess import Popen

def gen():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def genRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
        ip_range.append(".".join(map(str, temp)))
    return ip_range

def portCheck(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
    except Exception:
        return False
    return True

def hostAlive(hostname):
    response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
    #response = Popen("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1", shell=True).wait()
    if response == 0:
        return True
    else:
        return False

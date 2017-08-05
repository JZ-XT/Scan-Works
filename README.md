# Scan Works
*Easy to use python libary for scanning and interacting with internet.*

---  
<p align="center">  
  <img src="http://i.imgur.com/BsbjJzf.png"> 
  <img src="http://i.imgur.com/h4L0mLF.png"> 
</p>  

### What is it?
Scan Works is a easy to use python libary designed for scanning the internet. Designed ground up for easy of use Scan Works provides several modules for scanning and interacting with several protocols allowing complex systems to be built on top of it.
From scanning the entire internet for http/s servers to automaticly hacking all the ssh servers you can find Scan Works caters to all types of developer 

### It's *Modular*
Our code is useable as a module system for our fellow devs. Providing individual files for diffrent tasks for example: layer4.py provides all the functions for interacting with tcp/ip including: ip and ip range generation, port scanning, and host alive checks

### Example Usage
Basic Http Scanner using random ip generation
```python
import layer4
while (True):
    ip = layer4.gen()
    if (layer4.hostAlive(ip)):
        if (layer4.portCheck(ip, 80)):
            print '[+] Http Is Running On\t:\t'+ip
        else:
            print '[-] Http Is Not Running on\t:\t'+ip
    else:
        pass
```


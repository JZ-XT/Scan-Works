# Scan Works
*Easy to use python libary for scanning and interacting with internet.*

---  
<p align="center">  
  <img src="http://i.imgur.com/BsbjJzf.png"> 
</p>  

### What is it?
Scan Works is a easy to use python libary designed for scanning the internet. Designed ground up for easy of use Scan Works provides several modules for scanning and interacting with several protocols allowing complex systems to be built on top of it.
From scanning the entire internet for http/s servers to automaticly hacking all the ssh servers you can find Scan Works caters to all types of developer 

### It's *Modular*
Our code is useable as a module system for our fellow devs. Providing individual files for diffrent tasks for example: layer4.py provides all the functions for interacting with tcp/ip including: ip and ip range generation, port scanning, and host alive checks

### Example Usage
Http Scanner using default settings
```python
from scanworks import scanner
scanner = scanner()
scanner.port = 80
ips = scanner.scan()
print(ips)
```


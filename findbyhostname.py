import subprocess
import socket
import ipaddress

class nmap:

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        finally:
            s.close()


    def ipGrab(self):
        self.local_ip = self.get_local_ip()
        self.network = ipaddress.ip_network(self.local_ip + "/24", strict=False)
        
        print(f"\nYour local IP: {self.local_ip}")
        print(f"Detected network: {self.network}")

        self.user_confirm = input(f"Is This Correct? (y/n): ")
        if (self.user_confirm == "y" or self.user_confirm == ""):
            self.commandCall(str(self.network))
        elif self.user_confirm == 'n':
            self.network = input(f"Enter IP/Port#: ")
            self.commandCall(self.network)
        else:
            print("Input not excepted. Type either y or n.")
            self.ipGrab()
    
    def commandCall(self,ip):
        print(f"\nRunning nmap scan on {ip}...\n")
        
        self.result = subprocess.run(
            ["nmap", "--open", "-p 22", "-sT", ip],
            capture_output=True,
            text=True
        )

        self.output = self.result.stdout
        
        self.findByHostname()
    
    def findByHostname(self):
        self.search = self.userHost.lower().strip()
        self.resultArray = []
        for line in self.output.splitlines():
            if self.search in line.lower():
                self.result = print(line)
                self.resultArray.append(line)
                self.result
        if not self.resultArray:
            print(f"Hostname {self.userHost} Not Found.")
    
    def userHostname(self):
        self.userHost = input("Enter Hostname of Device: ")

        if " " in self.userHost:
            print("Hostname Should Not Contain Any Spaces. Try Again.")
            self.userHostname()
        self.ipGrab()

nmap = nmap()
nmap.userHostname()

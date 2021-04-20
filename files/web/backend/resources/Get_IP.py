import os

class Get_IP:
    def return_ip(): 
        os.system("hostname -I | awk '{print $3}' | tee /etc/hobby-hub/wifi_scan/ip.txt >/dev/null 2>&1")
        f = open("/etc/hobby-hub/wifi_scan/ip.txt", "r")
        board_ip = f.read()
        f.close()
        return board_ip.strip()
    
    def check_ping():
        response = os.system("ping -c 4 www.google.com >/dev/null 2>&1")
        
        return True if response == 0 else False
    
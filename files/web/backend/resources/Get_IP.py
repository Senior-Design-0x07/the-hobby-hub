import os

class Get_IP:
    def return_ip(): 
        os.system("hostname -I | awk '{print $3}' | tee /etc/hobby-hub/wifi_scan/ip.txt")
        f = open("/etc/hobby-hub/wifi_scan/ip.txt", "r")
        board_ip = f.read()
        f.close()
        return board_ip
    
    def check_ping():
        response = os.system("ping -4 www.google.com")
        if response == 0:
            return True
        else:
            return False


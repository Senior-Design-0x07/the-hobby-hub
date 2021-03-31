import os

class Get_IP:
    os.system("hostname -I | awk '{print $3}' | tee /etc/hobby-hub/wifi_scan/ip.txt")
    f = open("/etc/hobby-hub/wifi_scan/ip.txt", "r")
    board_ip = f.read()
    f.close()
    return board_ip


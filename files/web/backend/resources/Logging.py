from flask_restful import Resource

from hobby_hub_pkg.Log import Log

class Logging(Resource):
    def get(self, cmd):
        if(cmd == 'get'):
            logs = []
            f = open("/etc/hobby-hub/log.txt", "r")
            unformatted_logs = f.readlines()
            f.close()
            for line in unformatted_logs:
                logs.append(line.strip())
            return logs
        elif(cmd == 'clear'):
            syslog = Log()
            syslog.clear()
            return 'true' if True else False        

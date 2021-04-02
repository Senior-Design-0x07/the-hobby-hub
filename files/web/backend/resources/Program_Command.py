from flask_restful import Resource

class Program_Command(Resource):
    # Program Manager - Commands (Pause, Continue, Stop, Start)
    def get(self, cmd, program_name):
        if(cmd == 'pause_program'):
            # pause the supplied program (provided program is running)
            os.command("sudo hobby-hub -p " + program_name)

        elif(cmd == 'continue_program'):
            # continue the supplied program (provided program is paused)
            os.command("sudo hobby-hub -c " + program_name)

        elif(cmd == 'stop_program'):
            # stop the supplied program completely (provided program is running)
            os.command("sudo hobby-hub -s " + program_name)

        elif(cmd == 'start_program'):
            # start the supplied program
            os.command("sudo hobby-hub -t " + program_name)

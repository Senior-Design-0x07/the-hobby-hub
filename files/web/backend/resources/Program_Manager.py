from flask_restful import Resource, reqparse
import os

parser = reqparse.RequestParser()
parser.add_argument("command", type=str, required=True)
parser.add_argument("program", type=str, required=True)

class Program_Manager(Resource):
    # Program Manager - Retrieve Running/Pause Programs Lists
    def get(self, cmd):
        if(cmd == 'running_programs'):
            # obtain list of running programs from text file
            running_programs_raw = []
            running_programs_list = []
            with open("/etc/hobby-hub/out/running_programs.txt", "r") as f:
                # parse list into individual lines
                running_programs_raw = f.readlines()
                f.close()

                for line in running_programs_raw:
                    running_programs_list.append(line.strip())                    
                
            return running_programs_list

        elif(cmd == 'paused_programs'):
            # obtain list of paused programs from text file
            paused_programs_raw = []
            paused_programs_list = []
            with open("/etc/hobby-hub/out/paused_programs.txt", "r") as f:
                # parse list into individual lines
                paused_programs_raw = f.readlines()
                f.close()

                for line in paused_programs_raw:
                    paused_programs_list.append(line.strip())

            return paused_programs_list
    # Program Manager - Program Commands
    def post(self, cmd):
        args = parser.parse_args()
        if(cmd == 'pause_program'):
            # pause the supplied program (provided program is running)
            program_command = "sudo hobby-hub -p " + args["program"]
            os.system(program_command)

        elif(cmd == 'continue_program'):
            # continue the supplied program (provided program is paused)
            program_command = "sudo hobby-hub -c " + args["program"]
            os.system(program_command)

        elif(cmd == 'stop_program'):
            # stop the supplied program completely (provided program is running)
            program_command = "sudo hobby-hub -s " + args["program"]
            os.system(program_command)

        elif(cmd == 'start_program'):
            # start the supplied program
            program_command = "sudo hobby-hub -t " + args["program"]
            os.system(program_command)

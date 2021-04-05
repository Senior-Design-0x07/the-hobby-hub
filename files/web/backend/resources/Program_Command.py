from flask_restful import Resource, reqparse
import os

parser = reqparse.RequestParser()
parser.add_argument("command", type=str, required=True)
parser.add_argument("program", type=str, required=True)

class Program_Command(Resource):
    # Program Manager - Program Commands
    def post(self):
        args = parser.parse_args()
        if(args["command"] == 'pause_program'):
            # pause the supplied program (provided program is running)
            program_command = "sudo hobby-hub -p " + args["program"]
            os.system(program_command)

        elif(args["command"] == 'continue_program'):
            # continue the supplied program (provided program is paused)
            program_command = "sudo hobby-hub -c " + args["program"]
            os.system(program_command)

        elif(args["command"] == 'stop_program'):
            # stop the supplied program completely (provided program is running)
            program_command = "sudo hobby-hub -s " + args["program"]
            os.system("sudo hobby-hub -s " + args["program"])

        elif(args["command"] == 'start_program'):
            # start the supplied program
            program_command = "sudo hobby-hub -t " + args["program"]
            os.system(program_command)

from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("program_name", type=str, help="Program name required", required=True)

class Program_Manager(Resource):
    def get(self):
        # obtain list of running programs from text file
        running_programs = ""
        with open("/etc/hobby-hub/out/running_programs.txt", "r") as f:
            running_programs = f.read()
            f.close()
        return running_programs
    
    # take program name as argument for program manager commands from frontend
    def post(self):
        args = parser.parse_args()

        print("REQUEST: ")
        print("   Program Name: " + args["program_name"])

        # invoke program manager command (pause a running program)
        # subprocess.run("/home/debian/the-hobby-hub/files/system/commands/pause_process.sh", args["program_name"])
        os.command("sudo hobby-hub -p " + args["program_name"])
        return None

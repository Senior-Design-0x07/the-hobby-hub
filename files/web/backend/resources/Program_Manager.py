from flask_restful import Resource

class Program_Manager(Resource):
    # Program Manager - Retrieve Running/Pause Programs Lists
    def get(self, program_list):
        if(program_list == 'running_programs'):
            # obtain list of running programs from text file
            running_programs_raw = []
            running_programs_list = []
            with open("/etc/hobby-hub/out/running_programs.txt", "r") as f:
                # parse list into individual lines
                running_programs_raw = f.readLines()
                f.close()

                for line in running_programs_raw:
                    running_programs_list.append(line.strip())

            return running_programs_list

        elif(program_list == 'paused_programs'):
            # obtain list of paused programs from text file
            paused_programs_raw = []
            paused_programs_list = []
            with open("/etc/hobby-hub/out/paused_programs.txt", "r") as f:
                # parse list into individual lines
                paused_programs_raw = f.readLines()
                f.close()

                for line in paused_programs_raw:
                    paused_programs_list.append(line.strip())

            return paused_programs_list

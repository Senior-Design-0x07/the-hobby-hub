from flask_restful import Resource
from flask import redirect, url_for
import subprocess, sys

# Not Used, Anthony Used this with the web demo in Wk3
# Something like this will be used to access ROCK's Programming manager I think

class test_program1(Resource):
    def get(self):
        subprocess.run([sys.executable, "/etc/hobby-hub/test_programs/light1.py"])
        print("Program Finished")
        return redirect("http://192.168.7.2:5000/")

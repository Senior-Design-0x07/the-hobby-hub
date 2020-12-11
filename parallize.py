#!/usr/bin/env python3

import os
import sys
import argparse
from subprocess import Popen
from pathlib import Path


def main(arguments):
    """Takes a directory containing user programs and runs them as seperate processes

    Only runs .c, .cpp, and .py files for now
    For .c files:
        Uses a makefile if in the directory, or gcc to compile

    Args:
        arguments (string): [description]
    """
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('program_directory',
                        help="Directory containing user programs to run",
                        type=dir_path)

    # TODO add output file for each program in a specified output directory

    args = parser.parse_args(arguments)

    # get directory of programs
    program_dir = Path(args.program_directory)

    # extract programs
    py_files = list(program_dir.glob('**/*.py'))
    c_files = list(program_dir.glob('**/*.c'))
    cpp_files = list(program_dir.glob('**/*.cpp'))

    # TODO compile c files

    programs = py_files + c_files + cpp_files
    program_ids = []

    for program in py_files:
        pid = Popen(["python3", program]).pid
        program_ids.append(pid)

    # iterate over each of the .c and .py files in the directory

    # kickoff each program

    print(f'Now running:')
    for program, pid in zip(programs, program_ids):
        print(f'Program: {program}, pid: {pid}')


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
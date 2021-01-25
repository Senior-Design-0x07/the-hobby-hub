#!/usr/bin/env python3

import os
import sys
import argparse
from subprocess import Popen, run
from pathlib import Path


def main(arguments):
    """Takes a directory containing user programs and runs them as seperate processes

    May require elevated priveges if the supplied directory is restricted (i.e. use
    sudo when calling this)

    Only runs .c, .cpp, and .py files for now
    For .c and .cpp files:
        Uses g++ to compile and places excecutable in program_directory/obj

    Args:
        arguments (list): list of arguments
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

    programs = {} # program name : program id

    for program in py_files:
        pid = Popen(["python3", program]).pid
        programs[program] = pid

    #if c_files or cpp_files:
        #print('Compiling source files...')

    Path(program_dir, 'obj').mkdir(exist_ok=True)
    for source_file in c_files + cpp_files:
        program = Path(source_file.parent, 'obj', source_file.name.split('.')[0])
        run(["g++", '-o', program, source_file])
        pid = Popen([program]).pid
        programs[program] = pid

    #if c_files or cpp_files:
        #print('Finished compilation')

    #print(f'Now running:')
    for program, pid in programs.items():
        print(f'{program} {pid}')


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    
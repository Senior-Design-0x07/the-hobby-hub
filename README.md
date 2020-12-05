# the-hobby-hub
An embedded hub device to concurrently run multiple, single-task programs.


# Setup Instructions
1. clone this repository into the beaglebone green: `git clone https://github.com/Senior-Design-0x07/the-hobby-hub.git`
2. run command: `sudo ./the-hobby-hub/setup.sh`
3. Enter the user password when prompted


## Repo file description
Top level directory provides entry point into the system. 
`/scripts` provides shell scripts that will recursivly be run upon setup
`/files` provides files or programs to be installed upon the device (in a logical orginizaional mannor)
`/docs` provides documentation and reference documents for developers and users
setup.sh is the executable to setup the hobby-hub utilities on the board.

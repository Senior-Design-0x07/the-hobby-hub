#/bin/sh

# Author : 
# Description :

# flag to denote if you want fast setup
FAST=0
# flag to denote if you want to reboot or not.
REBOOT=1
# flag to display help menu
HELP=0

# first ensure script is run as root...
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi


for arg do

  if [ $arg = "fast" ]
  then
    FAST=1
  fi

  if [ $arg = "no-reboot" ]
  then
    REBOOT=0
  fi

  if [ $arg = "help" ]
  then
    HELP=1
  fi

  if [ $arg = "h" ]
  then
    HELP=1
  fi

done

if [ $HELP -eq 1 ]
then
  echo "setup script for the hobby-hub device."
  echo "no-reboot option does not reboot the device upon completion"
  echo "fast option skips remote device module update"
else 

echo ""
echo ""
echo "Running hobby-hub setup script."
echo "This may take a few moments..."
echo""

if [ $FAST -eq 0 ]
then
  echo "||||||||||||||||||||||||||||||||"
  echo "||| updating device packages |||"
  echo "||||||||||||||||||||||||||||||||"
  echo ""
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install openssh-server
fi

mkdir -p /etc/hobby-hub/


echo "||||||||||||||||||||||||||||||||"
echo "||| processing sub-scripts  ||||"
echo "||||||||||||||||||||||||||||||||"
echo""
for f in scripts/*.sh
do
  printf '%s\n' "[Processing sub-script: $f]"
  if [ $FAST -eq 0 ]
  then
    sh $f
  else
    sh $f $FAST
  fi
done
echo"" 

echo "||||||||||||||||||||||||||||||||"
echo "||||||| setup complete! ||||||||"
echo "||||||| restarting...   ||||||||"
echo "||||||||||||||||||||||||||||||||"
echo ""
sleep 3

if [ $REBOOT -eq 1 ]
then
  sudo reboot
fi

fi # help menu

